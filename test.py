import requests
import pandas as pd

# response = requests.post('https://tds-2025-seven.vercel.app/',
#                          json={
#                              'regions': ["emea", "apac"],
#                              'threshold_ms': 180
#                          }
#                          )
#
# print(response.json())
#
# print(requests.get('https://tds-2025-seven.vercel.app/api?class=9E').json())
# df = pd.read_csv('q-fastapi.csv')
# print({'students': df.to_dict(orient='records')})


# import wikipedia as wk
# page = wk.WikipediaPage('India')
#
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(page.html(), 'html5lib')
# print(soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']))

import requests
from urllib.parse import urlencode

base_url = "https://nominatim.openstreetmap.org/search"
params = {
    'format': 'json',
    'limit': 10,
    'city': 'Jeddah',
    'country': 'Saudi Arabia'
}
#
# # Encode parameters
# query_string = urlencode(params)
#
# # Combine base URL and encoded parameters
# full_url = f"{base_url}?{query_string}"
#
# print(full_url)

places = requests.get(base_url, params=params)
print(places.text)
print(places[0]["boundingbox"][0])
# osm_type = 'N'
# osm_id = 3717
#
# # Build Nominatim lookup URL
# url = f"https://nominatim.openstreetmap.org/lookup?osm_ids={osm_type}{osm_id}&format=json"
#
# headers = {"User-Agent": "test"}
#
# response = requests.get(url, headers=headers)
# data = response.json()
#
# if data:
#     location = data[0]
#     print(location['lat'], location['lon'])
# else:
#     print("Not found")
