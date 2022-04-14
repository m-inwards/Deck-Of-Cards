from Card import Card
from random import shuffle


class Deck:
    def __init__(self, name):
        self.name = name
        self.card_array = []

    # Overrides standard print string
    def __str__(self) -> str:
        return f"This is a deck called \"{self.name}\" and contains {len(self.card_array)} card(s)"

    # Converts the decks array of cards to be a standard 52 card deck
    def generate_standard_deck(self):
        self.card_array = []

        suits = [
            ("SPADES", "BLACK"),
            ("HEARTS", "RED"),
            ("CLUBS", "BLACK"),
            ("DIAMONDS", "RED")
        ]

        values = [
            ("ACE", 1),
            ("2", 2),
            ("3", 3),
            ("4", 4),
            ("5", 5),
            ("6", 6),
            ("7", 7),
            ("8", 8),
            ("9", 9),
            ("10", 10),
            ("JACK", 11),
            ("QUEEN", 12),
            ("KING", 13),
        ]

        for suit, colour in suits:
            for name, value in values:
                self.card_array.append(Card(name, value, suit, colour))

    # Thoroughly shuffles the deck of cards
    def shuffle_deck(self):
        shuffle(self.card_array)
        shuffle(self.card_array)
        shuffle(self.card_array)

    # Adds card to deck
    def add_card(self, card_to_add):
        self.card_array.append(card_to_add)

    # Removes card from deck
    def remove_card(self, card_to_remove):
        self.card_array.remove(card_to_remove)


# Testing
if __name__ == "__main__":
    print("Deck Creation |||||||||||||||||||||||||||||||||||||")
    test_deck = Deck("My Test Deck")
    print(test_deck)

    print("Generate Standard Deck ||||||||||||||||||||||||||||")
    test_deck.generate_standard_deck()
    print(test_deck)
    for card in test_deck.card_array:
        print(card)

    print("Shuffle Standard Deck |||||||||||||||||||||||||||||")
    test_deck.shuffle_deck()
    print(test_deck)
    for card in test_deck.card_array:
        print(card)
