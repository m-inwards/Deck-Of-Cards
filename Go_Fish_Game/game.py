import sys

# Used to import from parent directory
sys.path.append('../Deck-Of-Cards')
from Card import Card
from Deck import Deck
from Hand import Hand


class Game:
    def __init__(self, players_array):
        self.players_array = players_array


if __name__ == "__main__":
    test_card = Card("ACE", 1, "SPADES", "BLACK")
    print(test_card)