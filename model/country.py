from dataclasses import dataclass
@dataclass
class Country:
    stateAbb : str
    cCode : int
    stateNme : str

    def __hash__(self):
        return hash(self.cCode)

    def __str__(self):
        return f"{self.stateNme}"