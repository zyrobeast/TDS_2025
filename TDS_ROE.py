# import json

# def extract_lsb_message(json_path):
#     # Load pixel data from JSON file
#     with open(json_path, 'r') as f:
#         data = json.load(f)

#     pixels = data["pixels"]
#     bits = ""

#     # Iterate row by row, left to right
#     for row in pixels:
#         for pixel in row:
#             r, g, b = pixel
#             bits += str(r & 1)  # LSB of Red
#             bits += str(g & 1)  # LSB of Green
#             bits += str(b & 1)  # LSB of Blue

#     # Convert bits to ASCII characters
#     message = ""
#     for i in range(0, len(bits), 8):
#         byte = bits[i:i+8]
#         if len(byte) < 8:
#             break
#         message += chr(int(byte, 2))

#     # The message is a 16-character hex string
#     return message.strip()

# if __name__ == "__main__":
#     json_file = "stego_image.json"  # Path to your JSON file
#     hidden_message = extract_lsb_message(json_file)
#     print("Extracted Hidden Message:", hidden_message)




# import pandas as pd
# import networkx as nx

# def calculate_mst_cost(csv_path):
#     """
#     Calculates the total cost (sum of edge weights) of the Minimum Spanning Tree (MST)
#     for a connected undirected graph using Kruskal's algorithm.
    
#     Args:
#         csv_path (str): Path to the CSV file containing edges (source, target, weight).
        
#     Returns:
#         int: Total MST cost in lakhs ₹.
#     """
#     # Load graph from CSV (expects columns: source, target, weight)
#     df = pd.read_csv(csv_path)
    
#     # Create an undirected weighted graph
#     G = nx.from_pandas_edgelist(df, 'source', 'target', ['weight'])
    
#     # Compute the Minimum Spanning Tree using Kruskal's algorithm
#     mst = nx.minimum_spanning_tree(G, algorithm='kruskal')
    
#     # Sum all weights in the MST
#     total_cost = sum(data['weight'] for _, _, data in mst.edges(data=True))
    
#     return int(total_cost)

# if __name__ == "__main__":
#     csv_file = "network_graph.csv"  # Replace with your actual CSV file path
#     cost = calculate_mst_cost(csv_file)
#     print(f"Minimum Spanning Tree (MST) Total Cost: ₹{cost} lakhs")



# import pandas as pd

# def calculate_hyderabad_revenue(csv_path):
#     # Load the CSV file
#     df = pd.read_csv(csv_path)

#     # Extract month from date (assuming format like "2025-Apr-15")
#     df['month'] = df['date'].str.split('-').str[1]

#     # Filter for Hyderabad in April
#     filtered = df[(df['city'] == 'Hyderabad') & (df['month'] == 'Apr')]

#     # Calculate revenue = quantity × price
#     filtered['revenue'] = filtered['quantity'] * filtered['price']

#     # Total revenue rounded to nearest integer
#     total_revenue = round(filtered['revenue'].sum())

#     return total_revenue


# if __name__ == "__main__":
#     csv_file = "sales_data.csv"  # Path to your CSV
#     total = calculate_hyderabad_revenue(csv_file)
#     print(f"Total Revenue (Hyderabad, Apr 2025): ₹{total}")



# import json

# def count_merge_conflicts(base_file, branch_a_file, branch_b_file):
#     # Load JSON files
#     with open(base_file, 'r') as f:
#         base = json.load(f)
#     with open(branch_a_file, 'r') as f:
#         branch_a = json.load(f)
#     with open(branch_b_file, 'r') as f:
#         branch_b = json.load(f)

#     conflicts = 0

#     # Iterate over all settings
#     for key in base.keys():
#         base_value = base[key].get('value')
#         a_value = branch_a[key].get('value')
#         b_value = branch_b[key].get('value')

#         # Check if value changed in both branches differently
#         if (base_value != a_value) and (base_value != b_value) and (a_value != b_value):
#             conflicts += 1

#     return conflicts

# if __name__ == "__main__":
#     base_file = "base.json"
#     branch_a_file = "branch_a.json"
#     branch_b_file = "branch_b.json"

#     total_conflicts = count_merge_conflicts(base_file, branch_a_file, branch_b_file)
#     print(f"Total Conflicts: {total_conflicts}")


# import math
# import heapq

