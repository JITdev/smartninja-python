import json
from pprint import pprint
from urllib.request import urlopen

# with open("people.json") as file:
#     data = json.load(file)
#     # print each individual user (all data)
#     for user in data:
#         print(user)
#
#     # print each individual user (first name and last name)
#     for user in data:
#         print(user["first_name"] + " " + user["last_name"])

api_key = "b6907d289e10d714a6e88b30761fae22"  # insert your own API key!!!

response = urlopen('https://samples.openweathermap.org/data/2.5/weather?q=London,uk&appid=' + api_key).read()

data = json.loads(response)
main = data['main']
pprint(f"{data['name']} {main['temp']}")