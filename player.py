from hand import Hand


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = Hand()
        self.bust = False

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name.upper()

    def take_turn(self, my_deck):
        turn_over = False

        while not turn_over:
            print(f'Your hand: {self.hand}')
            print(f'({self.name}, do you want to pick a card (1) or stick (2)?')
            option = input()

            if option == '1':
                self.hand.add_card(my_deck.deal())
                if self.hand.value > 21:
                    turn_over = True
                    self.bust = True
            else:
                turn_over = True

