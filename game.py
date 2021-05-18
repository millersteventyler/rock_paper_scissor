from human import Human
from ai import Ai


class Game:
    def __init__(self):
        self.player_one = Human()
        self.player_two = Human() or Ai()

    def choose_player_two(self):
        pass
        single_or_multiplayer = input("Play against computer or friend? friend = 1, computer = 2")
        if single_or_multiplayer == "1":
            self.player_two = Human()
            print("Playing against friend")
        elif single_or_multiplayer == "2":
            self.player_two = Ai()
            print("Playing against computer")

    def run_game(self):
        # intro
        print("Welcome to Rock Paper Scissors Lizard!")
        # Rules
        print("Rules: The game is best of three.")
        print("Select a gesture using keys ( 0, 1, 2, 3, 4 )")
        print("Rock crushes Scissors")
        print("Scissors cuts Paper")
        print("Paper covers Rock")
        print("Rock crushes Lizard")
        print("Lizard poisons Spock")
        print("Spock smashes Scissors")
        print("Scissors decapitates Lizard")
        print("Lizard eats Paper")
        print("Paper disproves Spock")
        print("Spock vaporizes Rock")
        # Select Single or Multiplayer
        # Make sure both player objects exist and input name is necessary
        # Game Rounds - Loop? What determines when the loop will stop?
        # Player one chooses gesture
        # Player two chooses gesture
        # Compare gestures, assign point to winner, display winner of round
        # End game
        # Display overall winner of game
        # Play again?
