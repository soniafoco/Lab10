from operator import itemgetter
import networkx as nx
import matplotlib.pyplot as plt
from database.DAO import DAO


class Model:

    def __init__(self):
        self._countries = None
        self._contiguities = None
        self._grafo = nx.Graph()
        self._idMap = {}

    def buildGrafo(self, anno):
        self._countries = DAO.getCountries(anno)
        for country in self._countries:
            self._idMap[country.cCode] = country

        self._grafo.add_nodes_from(self._countries)
        #self._grafo.clear() #SBAGLIATO (cancella nodi)
        self._grafo.clear_edges()

        self._contiguities = DAO.getContiguities(anno)

        for edge in self._contiguities:
            v1 = self._idMap[edge.state1no]
            v2 = self._idMap[edge.state2no]
            if (not self._grafo.has_edge(v1, v2)) and (not self._grafo.has_edge(v2, v1)):
                self._grafo.add_edge(v1, v2)
                print(f"added edge from {v1} and {v2}")

        print(self._grafo)

        #nx.draw(self._grafo)  # draws the networkx graph containing nodes which are declared till before
        #plt.show()  # displays the networkx graph on matplotlib canvas


    def getNumNodes(self):
        return len(self._grafo.nodes)

    def getNumEdges(self):
        return len(self._grafo.edges)

    def getEdges(self):
        result = []
        for edge in self._grafo.edges:
            result.append((self._idMap[edge.state1no], self._idMap[edge.state2no]))
        return result

    def getConnessa(self):
        connessa = list(nx.connected_components(self._grafo))
        print(len(connessa))
        return len(connessa)

    def getDegrees(self):
        nodes = self._grafo.nodes
        result = []
        for node in nodes:
            degree = self._grafo.degree(node)
            result.append((node, degree))
        return result

    def getRaggiungibili(self, stato):
        result = nx.node_connected_component(self._grafo, stato)
        return result

    def countries(self):
        return self._countries

