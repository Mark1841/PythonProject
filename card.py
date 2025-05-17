class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    @property
    def rank(self):
        return self._rank

    @rank.setter
    def rank(self, rank):
        if rank in ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']:
            self._rank = rank
        else:
            print(f"{rank} is not a valid rank. Please choose from {['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']}.")

    @property
    def suit(self):
        return self._suit

    @suit.setter
    def suit(self, suit):
        if suit in ['Hearts', 'Diamonds', 'Clubs', 'Spades']:
            self._suit = suit
        else:
            print(f"{suit} is not a valid suit. Please choose from {['hearts', 'diamonds', 'clubs', 'spades']}.")

    def __repr__(self):
        return f'{self.rank} of {self.suit}'