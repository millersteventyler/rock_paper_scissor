class Player:
    def __init__(self, name):
        self.name = name
        self.gestures = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
        self.score = 0
        self.chosen_gesture = 0

    def set_name(self):
        self.name = input("What is your name?")
        return self.name

    def choosing_gesture(self):
        user_input = input("Pick a gesture, ( Rock = 0, Paper = 1, Scissors = 2, Lizard = 3, Spock = 4 )")
        if user_input == "0":
            user_input = self.gestures[0]
            print(f'{self.name} used Rock')
        elif user_input == "1":
            user_input = self.gestures[1]
            print(f'{self.name} used Paper')
        elif user_input == "2":
            user_input = self.gestures[2]
            print(f'{self.name} used Scissors')
        elif user_input == "3":
            user_input = self.gestures[3]
            print(f'{self.name} used Lizard')
        elif user_input == "4":
            user_input = self.gestures[4]
            print(f'{self.name} used Spock')
        else:
            print("Input invalid try again.")
            Player.choosing_gesture(self)
        self.chosen_gesture = user_input
        return self.chosen_gesture
