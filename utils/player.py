"""
import random to shuffle the cards and chose a random card 
"""

from utils.card import Card
from typing import List
import random
import sys


class Player:
    """
    Player class:
    :name = name of the player
    :cards = the cards in player's hand
    :turn count= which turn is getting played
    :number of cards: how manycards does player have in hand
    :history= cards he played
    """

    cards: List[Card] = []
    turn_count: int = 0
    number_of_cards: int = 13
    history: List[Card] = []
    points = 0

    def __init__(self, name: str):
        self.name = name

    def stop_game(self, x):
        """
        Function to stop the game in case of q entered as input
        """
        if x == "q":
            sys.exit(0)

    def get_input(self):
        """
        This function gets an integer input to select a card shown on the screen, or player can select "q" to quit game, if a number more than
        the cards avaliable game selects a random card
        """
        while True:
            num = input("Card nr: ")
            self.stop_game(num)
            try:
                val = int(num)
                return val
                break
            except ValueError:
                print("It is not a valid selection, Choose a card or q to quit.")

    def play(self):
        """
        Function to play a card. It is asked player to choose a card from given cards. It checks if selection
        is valid Played cards removed from cards and added to history
        also keeping turn number for future reference.
        """

        i = 0
        print(self.name, ", please choose a card  :  ")
        for a in self.cards:
            print(str(i), ":", a.icon, a.value, " ", end=" ")
            i += 1

        _selected_card_index = self.get_input()  # input("Choose a card ")

        if _selected_card_index < i and _selected_card_index >= 0:
            card = self.cards[int(_selected_card_index)]

        else:
            print("Dont cheat, a card is randomly selected for you")
            card = random.choice(self.cards)

        self.turn_count = 13 - self.number_of_cards + 1
        self.history.append(card)
        self.cards.remove(card)
        self.number_of_cards -= 1

        print(
            self.name, " played: ", str(card.icon), str(card.value)
        )  # + " / " + str(card.color) +" / " + str(card.point)
        return card


class Deck:
    """
    Deck class:
    :cards = all the cards in the deck
    :fill_deck() = filling the deck with 52 cards
    :shuffle(): shuffling all the cards
    :distrubute(): distrubuting cards to 4 players each 13 splitting the array

    """

    cards = []

    def __init__(self):
        pass

    def fill_deck(self):
        """
        Function that fills the deck with 52 cards .
        """
        _cards: list[Card] = []
        for i in range(0, 4):
            for j in range(0, 13):
                _cards.append(Card(i, j))

        self.cards = _cards

    def shuffle(self):
        """function to shuffle the cards"""
        random.shuffle(self.cards)

    def distrubute(self, players: list[Player]):
        """
        Function that will perform the distrubution operation of the card to players(in params).
        :players: list of Player

        """
        i = 0
        for a in players:
            a.cards = self.cards[i::4]
            i += 1
            a.number_of_cards = len(a.cards)
