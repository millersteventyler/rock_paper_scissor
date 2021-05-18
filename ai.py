import random
from player import Player


class Ai(Player):
    def __init__(self):
        super(Ai, self).__init__('')

    def set_name(self):
        self.name = "Computer"
        return self.name

    def choosing_gesture(self):
        user_input = random.randint(0, len(self.gestures) - 1)
        if user_input == 0:
            user_input = self.gestures[0]
            print(f'{self.name} used Rock')
        elif user_input == 1:
            user_input = self.gestures[1]
            print(f'{self.name} used Paper')
        elif user_input == 2:
            user_input = self.gestures[2]
            print(f'{self.name} used Scissors')
        elif user_input == 3:
            user_input = self.gestures[3]
            print(f'{self.name} used Lizard')
        elif user_input == 4:
            user_input = self.gestures[4]
            print(f'{self.name} used Spock')
        self.chosen_gesture = user_input
        return self.chosen_gesture
