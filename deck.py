import random

class Card:

    
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return f"{self.value} of {self.suit}"

class Deck:

    def __init__(self, deck):
        suits = ["Hearts","Diamonds","Clubs","Spades"]
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.cards = [Card(value, suit) for suit in suits for value in values]

        # for suit in suits:
        #     for value in values:
        #         self.cards.append(Card(value, suit))

    def __repr__(self):
        return f"Deck of {self.count()} cards"

    def __iter__(self):
        return iter(self.cards)

    def _deal(self, num):
        count = self.count()
        actual = min([count,num])
        if count == 0:
            raise ValueError("all cards have been dealt")
        cards = self.cards[-actual:]
        self.cards = self.cards[:-actual]
        return cards

    def deal_hand(self, hand_size):
        return self._deal(hand_size)

    def deal_card(self):
        return self._deal(1)[0]

    def count(self):
        return f"{len(self.cards)} cards in deck"

    def shuffle(self):
        if self.count() < 52:
            raise ValueError("Only full decks can be shuffled") 
        random.shuffle(self.cards)
        return self