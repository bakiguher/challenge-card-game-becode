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
        return len(self.players) + " players at turn nr: "+ str(self.turn_count) 

    def start_game(self):
        
        _deck=  Deck()
        _deck.fill_deck()
        _deck.shuffle()
        _deck.distrubute(self.players)
        self.history_cards = a

        for t in range(0, 13):
            print("____________________________")
            print("Turn: " + str(t+1) + " / Cards Left: " +str(len(self.history_cards.cards)))
            
            for k in self.players:
                self.history_cards.cards.remove(k.play())
        


