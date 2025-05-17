from hand import Hand

class Dealer:
    def __init__(self):
        self.name = 'DEALER'
        self.hand = Hand()
        self.bust = False


    def take_turn(self, my_deck):
        turn_over = False

        while not turn_over:
            if self.hand.value <17:
                self.hand.add_card(my_deck.deal())
            else:
                turn_over = True

            if self.hand.value > 21:
                self.bust = True