from deck import Deck
from player import Player

if __name__ == '__main__':
    my_deck = Deck()
    my_deck.build()

    my_deck.shuffle()


    player_one = Player("Mark")
    computer = Player("Computer")

    for deal in range (2):
        player_one.hand.add_card(my_deck.deal())
        computer.hand.add_card(my_deck.deal())

    # Player turn
    bust = player_one.take_turn(my_deck)

    if bust:
        print(f'{player_one.name}, sorry you went bust!!')
    else:
        bust = computer.ai_turn(my_deck, player_one)
        if bust:
            print(f'{player_one.name}, Congratulations! you won, the computer went bust!!')
        else:
            if player_one.hand.value > computer.hand.value:
                print(f'{player_one.name}, congratulations you won!!')
            else:
                print(f'{player_one.name}, sorry, you lost!!')


    print(f'Your hand: {player_one.hand}, your hand value: {player_one.hand.value}')
    print(f'Computer hand: {computer.hand}, computer hand value: {computer.hand.value}')


