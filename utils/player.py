from card import Card
from typing import List
import random
# n player.py create a class Player that contains these attributes:

# cards which is a list of Card. (you will need to import Card from card.py). In a real card game, this is equivalent to the cards that the player has in his hands.
# turn_count which is an int starting a 0.
# number_of_cards which is an int starting at 0.
# history which is a list of Card that will contain all the cards played by the player.

# play() that will:


class Player:
    name = ""
    cards: List[Card] = []
    turn_count: int = 0
    number_of_cards: int = 0
    history: List[Card] = []

    def __init__(self, name):
        self.name = name

    def play():
        # TODO
        # randomly pick a Card in cards.
        # Add the Card to the Player's history.
        # Print: {PLAYER_NAME} {TURN_COUNT} played: {CARD_NUMBER} {CARD_SYMBOL_ICON}.
        # Return the Card.
        pass


# Create a Deck class that contains:

# An attribute cards which is going to contain a list of instances of Card.
# A fill_deck() method that will fill cards with a complete card game (an instance of 'A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K' for each possible symbol [♥, ♦, ♣, ♠]). Your deck should contain 52 cards at the end.
# A shuffle() method that will shuffle all the list of cards.
# A distribute() that will take a list of Player as parameter and will distribute the cards evenly between all the players.

class Deck:

    cards = []

    def __init__(self):
        pass

    def fill_deck(self):
        _cards: list[Card] = []
        for i in range(0, 4):
            for j in range(0, 13):
                _cards.append(Card("red", i, j))

        self.cards = _cards

    def shuffle(self):
        random.shuffle(self.cards)

    def distrubute(self, players: list[Player]):
        for a in players:
            i = 0
            a.cards = self.cards[i::4]
            i += 1

        # return (deck[0::4], deck[1::4], deck[2::4], deck[3::4])
        pass


p1 = Player("Azra")
p2 = Player("Baki")
p3 = Player("Chrysanti")
p4 = Player("Destan")


_players = [p1, p2, p3, p4]


a = Deck()
a.fill_deck()
a.shuffle()
a.distrubute(_players)


# print(a.cards)
for k in _players:
    print("########")
    for e in k.cards:
        print(e.icon + e.value)
