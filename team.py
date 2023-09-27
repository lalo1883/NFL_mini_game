import random

class Team():
    def __init__(self, name, current_yard, yards_to_score):
        self.name = name
        self.current_yard = current_yard
        self.yards_to_score = yards_to_score

    def show_current_yard(self):
        print('_______________________CURRENT YARDS________________________________')
        self.yards_to_score = 100 - self.current_yard
        print(f'Current yard: {self.current_yard}')
        print(f'Yards to score: {self.yards_to_score}')
        
    def advance_yards(self):
        ranges = [list(range(1, 11)), list(range(10, 25)), list(range(25, 50)), list(range(50, 75)), list(range(75, 100))]
        probabilities = [0.7, 0.1, 0.1, 0.05, 0.05]
        yards_advanced = random.choices(ranges, probabilities)
        yard_advance = random.choice(yards_advanced[0])
        self.current_yard += yard_advance
        print(f'You advanced {yard_advance} yards')

    def retreat_yards(self):
        ranges = [list(range(1, 8)), list(range(9, 14))]
        probabilities = [0.8, 0.3]
        yards_retreated = random.choices(ranges, probabilities)
        yard_retreat = random.choice(yards_retreated[0])
        self.current_yard -= yard_retreat
        print(f'You retreated {yard_retreat} yards')

    def choose_play(self):
        plays = ['Pass', 'Run']
        menu = '''
'_______________________CHOOSE A PLAY________________________________
Press 1) for passing
Press 2) for running
ENTER A PLAY:'''
        play_option = input(menu)
