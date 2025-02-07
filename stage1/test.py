import requests

url = "http://127.0.0.1:5000/api/classify-number?number=371"

response = requests.get(url)
print(response.text)