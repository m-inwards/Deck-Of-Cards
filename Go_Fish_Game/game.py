from Deck import Deck
from Hand import Hand
from datetime import datetime


class Game:
    def __init__(self):

        print(f"\033[0;36;1m[{datetime.now().strftime('%H:%M:%S')} INFO]: INITIALIZING GAME\033[0;0m")

        # »»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»
        # Generates players array
        # »»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»
        self.players_array = []
        another_player = True

        while another_player:
            current_player_name = ""
            while len(current_player_name) == 0:
                current_player_name = input("Please enter a player name:\n")

            self.players_array.append((current_player_name, Hand(current_player_name)))

            add_another_player_response = ""
            while add_another_player_response.lower() not in ["yes", "no", "y", "n"]:
                add_another_player_response = input("Would you like to add another player? (yes/no)")

            if add_another_player_response in ["no", "n"]:
                another_player = False

        # »»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»
        # Generates standard 52 card deck and shuffles it ready for use
        # »»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»
        self.game_deck = Deck("Go Fish Game Deck")
        self.game_deck.generate_standard_deck()
        self.game_deck.shuffle_deck()

        print(f"\033[0;36;1m[{datetime.now().strftime('%H:%M:%S')} INFO]: GAME INITIALIZED\033[0;0m")


if __name__ == "__main__":
    new_game = Game()
