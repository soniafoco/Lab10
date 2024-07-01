from operator import itemgetter
import flet as ft

class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._anno = None

    def handleCalcola(self, e):
        self.readAnno()
        if self._anno>2006 or self._anno<1816:
            self._view._txt_result.controls.append(ft.Text(f"Non sono disponibili i dati per questo anno"))
        else:

            self._model.buildGrafo(self._anno)

            numNodes = self._model.getNumNodes()
            numEdges = self._model.getNumEdges()
            connessa = self._model.getConnessa()
            gradi = self._model.getDegrees()
            gradi = sorted(gradi, key=lambda x:x[0].stateNme)

            self._view._txt_result.controls.clear()
            self._view._txt_result.controls.append(ft.Text(f"Grafo correttamente creato ({numNodes} nodi e {numEdges} archi)."))
            self._view._txt_result.controls.append(ft.Text(f"Il grafo ha {connessa} componenti connesse"))
            for nodo in gradi:
                self._view._txt_result.controls.append(ft.Text(f"{nodo[0].__str__()} -- {nodo[1]} vicini"))

        self.fillDD()

        self._view.update_page()

    def handleRaggiungibili(self, e):
        self._view._txt_result.controls.clear()
        if self._anno is None or self._stato is None:
            self._view._txt_result.controls.append(ft.Text(f"Riempire i campi!"))
        else:
            raggiungibili = self._model.getRaggiungibili(self._stato)
            if len(raggiungibili) > 0:
                self._view._txt_result.controls.append(ft.Text("Stati raggiungibili:"))
                for stato in raggiungibili:
                    self._view._txt_result.controls.append(ft.Text(f"{stato.__str__()}"))
            else:
                self._view._txt_result.controls.append(ft.Text("Non ci sono stati raggiungibili"))

        self._view.update_page()

    def readAnno(self):
        self._anno = int(self._view._txtAnno.value)

    def readStato(self, e):
        self._stato = e.control.data

    def fillDD(self):
        for country in self._model.countries():
            self._view._ddStato.options.append(ft.dropdown.Option(text=country.stateNme, data=country, on_click=self.readStato))

