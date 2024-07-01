from database.DB_connect import DBConnect
from model.contiguity import Contiguity
from model.country import Country


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getContiguities(anno):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select * from contiguity c where c.conttype = 1 and c.year <= %s"""

        cursor.execute(query, (anno,))

        for row in cursor:
            result.append(Contiguity(**row))

        cursor.close()
        conn.close()
        return result


    @staticmethod
    def getCountries(anno):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT co.StateAbb, co.CCode, co.StateNme 
                from contiguity c, country co
                where c.`year` <= %s
                and c.state1no = co.CCode 
                group by c.state1no ORDER BY StateAbb"""

        cursor.execute(query, (anno,))

        for row in cursor:
            result.append(Country(row["StateAbb"], row["CCode"], row["StateNme"]))

        cursor.close()
        conn.close()
        return result