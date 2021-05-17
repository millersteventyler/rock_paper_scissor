from human import Human
from ai import Ai


class Game:
    def __init__(self):
        self.player_one = Human()
        self.player_two = Human() or Ai()

    def choose_player_two(self):
        pass
        # Prompt user to choose single player or multiplayer
        # set self.player_two to a Human() or Ai() depending on input

    def run_game(self):
        pass
        # intro
        # Welcome / Rules
        # Select Single or Multiplayer
        # Make sure both player objects exist and input name is necessary
        # Game Rounds - Loop? What determines when the loop will stop?
        # Player one chooses gesture
        # Player two chooses gesture
        # Compare gestures, assign point to winner, display winner of round
        # End game
        # Display overall winner of game
        # Play again?
