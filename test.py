import requests

# Replace "webdesigning" with your desired search topic
topic = "webdesigning"
url = f"https://api.stackexchange.com/2.3/search?order=desc&sort=votes&intitle={topic}&site=stackoverflow"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    for item in data["items"]:
        print(item["title"])
else:
    print(f"Error: {response.status_code}")
