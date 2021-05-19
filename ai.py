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
        self.chosen_gesture = self.gestures[user_input]
        print(f'{self.name} used {self.chosen_gesture}')
        return self.chosen_gesture
