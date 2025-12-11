import pandas as pd
from geopy.distance import geodesic

# df = pd.read_csv('q-geospatial-excel-gap.csv')
# df['pps'] = df['Population'] / df['Our_Stores']
# print(df.sort_values(by='pps', ascending=False).head())

###########################################################################################################################

# origin = (40.785533, -73.944110)
# df = pd.read_csv('q-geospatial-python-proximity.csv')
# print(df[df.apply(lambda x: geodesic(origin, (x['latitude'], x['longitude'])).kilometers <= 1.2, axis=1)])

###########################################################################################################################


import geopandas as gpd
gdf = gpd.read_file("q-geospatial-qgis-buffer-area.geojson")
projections = {
    "Default (WGS 84)": 4326,
    "Web Mercator": 3857,
    "UTM zone 33N": 32633,
    "UTM zone 33S": 32733,
    "UK National Grid": 27700,
    "UTM zone 18N (example East Coast US)": 32618,
}

buffer_meters = 500
results = {}

for name, epsg in projections.items():
    gdf_proj = gdf.to_crs(epsg=epsg)
    gdf_proj['geometry'] = gdf_proj.geometry.buffer(buffer_meters)
    dissolved = gdf_proj.dissolve()
    area_km2 = dissolved.geometry.area.iloc[0] / 1_000_000
    area_km2 = round(area_km2, 2)
    results[name] = area_km2

print("Total serviced area for different projections (km²):")
for proj, area in results.items():
    print(f"{proj}: {area}")




