import folium
from folium.plugins import MarkerCluster, HeatMap


class HartaView:

    def __init__(self):
        self.harta = None
        self.cluster = None

    def krijo_harten_baze(self):
        #harta baze
        self.harta = folium.Map(
            location=[41.3275, 19.8187],
            zoom_start=7,
            tiles="CartoDB Positron",
            control_scale=False
        )

    def shto_geojson(self, geojson_data):
        #kufijte me geojson
        folium.GeoJson(
            geojson_data,
            name="Kufijtë e Shqipërisë",
            style_function=lambda x: {
                "fillColor":   "#e63946",
                "color":       "#c1121f",
                "weight":      2.5,
                "fillOpacity": 0.08,
                "dashArray":   "none"
            },
            
        ).add_to(self.harta)

    def krijo_cluster(self):
        #markercluster
        self.cluster = MarkerCluster(
            name="Qytetet kryesore",
            overlay=True,
            control=True
        ).add_to(self.harta)

    def shto_marker(self, rresht):
        #marker me popup per qytet
        popup_html = f"""
        <div style="
            font-family: 'Segoe UI', Arial, sans-serif;
            min-width: 180px;
            padding: 5px;
        ">
            <h3 style="
                margin: 0 0 8px 0;
                color: #c1121f;
                font-size: 18px;
                border-bottom: 2px solid #e63946;
                padding-bottom: 5px;
            "> {rresht['Qyteti']}</h3>
            <table style="width:100%; font-size:13px;">
                <tr>
                    <td style="color:#666; padding:3px 0;"> Popullsia:</td>
                    <td style="font-weight:bold; color:#333;">
                        {rresht['Popullsia']:,} banorë
                    </td>
                </tr>
            </table>
        </div>
        """

        folium.Marker(
            location=[rresht["Lat"], rresht["Lon"]],
            popup=folium.Popup(popup_html, max_width=250),
            tooltip=f" {rresht['Qyteti']} — kliko për detaje",
            icon=folium.Icon(icon="home", prefix="fa")
        ).add_to(self.cluster)

    def shto_heatmap(self, heat_data):
        #heatMap
        HeatMap(
            heat_data,
            name="HeatMap - Dendësia e Popullsisë",
            min_opacity=0.6,
            max_zoom=12,
            radius=50,
            blur=30,
            gradient={
                0.2: "#313695",
                0.4: "#74add1",
                0.6: "#fdae61",
                0.8: "#f46d43",
                1.0: "#d73027"
            }
        ).add_to(self.harta)

    def shto_legjenden(self):
        #legjenda
        legjenda_html = """
        <div style="
            position: fixed; bottom: 40px; left: 20px; z-index: 1000;
            background-color: white; padding: 12px 16px;
            border-radius: 8px; border: 1px solid #ddd;
            box-shadow: 0 2px 8px rgba(0,0,0,0.15);
            font-family: 'Segoe UI', Arial, sans-serif;
            font-size: 13px; min-width: 180px;
        ">
            <b style="font-size:14px; color:#333;"> Legjenda</b>
            <hr style="margin:6px 0; border-color:#eee;">
            <b style="color:#555; font-size:12px;">HeatMap - Popullsia:</b><br>
            <span style="background: linear-gradient(to right, #313695, #fdae61, #d73027);
                         display:inline-block; width:100%; height:10px;
                         border-radius:3px; margin-top:4px;"></span>
            <div style="display:flex; justify-content:space-between;
                        font-size:10px; color:#777;">
                <span>E ulët</span><span>E lartë</span>
            </div>
        </div>
        """
        self.harta.get_root().html.add_child(folium.Element(legjenda_html))

    def shto_layer_control(self):
        #kontrolli i shtresave
        folium.LayerControl(position="topright", collapsed=False).add_to(self.harta)

    def ruaj_harten(self, output_path):
        #ruaje si html
        self.harta.save(output_path)
        