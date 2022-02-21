from enum import Enum
from xml.etree.ElementTree import tostring

# class Icon(Enum):
#     Clubs = '♣'
#     Diamonds = '♦'
#     Hearths = '♥'
#     Spades = '♠'

# symbol = "♠ ♡ ♢ ♣".split()
# ranks = "2 3 4 5 6 7 8 9 10 J Q K A".split()


class Symbol:
    color: str = ""
    icon = ""

    def __init__(self, color: str, item: int):
        self.color = color
        icons = ["♠", "♡", "♢", "♣"]
        self.icon = icons[item]

    def __str__(self):
        return f"{self.color} {self.icon}"


class Card(Symbol):
    value = ""

    def __init__(self, color, icon, item: int):

        values = ["Ace", "2", "3", "4", "5", "6", "7",
                  "8", "9", "10", "Jack", "Queen", "King"]

        super().__init__(color, icon)
        self.value = values[item]

    def __str__(self):
        return (super().icons[self.icon] + self.values[self.item])



b=Symbol("blue",2)
print (b)
# a = Card("red", 0, 4)
# print(a.value)
# a = Card("blue", 0, 9)
# print(a)
# # class Deck:


#a = Card("green")
