import requests

url = "https://dog.ceo/api/breeds/image/random"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(f"Random Dog Image URL:{data}")
else:
    print("Failed to fetch dog image", response.status_code)
