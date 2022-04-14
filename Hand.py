from Card import Card


class Hand:
    def __init__(self, owner):
        self.owner = owner
        self.card_array = []

    def __str__(self) -> str:
        return f"This hand belongs to {self.owner} and contains {len(self.card_array)} card(s)"


if __name__ == "__main__":
    print("placeholder")
