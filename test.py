import requests

response = requests.post('http://127.0.0.1:8000/',
                         json={
    'regions': ["emea","apac"],
    'threshold_ms': 180
}
                         )

print(response.json())