# # Haversine formula to calculate distance between two lat/lon points
# def haversine(lat1, lon1, lat2, lon2):
#     R = 6371  # Earth radius in km
#     phi1 = math.radians(lat1)
#     phi2 = math.radians(lat2)
#     delta_phi = math.radians(lat2 - lat1)
#     delta_lambda = math.radians(lon2 - lon1)
#     a = math.sin(delta_phi / 2)**2 + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2)**2
#     c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
#     return R * c

# # List of cities with latitude and longitude
# cities = {
#     "New York": (40.7128, -74.006),
#     "Los Angeles": (34.0522, -118.2437),
#     "London": (51.5074, -0.1278),
#     "Tokyo": (35.6895, 139.6917),
#     "Osaka": (34.6937, 135.5023),
#     "Paris": (48.8566, 2.3522),
#     "New Delhi": (28.6139, 77.209),
#     "Sydney": (33.8688, 151.2093),
#     "Toronto": (43.65107, -79.347015),
#     "Mexico City": (19.432608, -99.133209),
#     "Shanghai": (31.2304, 121.4737),
#     "Dubai": (25.276987, 55.296249),
#     "Moscow": (55.7558, 37.6176),
#     "Istanbul": (41.0082, 28.9784),
#     "Mumbai": (19.076, 72.8777),
#     "Bangkok": (13.7563, 100.5018),
#     "Cape Town": (33.9249, 18.4241),
#     "Singapore": (1.3521, 103.8198),
#     "Hong Kong": (22.3193, 114.1694),
#     "Barcelona": (41.3851, 2.1734),
#     "Berlin": (52.52, 13.405),
#     "Rome": (41.9028, 12.4964),
#     "Chicago": (41.8781, -87.6298),
#     "Buenos Aires": (34.6037, -58.3816),
#     "Madrid": (40.4168, -3.7038),
#     "San Francisco": (37.7749, -122.4194),
#     "Rio de Janeiro": (22.9068, -43.1729),
#     "Seoul": (37.5665, 126.978),
#     "Santiago": (33.4489, -70.6693),
#     "Lisbon": (38.7223, -9.1393),
#     "Vienna": (48.2082, 16.3738),
#     "Amsterdam": (52.3676, 4.9041),
#     "Cairo": (30.0444, 31.2357),
#     "Jakarta": (6.2088, 106.8456),
#     "Lagos": (6.5244, 3.3792),
#     "Kuala Lumpur": (3.139, 101.6869),
#     "Vancouver": (49.2827, -123.1207),
#     "Manila": (14.5995, 120.9842),
#     "Athens": (37.9838, 23.7275),
#     "Warsaw": (52.2297, 21.0122),
#     "Budapest": (47.4979, 19.0402),
#     "Helsinki": (60.1695, 24.9354),
#     "Stockholm": (59.3293, 18.0686),
#     "Brussels": (50.8503, 4.3517),
#     "Prague": (50.0755, 14.4378),
#     "Oslo": (59.9139, 10.7522),
#     "Zurich": (47.3769, 8.5417),
#     "Tel Aviv": (32.0853, 34.7818),
#     "Doha": (25.276987, 51.520008),
#     "Dublin": (53.3498, -6.2603),
#     "Lima": (12.0464, -77.0428),
#     "Bogota": (4.711, -74.0721),
#     "Montreal": (45.5017, -73.5673),
#     "Miami": (25.7617, -80.1918),
#     "Seattle": (47.6062, -122.3321),
#     "Boston": (42.3601, -71.0589),
#     "Houston": (29.7604, -95.3698),
#     "Phoenix": (33.4484, -112.074),
#     "Dallas": (32.7767, -96.797),
#     "Atlanta": (33.749, -84.388),
#     "San Diego": (32.7157, -117.1611),
#     "Caracas": (10.4806, -66.9036),
#     "Sao Paulo": (23.5505, -46.6333),
#     "Melbourne": (37.8136, 144.9631),
#     "Auckland": (36.8485, 174.7633),
#     "Wellington": (41.2865, 174.7762),
#     "Perth": (31.9505, 115.8605),
#     "Brisbane": (27.4698, 153.0251),
#     "Copenhagen": (55.6761, 12.5683),
#     "Hanoi": (21.0285, 105.8542),
#     "Ho Chi Minh City": (10.8231, 106.6297),
#     "Taipei": (25.032969, 121.565418),
#     "Nairobi": (1.286389, 36.817223),
#     "Accra": (5.603716, -0.187),
#     "Casablanca": (33.589886, -7.603869),
#     "Algiers": (36.737232, 3.086472),
#     "Kinshasa": (4.441931, 15.266293),
#     "Kigali": (1.944072, 30.061885),
#     "Addis Ababa": (9.005401, 38.763611),
#     "Luanda": (8.838333, 13.234444),
#     "Abu Dhabi": (24.453884, 54.377343),
#     "Muscat": (23.588, 58.3829),
#     "Jeddah": (21.2854, 39.2376),
#     "Riyadh": (24.7136, 46.6753),
#     "Kuwait City": (29.3759, 47.9774),
#     "Tehran": (35.6892, 51.389),
#     "Karachi": (24.8607, 67.0011),
#     "Dhaka": (23.8103, 90.4125),
#     "Lahore": (31.5204, 74.3587),
#     "Colombo": (6.9271, 79.8612),
#     "Kathmandu": (27.7172, 85.324),
#     "Islamabad": (33.6844, 73.0479),
#     "Tashkent": (41.2995, 69.2401),
#     "Baku": (40.4093, 49.8671),
#     "Yerevan": (40.1872, 44.5152),
#     "Tbilisi": (41.7151, 44.8271),
#     "Bishkek": (42.8746, 74.5698),
#     "Kyoto": (35.02107, 135.75385),
#     "Nur-Sultan": (51.1655, 71.4272),
#     "Ulaanbaatar": (47.8864, 106.9057),
#     "Almaty": (43.2565, 76.9283),
#     "Beijing": (39.9042, 116.4074)
# }

