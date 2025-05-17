import random

from card import Card

class Deck:
    def __init__(self):
        self.cards = []

    def build(self):
        suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
        ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(rank, suit))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop(0)


