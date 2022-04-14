from Card import Card
from random import shuffle


class Deck:
    def __init__(self, name):
        self.name = name
        self.card_array = []

    def __str__(self) -> str:
        return f"This is a deck called \"{self.name}\" and contains {len(self.card_array)} card(s)"

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

    def shuffle_deck(self):
        shuffle(self.card_array)
        shuffle(self.card_array)
        shuffle(self.card_array)


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
