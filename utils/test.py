from typing import List, Dict, Tuple

# import random from somewhere
import random


suits = "♠ ♡ ♢ ♣".split()
ranks = "2 3 4 5 6 7 8 9 10 J Q K A".split()

Players: List[str] = ["Player1", "Player2", "PLayer3", "Player4"]

#Card: Tuple[str, str] = []

#Deck: List[Tuple[str, str]] = [(s, r) for r in ranks for s in suits]


# print(Deck)
# random.shuffle(Deck)


print("------------------------------------")
# print(Deck)


def deal_hands(deck):   #: List[Tuple[str, str]]
    """Deal the cards in the deck into four hands"""
    print((deck[0::4], deck[1::4], deck[2::4], deck[3::4]))
    return (deck[0::4], deck[1::4], deck[2::4], deck[3::4])


def shufle_deck(Players: List[str]):
    Deck: List[Tuple[str, str]] = [(s, r) for r in ranks for s in suits]
    # print(Deck)
    random.shuffle(Deck)
    hands = zip(Players, deal_hands(Deck))
    # print(hands)
    x = dict(hands)
    return x


a=[1,2,3,4,5,6,7,8,9,10,11,12]
deal_hands(a)

# d = shufle_deck(Players)
# items = d.items()

# for a in items:
#     print(a)
