class Card:
    def __init__(self, name, value, suit, colour):
        self.name = name
        self.value = value
        self.suit = suit
        self.colour = colour

    # Overrides standard print string
    def __str__(self) -> str:
        return f"{self.name} of {self.suit}"


# Testing
if __name__ == "__main__":
    test_card = Card("ACE", 1, "SPADES", "BLACK")
    print(test_card)
