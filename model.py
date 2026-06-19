import pandas as pd
import json

class QytetetModel:
    def __init__(self):
        self._te_dhenat = {
            "Qyteti":    ["Tirane",  "Durres",  "Shkoder", "Vlore",   "Korce"],
            "Lat":       [41.3275,   41.3231,   42.0683,   40.4661,   40.6167],
            "Lon":       [19.8187,   19.4414,   19.5126,   19.4914,   20.7667],
            "Popullsia": [800000,    175000,    135000,    130000,    75000],
        }
        self.df = pd.DataFrame(self._te_dhenat)
    
        with open("albania.geojson", "r", encoding="utf-8") as f:
            self.geojson_data = json.load(f)

    def merr_heat_data(self):
        max_pop = self.df["Popullsia"].max()
        return [[r["Lat"], r["Lon"], r["Popullsia"] / max_pop] for _, r in self.df.iterrows()]
