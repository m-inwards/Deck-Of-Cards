from Deck import Deck
from Hand import Hand
from Player import Player
from System_Messages import print_info
from System_Messages import print_warn
from datetime import datetime


class Game:
    def __init__(self):
        print_info("INITIALIZING GAME")

        # »»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»
        # Generates players array
        # »»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»
        self.players_array = []
        another_player = True

        while another_player:
            current_player_name = ""
            while len(current_player_name) == 0:
                current_player_name = input("Please enter a player name:\n")

            self.players_array.append(Player(current_player_name, Hand()))

            add_another_player_response = ""
            while add_another_player_response.lower() not in ["yes", "no", "y", "n"]:
                add_another_player_response = input("Would you like to add another player? (yes/no)\n")

            if add_another_player_response in ["no", "n"]:
                another_player = False

        self.number_of_players = len(self.players_array)
        self.players_turn_index = 0

        # »»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»
        # Generates standard 52 card deck and shuffles it ready for use
        # »»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»
        self.game_deck = Deck("Go Fish Game Deck")
        self.game_deck.generate_standard_deck()
        self.game_deck.shuffle_deck()

        # »»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»
        # Deals 7 cards into each player's hand
        # »»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»
        for player in self.players_array:
            for loop in range(7):
                pulled_card = self.game_deck.card_array[0]
                self.game_deck.remove_card(pulled_card)
                player.hand.add_card(pulled_card)

        # »»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»
        # Sorts the cards in each player's hand
        # »»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»
        for player in self.players_array:
            player.hand.sort_go_fish_hand()

        print_info("GAME INITIALIZED")

    def next_turn(self):
        # »»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»
        # Increments the player turn index up to the max players and
        # then cycles round the loop of people.
        # »»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»
        self.players_turn_index += 1

        if self.players_turn_index == self.number_of_players:
            self.players_turn_index = 0

    def current_turn_options(self):
        device_passed_response = ""

        while device_passed_response.lower() not in ["yes", "y"]:
            device_passed_response = input(f"Has the device been passed to {self.players_array[self.players_turn_index].name}? (yes/no)\n")

        print("Your current cards are as follows:")
        print("----------------------------------------")
        for card in self.players_array[self.players_turn_index].hand.card_array:
            print(card)
        print("----------------------------------------")

        print("Here are the players you can select:")
        print("----------------------------------------")
        for count in range(self.number_of_players):
            if count != self.players_turn_index:
                print(f"{count}: {self.players_array[count].name}")
        print("----------------------------------------")

        target_player_index = -1
        while target_player_index not in range(self.number_of_players) or target_player_index == self.players_turn_index:
            target_input = input("Please enter the number of the player you would like to ask for cards:\n")
            try:
                target_player_index = int(target_input)
            except ValueError:
                print_warn("That is not a valid integer")
                target_player_index = -1


if __name__ == "__main__":
    test = Game()
    test.current_turn_options()
