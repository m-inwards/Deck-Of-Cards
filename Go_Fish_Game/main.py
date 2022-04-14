import sys

# Used to import from parent directory
sys.path.append('../Deck-Of-Cards')
from Card import Card
from Deck import Deck
from Hand import Hand


if __name__ == "__main__":
    test_card = Card("ACE", 1, "SPADES", "BLACK")
    print(test_card)
