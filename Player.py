from Hand import Hand


class Player:
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def __str__(self) -> str:
        return self.name
