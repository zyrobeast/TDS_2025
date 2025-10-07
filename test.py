import requests
import pandas as pd

response = requests.post('https://tds-2025-seven.vercel.app/',
                         json={
                             'regions': ["emea", "apac"],
                             'threshold_ms': 180
                         }
                         )

print(response.json())

print(requests.get('https://tds-2025-seven.vercel.app/api?class=9E').json())
df = pd.read_csv('q-fastapi.csv')
print({'students': df.to_dict(orient='records')})
