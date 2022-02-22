from utils.card import Card
from utils.player import Player, Deck


class Board:
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
            print()
            print("____________________________")
            print(
                "Turn: "
                + str(t + 1)
                + " / Cards Left: "
                + str(len(self.history_cards.cards))
            )

            turnpoints = []
            for k in self.players:
                a = k.play()
                turnpoints.append(a.point)

                self.history_cards.cards.remove(a)
            max_value = max(turnpoints)
            max_index = turnpoints.index(max_value)
            self.players[max_index].points += 1
            print("Turn points ")

            for _z in self.players:
                print(_z.name + " :  " + str(_z.points))

        print("XXXXXXXXXXXX GAME OVER XXXXXXXXXXXXXX")
        print("Points :  ")
        _winner = {}
        for _t in self.players:
            print(_t.name + " :  " + str(_t.points))
            _winner[_t.name] = _t.points

        # ordering winner dictionary
        _q = {
            k: v
            for k, v in sorted(_winner.items(), key=lambda item: item[1], reverse=True)
        }
        print("WINNER IS :")
        _first_pair = next(iter((_q.items())))
        print(_first_pair[0])
