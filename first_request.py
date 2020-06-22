import requests
url = "https://www.google.com"
response = requests.get(url)

print(f"your request to {url} gave the response code {response.status_code}")