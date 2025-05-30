from hand import Hand

class Dealer:
    def __init__(self):
        self.name = 'DEALER'
        self.hand = Hand()
        self.bust = False

    def take_turn(self, deck):

        while self.hand.value <17:
            self.hand.add_card(deck.deal())

        if self.hand.value > 21:
            self.bust = True