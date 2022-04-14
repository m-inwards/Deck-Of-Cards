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


# Testing
if __name__ == "__main__":
    print("placeholder")
