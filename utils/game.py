from utils.card import Card
from utils.player import Player, Deck


class Board:
    """
    Board class, where the game is played. 
    :players All the players 
    :turn_count 
    :active_cards Cards in the last hand
    :history_cards The cards played in previous hands 
    """
    players: list[Player] = []
    turn_count: int = 0
    active_cards: list[Card] = []
    history_cards: list[Card] = []

    def __init__(self, players: list[Player]):
        self.players = players

    def __str__(self):
        return len(self.players) + " players at turn nr: " + str(self.turn_count)

    def start_game(self):
        """
        Function that will start the game
        Creates a Deck, fills, shuffles and distributes the deck
        Writes the turn number and remaining cards amount of the game
        for each player plays the game and removes the played cards from card history.

        """

        _deck = Deck()
        _deck.fill_deck()
        _deck.shuffle()
        _deck.distrubute(self.players)
        self.history_cards = _deck

        for t in range(0, 13):
            print("____________________________")
            print(
                "Turn: "
                + str(t + 1)
                + " / Cards Left: "
                + str(len(self.history_cards.cards))
            )

            for k in self.players:
                _k=k.play()
                self.history_cards.cards.remove(_k)
                self.active_cards.append(_k)
