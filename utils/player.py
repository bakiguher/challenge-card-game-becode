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
    number_of_cards: int = 13
    history: List[Card] = []

    def __init__(self, name):
        self.name = name

    def play(self):
        # TODO
        card = random.choice(self.cards)
        turn = 13- self.number_of_cards + 1
        self.history.append(card)
        self.cards.remove(card)
        self.number_of_cards -= 1
        
        print(self.name + " played " + str(card.value) + " of "+ str(card.icon))

        # for k in self.cards:
        #     print(k.value+k.icon)

        # randomly pick a Card in cards.
        # Add the Card to the Player's history.
        # Print: {PLAYER_NAME} {TURN_COUNT} played: {CARD_NUMBER} {CARD_SYMBOL_ICON}.
        # Return the Card.
        


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
        i = 0
        for a in players:
            a.cards = self.cards[i::4]
            i += 1
            a.number_of_cards = len(a.cards)

        # for a in players:
        #     for j in a.cards:
        #         print(j.icon+   j.value)

        # pass






# p1.play()
# p2.play()

# print(a.cards)
# for k in _players:
#     print(k.number_of_cards)
#     for e in k.cards:
#         print(e.icon + e.value)
