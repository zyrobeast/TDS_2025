import requests

response = requests.post('https://tds-2025-seven.vercel.app/',
                         json={
    'regions': ["emea","apac"],
    'threshold_ms': 180
}
                         )

print(response.json())