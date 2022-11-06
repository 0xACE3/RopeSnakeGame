import random
from rgbprint.color import Color as Fore


# All players logic and their scores
class Player:

    instances = 0  # how many instances of player has been created

    def __init__(self,
                 penalty_square,
                 lucky_square):

        Player.instances += 1
        self.penalty_square = penalty_square
        self.lucky_square = lucky_square
        self.player = Player.instances  # to know which player is it
        self.player_history = []  # keep track of all the moves of each player
        self.current_move = None  # which move the player is currently at

    def current_score(self):  # calculate the current score of the player
        score = sum(self.player_history)

        if score in self.penalty_square:
            self.player_history.append(-10)

        elif score in self.lucky_square:
            self.player_history.append(10)

        score = sum(self.player_history)

        return [self.player, score]

    def roll_dice(self):  # roll the dice
        print(f"\n{Fore.magenta}Player{self.player} playing his turn...")
        roll = random.randint(1, 6)

        self.current_move = roll
        print(f"Player{self.player} got {roll}...{Fore.reset}")
        self.player_history.append(roll)

    def __str__(self):  # print player's score
        return f"Player{self.player}'s Score: {self.current_score()[1]}"
