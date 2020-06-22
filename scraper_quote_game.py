from bs4 import BeautifulSoup
import requests
from csv import DictReader
from random import choice

BASE_URL = "http://quotes.toscrape.com"

def read_quotes(filename):
    with open(filename, "r") as file:
        csv_reader = DictReader(file)
        return list(csv_reader)

def start_game(quotes):
    quote = choice(quotes)
    remaining_guesses = 4
    print("Here's a quote: ")
    print(quote['text'])
    print(quote['author'])
    guess = ""
    while guess.lower() != quote['author'].lower() and remaining_guesses > 0:
        guess = input(f"Who said this quote? Guesses remaining {remaining_guesses} ")
        remaining_guesses -= 1

        if guess.lower() == quote["author"].lower():
            print("You Win!") 
            break

        if remaining_guesses == 3:
            res = requests.get(f"{BASE_URL}{quote['bio-link']}")
            soup = BeautifulSoup(res.text,"html.parser")
            birth_date = soup.find(class_="author-born-date").get_text()
            birth_place = soup.find(class_="author-born-location").get_text()
            print(f"Here's a hint: The author was born on {birth_date} {birth_place}")

        elif remaining_guesses == 2:
            first_initial = quote["author"][0]
            print(f"Here's a hint: Author's first name starts with {first_initial}")

        elif remaining_guesses == 1:
            last_initial = quote["author"].split(" ")[1][0]
            print(f"Here's a hint: Author's first name starts with {last_initial}")

        else:
            print(f"Sorry you ran out of guesses. The author was: {quote['author']}")

    again = ""
    while again not in ('y', 'yes','n','no'):
        again = input("Would you like to pay again (y/n)?")

    if again.lower() in ('yes','y'):
        print("Ok lets go!")
        return start_game(quotes)
    else:
        print("Ok, bye")
    
quotes = read_quotes("quotes.csv")
start_game(quotes)