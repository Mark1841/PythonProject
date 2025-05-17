class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value = self.get_card_value()

    def __repr__(self):
        return str(self.cards)

    def get_card_value(self):
        total = 0
        for card in self.cards:
            if card.rank in ['J', 'Q', 'K']:
                total += 10
            elif card.rank in ['2', '3', '4', '5', '6', '7', '8', '9', '10']:
                total += int(card.rank)
            elif card.rank == 'A':
                if total < 10:
                    total += 11
                else:
                    total += 1
        return total


