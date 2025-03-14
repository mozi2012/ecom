import random

def monty_hall_simulation(num_trials=10000, switch=True):
    wins = 0
    for _ in range(num_trials):
        car_door = random.randint(0, 2)
        contestant_choice = random.randint(0, 2)
        remaining_doors = [door for door in range(3) if door != contestant_choice and door != car_door]
        monty_opens = random.choice(remaining_doors)
        if switch:
            new_choice = [door for door in range(3) if door != contestant_choice and door != monty_opens][0]
            contestant_choice = new_choice
        if contestant_choice == car_door:
            wins += 1
    return wins / num_trials
num_trials = 10000
win_rate_switch = monty_hall_simulation(num_trials, switch=True)
win_rate_stay = monty_hall_simulation(num_trials, switch=False)

win_rate_switch, win_rate_stay