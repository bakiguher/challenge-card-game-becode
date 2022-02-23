class Symbol:
    """
    Symbol class
    :color Red or Black
    :icon ["♡", "♢", "♣","♠"]
    """

    color: str = ""  # Why do we need color????

    def __init__(self, item: int):
        self.color = ""
        icons = ["♡", "♢", "♣", "♠"]
        self.icon = icons[item]

        if item < 2:
            self.color = "red"
        else:
            self.color = "black"

    def __str__(self):
        return f"{self.color} {self.icon}"


class Card(Symbol):

    """
    Card class
    :inherits Symbol
    :value=  ["A", "2", "3", "4", "5", "6", "7","8", "9", "10", "J", "Q", "K"]
    """

    def __init__(self, icon, item: int):

        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

        super().__init__(icon)
        self.value = values[item]

    def __str__(self):
        return super().icons[self.icon] + self.values[self.item]
