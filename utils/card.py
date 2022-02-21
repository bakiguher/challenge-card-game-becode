
class Symbol:
    color: str = ""  #Why do we need color????
    def __init__(self, color: str, item: int):
        self.color = color
        icons = ["♠", "♡", "♢", "♣"]
        self.icon = icons[item]

    def __str__(self):
        return f"{self.color} {self.icon}"

class Card(Symbol):
    def __init__(self, color:str, icon, item: int):

        values = ["A", "2", "3", "4", "5", "6", "7",
                  "8", "9", "10", "J", "Q", "K"]

        super().__init__(color, icon)
        self.value = values[item]

    def __str__(self):
        return (super().icons[self.icon] + self.values[self.item])

