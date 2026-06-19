import webbrowser
import os
from model import QytetetModel
from view import HartaView


class HartaController:

    def __init__(self):
        self.model = QytetetModel()
        self.view = HartaView()

    def ekzekuto(self, output_path="harta_shqiperia.html"):


        self.view.krijo_harten_baze()

        self.view.shto_geojson(self.model.geojson_data)

        self.view.krijo_cluster()

        for _, rresht in self.model.df.iterrows():
            self.view.shto_marker(rresht)

        heat_data = self.model.merr_heat_data()
        self.view.shto_heatmap(heat_data)

        self.view.shto_legjenden()
        self.view.shto_layer_control()

        self.view.ruaj_harten(output_path)

        webbrowser.open("file://" + os.path.abspath(output_path))
        