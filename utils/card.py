class Symbol:
    """
    Symbol class
    :color Red or Black
    :icon ["♡", "♢", "♣","♠"]
    """

    color: str = ""

    def __init__(self, item: int):
        self.color = ""
        icons = ["♡", "♢", "♣", "♠"]
        self.icon = icons[item]

        if item < 2:
            self.color = "red"
        else:
            self.color = "black"

    def __str__(self):
        return f"{self.color}{self.icon}"


class Card(Symbol):

    """
    Card class, a card with icon and number
    :inherits Symbol
    :value=  ["A", "2", "3", "4", "5", "6", "7","8", "9", "10", "J", "Q", "K"]
    """

    def __init__(self, icon, item: int):

        values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        points = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        super().__init__(icon)
        self.value = values[item]
        self.point = points[item]

    def __str__(self):
        return f"{super().icons[self.icon]}{self.values[self.item]}"
