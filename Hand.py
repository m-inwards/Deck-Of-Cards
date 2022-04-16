from Card import Card


class Hand:
    def __init__(self, owner):
        self.owner = owner
        self.card_array = []

    def __str__(self) -> str:
        return f"This hand belongs to {self.owner} and contains {len(self.card_array)} card(s)"

    # Adds card to hand
    def add_card(self, card_to_add):
        self.card_array.append(card_to_add)

    # Removes card from hand
    def remove_card(self, card_to_remove):
        self.card_array.remove(card_to_remove)

    # Sorts hand of cards
    def sort_standard_hand(self):
        self.card_array.sort(key=lambda card: card.value)
        self.card_array.sort(key=lambda card: card.suit)

    def sort_go_fish_hand(self):
        self.card_array.sort(key=lambda card: card.suit)
        self.card_array.sort(key=lambda card: card.value)


# Testing
if __name__ == "__main__":
    test_hand = Hand("Matt")

    test_card_1 = Card("ACE", 1, "SPADES", "BLACK")
    test_card_2 = Card("3", 3, "HEARTS", "BLACK")
    test_card_3 = Card("KING", 13, "DIAMONDS", "BLACK")
    test_card_4 = Card("2", 2, "HEARTS", "BLACK")
    test_card_5 = Card("5", 5, "CLUBS", "BLACK")
    test_card_6 = Card("4", 4, "SPADES", "BLACK")

    test_hand.add_card(test_card_1)
    test_hand.add_card(test_card_2)
    test_hand.add_card(test_card_3)
    test_hand.add_card(test_card_4)
    test_hand.add_card(test_card_5)
    test_hand.add_card(test_card_6)

    print("Cards before sorting:")
    for card in test_hand.card_array:
        print(card)

    test_hand.sort_standard_hand()

    print("Cards after sorting:")
    for card in test_hand.card_array:
        print(card)