# # Flight connections as a dictionary
# flights = [
#     ("New York","London"),("Tokyo","Sydney"),("Paris","Berlin"),("Dubai","Mumbai"),
#     ("San Francisco","Tokyo"),("Toronto","New York"),("Shanghai","Singapore"),
#     ("Los Angeles","Mexico City"),("Istanbul","Athens"),("Madrid","Rome"),
#     ("Bangkok","Hong Kong"),("Seoul","Shanghai"),("Chicago","Toronto"),
#     ("Cape Town","Nairobi"),("Melbourne","Auckland"),("Kuala Lumpur","Jakarta"),
#     ("Rio de Janeiro","Buenos Aires"),("Berlin","Prague"),("Lima","Bogota"),
#     ("Montreal","Miami"),("Santiago","Lima"),("Vancouver","San Francisco"),
#     ("Boston","Dublin"),("Oslo","Helsinki"),("Sydney","Brisbane"),("Singapore","Bangkok"),
#     ("Zurich","Vienna"),("Tokyo","Seoul"),("Dubai","Tel Aviv"),("Doha","Istanbul"),
#     ("Athens","Cairo"),("Lisbon","Madrid"),("Warsaw","Budapest"),("Houston","Phoenix"),
#     ("Dallas","Atlanta"),("Stockholm","Copenhagen"),("Hanoi","Ho Chi Minh City"),
#     ("Casablanca","Algiers"),("Abu Dhabi","Riyadh"),("Nairobi","Accra"),("Moscow","Tbilisi"),
#     ("Addis Ababa","Lagos"),("Tehran","Karachi"),("Lahore","Islamabad"),("Dhaka","Colombo"),
#     ("Kathmandu","New Delhi"),("Ulaanbaatar","Nur-Sultan"),("Brussels","Amsterdam"),
#     ("Perth","Jakarta"),("Tashkent","Bishkek"),("London","Paris"),("Los Angeles","San Francisco"),
#     ("Hong Kong","Seoul"),("Chicago","Boston"),("Rome","Vienna"),("Miami","Atlanta"),
#     ("Cape Town","Addis Ababa"),("Jakarta","Singapore"),("Mexico City","Bogota"),
#     ("Montreal","Toronto"),("Dubai","Doha"),("New York","Miami"),("Tokyo","Osaka"),
#     ("Cairo","Istanbul"),("Berlin","Warsaw"),("Rio de Janeiro","Lima"),
#     ("Buenos Aires","Santiago"),("Melbourne","Sydney"),("Lisbon","Dublin"),
#     ("Helsinki","Stockholm"),("Ho Chi Minh City","Bangkok"),("Casablanca","Nairobi"),
#     ("Vienna","Prague"),("Dallas","Houston"),("Phoenix","San Diego"),
#     ("Vancouver","Seattle"),("Kuala Lumpur","Manila"),("Manila","Taipei"),
#     ("Taipei","Hong Kong"),("Nairobi","Accra"),("Accra","Lagos"),("Addis Ababa","Luanda"),
#     ("Luanda","Cape Town"),("Athens","Rome"),("Oslo","Brussels"),("Stockholm","Helsinki"),
#     ("Zurich","Amsterdam"),("Tel Aviv","Istanbul"),("Tehran","Dubai"),("Moscow","Helsinki"),
#     ("Doha","Abu Dhabi"),("Kuwait City","Dubai"),("Islamabad","New Delhi"),
#     ("Colombo","Mumbai"),("Karachi","Tehran"),("Yerevan","Tbilisi"),("Tbilisi","Baku"),
#     ("Kigali","Nairobi"),("Muscat","Dubai"),("Jeddah","Riyadh"),("Brisbane","Perth"),
#     ("Barcelona","Paris"),("Caracas","Bogota"),("Sao Paulo","Buenos Aires"),
#     ("Nairobi","Addis Ababa"),("Accra","Lagos"),("Luanda","Kinshasa"),
#     ("Wellington","Auckland"),("Perth","Wellington"),("Kigali","Nairobi"),
#     ("Mumbai","New Delhi"),("Lahore","Karachi"),("Nur-Sultan","Almaty"),
#     ("Tashkent","Almaty"),("Ulaanbaatar","Beijing"),("Beijing","Shanghai"),
#     ("Shanghai","Hong Kong"),("Hong Kong","Tokyo"),("Kyoto","Osaka"),
#     ("Tokyo","Seoul"),("Seoul","Beijing"),("Dubai","Singapore"),
#     ("Istanbul","Bangkok"),("Cairo","Dubai"),("Istanbul","Casablanca"),
#     ("Mumbai","Singapore"),("Dubai","Bangkok")
# ]

