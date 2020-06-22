import requests
from random import choice

url = "https://icanhazdadjoke.com/search"

subject = input("What would you like to hear a joke about? ")


response = requests.get(
    url,
    headers={"Accept":"application/json"},
    params={"term": subject}
)

data = response.json()

# print(data['results'][0]['joke'])
if len(data['results']) > 1:
    joke = choice(data['results'])

    print(f"I have {len(data)} jokes, here is one:")
    print(joke['joke'])
else:
    print("I don't have any jokes on that")