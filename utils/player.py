from utils.card import Card
from typing import List
import random

'''
imported random to shuffle the cards and chose a random card 
'''


"""
Player class:
:name = name of the player
:cards = the cards in player's hand
:turn count= which turn is getting played
:number of cards: how manycards does player have in hand
:history= cards he played
"""


class Player:
    
    cards: List[Card] = []
    turn_count: int = 0
    number_of_cards: int = 13
    history: List[Card] = []

    def __init__(self, name:str):
        self.name = name

    def play(self):
        card = random.choice(self.cards)
        turn = 13 - self.number_of_cards + 1
        self.history.append(card)
        self.cards.remove(card)
        self.number_of_cards -= 1

        print(self.name + " played: " + str(card.value) +
              " of " + str(card.icon) + " / " + str(card.color))
        return card


"""
Deck class:
:cards = all the cards in the deck
:fill_deck() = filling the deck with 52 cards
:shuffle(): shuffling all the cards 
:distrubute(): distrubuting cards to 4 players each 13 splitting the array

"""


class Deck:

    cards = []

    def __init__(self):
        pass

    def fill_deck(self):
        _cards: list[Card] = []
        for i in range(0, 4):
            for j in range(0, 13):
                _cards.append(Card(i, j))

        self.cards = _cards

    def shuffle(self):
        random.shuffle(self.cards)

    def distrubute(self, players: list[Player]):
        i = 0
        for a in players:
            a.cards = self.cards[i::4]
            i += 1
            a.number_of_cards = len(a.cards)
