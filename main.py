from deck import Deck
from player import Player
from dealer import Dealer

"""
Blackjack rules:

Dealer and player given two cards each
Player can request another card or stay as is, with the goal being to get as close to
21 as possible but not over 21, in which case you go bust and lose
Once player has competed their turn, the dealer draws cards until they are at least
at 17, but not over 21, at which time they stop
Player with the highest value hand wins
Picture cards count as 10, Ace can be 1 or 11, all other cards are face value
"""


if __name__ == '__main__':
    deck = Deck()
    deck.shuffle()

    def check_winner():
        if player_one.hand.value > dealer.hand.value and not player_one.bust or dealer.bust:
            return player_one.name
        else:
            return dealer.name

    player_one = Player("Mark")
    dealer = Dealer()

    # Deal the initial two cards
    for deal in range (2):
        player_one.hand.add_card(deck.deal())
        dealer.hand.add_card(deck.deal())

    # Player and Dealer take turns
    player_one.take_turn(deck)
    if player_one.bust:
        print(f'{player_one.name}, sorry you went bust!!')
    else:
        dealer.take_turn(deck)

    #Display Winner
    print(f'Winner:  {check_winner()}')
    print(f'Your hand: {player_one.hand}, your hand value: {player_one.hand.value}')
    print(f'Computer hand: {dealer.hand}, computer hand value: {dealer.hand.value}')