# # Build graph with distances
# graph = {}
# for city1, city2 in flights:
#     lat1, lon1 = cities[city1]
#     lat2, lon2 = cities[city2]
#     distance = haversine(lat1, lon1, lat2, lon2)
#     graph.setdefault(city1, []).append((city2, distance))
#     graph.setdefault(city2, []).append((city1, distance))  # assuming flights are bidirectional

# # Dijkstra's algorithm
# def dijkstra(start, end):
#     heap = [(0, start, [])]
#     visited = set()
#     while heap:
#         cost, city, path = heapq.heappop(heap)
#         if city in visited:
#             continue
#         visited.add(city)
#         path = path + [city]
#         if city == end:
#             return path
#         for neighbor, dist in graph.get(city, []):
#             if neighbor not in visited:
#                 heapq.heappush(heap, (cost + dist, neighbor, path))
#     return None

# # Find shortest path from Kuwait City to Paris
# path = dijkstra("Kuwait City", "Paris")
# print(",".join(path))


from shapely.geometry import Point, Polygon

# Your pickup points (lat, lon)
pickup_points = [
    (41.3862, 118.2505),
    (56.3003, 21.7064),
    (18.191, 124.1161),
    (27.5906, 81.3611),
    (34.615, 151.8026)
]

# Franchisee regions (ID → list of (lat, lon) boundary cities)
franchisee_regions = {
    1: [(42.8746,74.5698),(51.1655,71.4272),(43.2565,76.9283),(55.7558,37.6176),(35.6892,51.389),(41.2995,69.2401),(40.4093,49.8671)],
    2: [(32.0853,34.7818),(40.4093,49.8671),(35.6892,51.389),(41.0082,28.9784),(40.1872,44.5152),(41.7151,44.8271)],
    3: [(41.9028,12.4964),(37.9838,23.7275),(52.2297,21.0122),(47.4979,19.0402),(48.2082,16.3738)],
    4: [(53.3498,-6.2603),(45.5017,-73.5673),(42.3601,-71.0589),(34.6037,-58.3816),(22.9068,-43.1729),(38.7223,-9.1393)],
    5: [(41.2865,174.7762),(35.6895,139.6917),(33.8688,151.2093),(37.8136,144.9631)],
    6: [(33.589886,-7.603869),(36.737232,3.086472),(8.838333,13.234444),(33.9249,18.4241),(41.3851,2.1734),(41.9028,12.4964),(40.4168,-3.7038)],
    7: [(51.5074,-0.1278),(48.8566,2.3522),(40.4168,-3.7038),(50.8503,4.3517),(52.3676,4.9041)],
    8: [(41.3851,2.1734),(41.9028,12.4964),(48.8566,2.3522),(48.2082,16.3738),(50.8503,4.3517),(47.3769,8.5417)],
    9: [(51.5074,-0.1278),(5.603716,-0.187),(33.589886,-7.603869),(53.3498,-6.2603),(40.4168,-3.7038),(22.9068,-43.1729),(38.7223,-9.1393)],
    10: [(6.2088,106.8456),(1.3521,103.8198),(3.139,101.6869),(10.8231,106.6297)],
    11: [(31.9505,115.8605),(34.6937,135.5023),(39.9042,116.4074),(25.032969,121.565418),(31.2304,121.4737)],
    12: [(25.276987,55.296249),(32.0853,34.7818),(25.276987,51.520008),(24.7136,46.6753),(29.3759,47.9774),(35.6892,51.389),(40.1872,44.5152)],
    13: [(3.139,101.6869),(19.076,72.8777),(13.7563,100.5018),(1.3521,103.8198),(23.8103,90.4125),(6.9271,79.8612)],
    14: [(25.276987,51.520008),(24.453884,54.377343),(23.588,58.3829),(24.7136,46.6753),(29.3759,47.9774),(25.276987,55.296249)],
    15: [(43.2565,76.9283),(24.8607,67.0011),(28.6139,77.209),(31.5204,74.3587)],
    16: [(30.0444,31.2357),(33.9249,18.4241),(41.9028,12.4964),(37.9838,23.7275),(41.0082,28.9784),(8.838333,13.234444)],
    17: [(22.3193,114.1694),(3.139,101.6869),(21.0285,105.8542),(10.8231,106.6297),(13.7563,100.5018)],
    18: [(52.2297,21.0122),(60.1695,24.9354),(59.3293,18.0686),(55.7558,37.6176),(50.0755,14.4378),(59.9139,10.7522),(52.52,13.405)],
    19: [(31.9505,115.8605),(47.8864,106.9057),(39.9042,116.4074),(21.0285,105.8542)],
    20: [(19.432608,-99.133209),(25.7617,-80.1918),(29.7604,-95.3698),(32.7767,-96.797),(33.749,-84.388),(33.4489,-70.6693),(10.4806,-66.9036)],
    21: [(24.453884,54.377343),(23.588,58.3829),(24.7136,46.6753),(6.9271,79.8612),(9.005401,38.763611)],
    22: [(49.2827,-123.1207),(43.65107,-79.347015),(41.8781,-87.6298),(47.6062,-122.3321),(33.4484,-112.074),(32.7767,-96.797),(33.749,-84.388)],
    23: [(40.7128,-74.006),(45.5017,-73.5673),(42.3601,-71.0589),(43.65107,-79.347015)],
    24: [(34.0522,-118.2437),(49.2827,-123.1207),(47.6062,-122.3321),(33.4484,-112.074),(32.7157,-117.1611),(37.7749,-122.4194)],
    25: [(1.286389,36.817223),(1.944072,30.061885),(9.005401,38.763611),(32.0853,34.7818),(21.2854,39.2376),(24.7136,46.6753)],
    26: [(27.4698,153.0251),(35.6895,139.6917),(14.5995,120.9842),(34.6937,135.5023),(33.8688,151.2093),(1.3521,103.8198)],
    27: [(36.8485,174.7633),(1.3521,103.8198),(41.2865,174.7762),(27.4698,153.0251),(33.8688,151.2093)],
    28: [(34.6037,-58.3816),(22.9068,-43.1729),(10.4806,-66.9036),(23.5505,-46.6333)],
    29: [(24.8607,67.0011),(31.5204,74.3587),(33.6844,73.0479),(41.2995,69.2401)],
    30: [(6.5244,3.3792),(5.603716,-0.187),(33.589886,-7.603869),(36.737232,3.086472),(4.441931,15.266293),(8.838333,13.234444)],
    31: [(51.5074,-0.1278),(55.6761,12.5683),(59.3293,18.0686),(59.9139,10.7522),(52.3676,4.9041)],
    32: [(52.52,13.405),(48.2082,16.3738),(50.0755,14.4378),(47.3769,8.5417),(52.3676,4.9041)],
    33: [(25.276987,55.296249),(19.076,72.8777),(23.588,58.3829),(35.6892,51.389),(24.8607,67.0011),(6.9271,79.8612),(41.2995,69.2401)],
    34: [(1.3521,103.8198),(1.286389,36.817223),(6.9271,79.8612),(9.005401,38.763611)],
    35: [(42.8746,74.5698),(43.2565,76.9283),(31.5204,74.3587),(33.6844,73.0479),(41.2995,69.2401)],
    36: [(50.0755,14.4378),(48.2082,16.3738),(52.2297,21.0122)],
    37: [(53.3498,-6.2603),(51.5074,-0.1278),(45.5017,-73.5673),(49.2827,-123.1207),(59.9139,10.7522)],
    38: [(40.7128,-74.006),(42.3601,-71.0589),(34.6037,-58.3816),(33.4489,-70.6693),(10.4806,-66.9036)],
    39: [(6.2088,106.8456),(22.3193,114.1694),(1.3521,103.8198),(14.5995,120.9842),(10.8231,106.6297)],
    40: [(35.02107,135.75385),(35.6895,139.6917),(34.6937,135.5023),(39.9042,116.4074),(31.2304,121.4737),(37.5665,126.978),(37.8136,144.9631)],
    41: [(55.6761,12.5683),(52.52,13.405),(59.3293,18.0686),(52.3676,4.9041)],
    42: [(37.9838,23.7275),(52.2297,21.0122),(47.4979,19.0402),(55.7558,37.6176),(41.0082,28.9784),(40.4093,49.8671),(41.7151,44.8271)],
    43: [(4.711,-74.0721),(1.944072,30.061885),(5.603716,-0.187),(10.4806,-66.9036)],
    44: [(50.8503,4.3517),(47.3769,8.5417),(52.3676,4.9041)],
    45: [(41.2865,174.7762),(51.1655,71.4272),(47.8864,106.9057),(60.1695,24.9354),(55.7558,37.6176),(37.8136,144.9631)],
    46: [(35.02107,135.75385),(35.6895,139.6917),(34.6937,135.5023),(39.9042,116.4074),(31.2304,121.4737),(37.5665,126.978)],
    47: [(29.7604,-95.3698),(19.432608,-99.133209),(32.7767,-96.797),(32.7157,-117.1611),(33.4484,-112.074)],
    48: [(30.0444,31.2357),(21.2854,39.2376),(5.603716,-0.187),(4.441931,15.266293),(1.944072,30.061885),(8.838333,13.234444)],
    49: [(47.8864,106.9057),(43.2565,76.9283),(28.6139,77.209),(19.076,72.8777),(24.8607,67.0011),(23.8103,90.4125),(27.7172,85.324)],
    50: [(31.9505,115.8605),(22.3193,114.1694),(34.6937,135.5023),(14.5995,120.9842),(21.0285,105.8542),(25.032969,121.565418)],
    51: [(30.0444,31.2357),(21.2854,39.2376),(41.0082,28.9784),(32.0853,34.7818)],
    52: [(5.603716,-0.187),(22.9068,-43.1729),(10.4806,-66.9036),(23.5505,-46.6333)],
    53: [(51.1655,71.4272),(47.8864,106.9057),(43.2565,76.9283),(27.7172,85.324)],
    54: [(40.7128,-74.006),(41.8781,-87.6298),(43.65107,-79.347015),(33.749,-84.388)],
    55: [(1.286389,36.817223),(4.711,-74.0721),(1.944072,30.061885)],
    56: [(43.65107,-79.347015),(45.5017,-73.5673),(49.2827,-123.1207)],
    57: [(12.0464,-77.0428),(4.711,-74.0721),(19.432608,-99.133209),(10.4806,-66.9036)],
    58: [(47.6062,-122.3321),(33.4484,-112.074),(34.0522,-118.2437)],
    59: [(5.603716,-0.187),(6.5244,3.3792),(4.441931,15.266293)],
    60: [(12.0464,-77.0428),(25.7617,-80.1918),(19.432608,-99.133209),(10.4806,-66.9036)],
    61: [(47.8864,106.9057),(21.0285,105.8542),(23.8103,90.4125),(13.7563,100.5018)],
    62: [(40.4168,-3.7038),(41.3851,2.1734),(48.8566,2.3522)]
}

# Build polygons
franchisee_polygons = {fid: Polygon(coords) for fid, coords in franchisee_regions.items()}

def find_franchisee(lat, lon):
    pt = Point(lat, lon)
    for fid, poly in franchisee_polygons.items():
        if poly.contains(pt):
            return fid
    return None

results = [find_franchisee(lat, lon) for lat, lon in pickup_points]
print(','.join(str(r) for r in results))
