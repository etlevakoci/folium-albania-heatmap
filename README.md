# Interactive Map of Albania 🇦🇱

An interactive geographical visualization of Albania built using **Python**, **Folium**, and **Pandas**. This project maps major Albanian cities, visualizes population density using heatmaps and marker clusters, and overlays official country boundaries using GeoJSON data.



## 🌟 Features

* **Centering & Zoom:** Automatically centers on Tirana, the capital city.
* **City Markers & Popups:** Displays key cities (Tirana, Durrës, Shkodër, Vlorë, Korçë) with interactive popups showing their names and population.
* **Marker Clustering:** Uses `MarkerCluster` for clean and organized visual grouping when zoomed out.
* **Population HeatMap:** Visualizes population density dynamically across regions.
* **GeoJSON Integration:** Overlays the administrative boundaries of Albania.
* **Static Export:** Saves the final output as a standalone, shareable `harta_shqiperia.html` file.

---

## 🛠️ Tech Stack & Libraries

* **Python 3.x**
* **Folium:** For generating the interactive Leaflet.js maps.
* **Pandas:** For data manipulation and structuring city coordinates/population.
* **Branca / Jinja2:** (Handled by Folium) for HTML rendering.

---

## 📁 Project Structure

```text
├── data/
│   └── albania_boundaries.geojson  # GeoJSON file for Albania's borders
├── app.py                          # Main Python script
├── harta_shqiperia.html            # Generated interactive map (Output)
└── README.md                       # Project documentation
