from team import Team
import random

def create_team():
    print('Create your team!')
    yard_ranges = [list(range(15, 25)), list(range(26, 35)), list(range(36, 55)), list(range(56, 75)), list(range(75, 100))]
    yard_probabilities = [0.7, 0.1, 0.1, 0.05, 0.05]
    random_yards = random.choices(yard_ranges, yard_probabilities)
    current_yard = random.choice(random_yards[0])  # Select a random value from the list
    yards_to_score = 100 - current_yard
    name = input('Enter the team name: ')
    team = Team(name, current_yard, yards_to_score)
    return team

def play():
    # print('Let's play')
    team1 = create_team()
    team1.show_current_yard()
    while team1.current_yard < 100:
        team1.choose_play()
        advance_or_retreat = random.random() <= 0.93  # 70% probability of True, 30% probability of False
        if advance_or_retreat:
            team1.advance_yards()
            team1.show_current_yard()
            if team1.current_yard >= 100:
                print('Touchdown!!')
                break
        else:
            team1.retreat_yards()
            team1.show_current_yard()

play()
