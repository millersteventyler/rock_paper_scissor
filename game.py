from human import Human
from ai import Ai
from player import Player


class Game:
    def __init__(self):
        self.player_one = Human()
        self.player_two = Human() or Ai()
        self.round = 0

    def choose_player_two(self):
        pass
        single_or_multiplayer = input("Play against computer or friend? friend = 1, computer = 2")
        if single_or_multiplayer == "1":
            self.player_two = Human()
            print("Player 1")
            print(f'Player 1: {self.player_one.set_name()}')
            print("Player 2")
            print(f'Player 2: {self.player_two.set_name()}')
        elif single_or_multiplayer == "2":
            self.player_two = Ai()
            print("Player 1")
            print(f'Player 1: {self.player_one.set_name()}')
            self.player_two.set_name()
            print("Playing against Computer")
        else:
            print("Invalid input, try again!")
            Game.choose_player_two(self)

    def conditions_of_win_or_lose(self):
        while self.player_one.score < 3 and self.player_two.score < 3:
            print("Player one choose!")
            self.player_one.choosing_gesture()
            print("Player two choose!")
            self.player_two.choosing_gesture()
            if self.player_one.chosen_gesture == self.player_two.chosen_gesture:
                print("Draw, no point rewarded.")
                self.round += 1
                Game.conditions_of_win_or_lose(self)
            elif self.player_one.chosen_gesture == Player(self).gestures[0] and self.player_two.chosen_gesture == Player(self).gestures[2]:
                print(f'{self.player_one.name} won a point!')
                self.player_one.score += 1
                self.round += 1
                Game.conditions_of_win_or_lose(self)
            elif self.player_one.chosen_gesture == Player(self).gestures[0] and self.player_two.chosen_gesture == Player(self).gestures[3]:
                print(f'{self.player_one.name} won a point!')
                self.player_one.score += 1
                self.round += 1
            elif self.player_one.chosen_gesture == Player(self).gestures[1] and self.player_two.chosen_gesture == Player(self).gestures[0]:
                print(f'{self.player_one.name} won a point!')
                self.player_one.score += 1
                self.round += 1
                Game.conditions_of_win_or_lose(self)
            elif self.player_one.chosen_gesture == Player(self).gestures[1] and self.player_two.chosen_gesture == Player(self).gestures[4]:
                print(f'{self.player_one.name} won a point!')
                self.player_one.score += 1
                self.round += 1
                Game.conditions_of_win_or_lose(self)
            elif self.player_one.chosen_gesture == Player(self).gestures[2] and self.player_two.chosen_gesture == Player(self).gestures[1]:
                print(f'{self.player_one.name} won a point!')
                self.player_one.score += 1
                self.round += 1
                Game.conditions_of_win_or_lose(self)
            elif self.player_one.chosen_gesture == Player(self).gestures[2] and self.player_two.chosen_gesture == Player(self).gestures[3]:
                print(f'{self.player_one.name} won a point!')
                self.player_one.score += 1
                self.round += 1
                Game.conditions_of_win_or_lose(self)
            elif self.player_one.chosen_gesture == Player(self).gestures[3] and self.player_two.chosen_gesture == Player(self).gestures[4]:
                print(f'{self.player_one.name} won a point!')
                self.player_one.score += 1
                self.round += 1
                Game.conditions_of_win_or_lose(self)
            elif self.player_one.chosen_gesture == Player(self).gestures[3] and self.player_two.chosen_gesture == Player(self).gestures[1]:
                print(f'{self.player_one.name} won a point!')
                self.player_one.score += 1
                self.round += 1
                Game.conditions_of_win_or_lose(self)
            elif self.player_one.chosen_gesture == Player(self).gestures[4] and self.player_two.chosen_gesture == Player(self).gestures[2]:
                print(f'{self.player_one.name} won a point!')
                self.player_one.score += 1
                self.round += 1
                Game.conditions_of_win_or_lose(self)
            elif self.player_one.chosen_gesture == Player(self).gestures[4] and self.player_two.chosen_gesture == Player(self).gestures[0]:
                print(f'{self.player_one.name} won a point!')
                self.player_one.score += 1
                self.round += 1
                Game.conditions_of_win_or_lose(self)
            else:
                print(f'{self.player_two.name} won a point')
                self.player_two.score += 1
                self.round += 1
                Game.conditions_of_win_or_lose(self)

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
        Game.choose_player_two(self)
        # Make sure both player objects exist and input name is necessary
        # Game Rounds - Loop? What determines when the loop will stop?
        Game.conditions_of_win_or_lose(self)
        # Player one chooses gesture
        # Player two chooses gesture

        # Compare gestures, assign point to winner, display winner of round

        # End game

        # Display overall winner of game

        # Play again?



