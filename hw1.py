import os
import requests
from dotenv import load_dotenv
from fake_useragent import UserAgent
from pprint import pprint


ua = UserAgent()   #something like browser
category = input("Input any kind of place  (Park, Zoos, Museums, etc) : ")
url = "https://api.foursquare.com/v3/places/search"
params = {
    'limit': 50,
    'query': category,
    'fields': 'name,location,rating'
}
headers = {
    "User-Agent": ua.firefox,
    "Accept": "application/json",
    "Authorization": "fsq3P6zWw5hrHAp69JoTu+0TFeYEBCEXDIo7+Ivypcz/4Uo="
}
response = requests.request("GET", url, params=params, headers=headers)
if response.status_code == 200:
    print("Successful request API with URL: ", response.url)
else:
    print("Not successful,  API code:", response.status_code)

data = response.json()
establishments = []
for place in data['results']:
    place_name = place.get('name')
    place_address = place.get('location')['formatted_address']
    place_rating = place.get('rating') if 'rating' in place else "no rating"
    establishments.append({'name': place_name, 'address': place_address, 'rating': place_rating})
for establishment in establishments:
        print(f"Place: {establishment['name']}")
        print(f"Address: {establishment['address']}")
        print(f"Rating: {establishment['rating']}")
        print()