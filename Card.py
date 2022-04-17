class Card:
    def __init__(self, name, value, suit, colour):
        self.name = name
        self.value = value
        self.suit = suit
        self.colour = colour

    # Overrides standard print string
    def __str__(self) -> str:
        suit_ascii = ""

        match self.suit:
            case "SPADES":
                suit_ascii = "♤"
            case "HEARTS":
                suit_ascii = "♡"
            case "CLUBS":
                suit_ascii = "♧"
            case "DIAMONDS":
                suit_ascii = "♢"

        return f"{self.name}{suit_ascii} ({self.name} of {self.suit})"


# Testing
if __name__ == "__main__":
    test_card = Card("ACE", 1, "SPADES", "BLACK")
    print(test_card)
