from player import Player
from rgbprint.color import Color as Fore
import re as regex


lucky_squares = []
penalty_squares = []


# Game's logic to handle n players generated from Player class
class Game:

    MAX_PATH = 100  # maximum score
    MIN_PATH = 1  # minimum score

    def __init__(self,
                 max_player: int):

        self.max_player = max_player  # maximum players in one game
        self.players = []  # All instances of  Player class

    def start_game(self):  # start the game

        print(f"\n{Fore.cyan}Note: lucky squares and penalty squares must be different!")
        for player in range(self.max_player):
            print("\n" + f"{Fore.magenta}+".center(80, "-"))
            squares = Game._v_input(player)
            if Game._is_same_squares(squares):  # checks for same squares to avoid loopholes issues
                print("\nFound same squares. Both squares must be unique!\nExited with error code 1")
                exit(1)  # exit if found any

            player = Player(squares[0], squares[1])  # create a new player instance from Player class
            self.players.append(player)  # append to players list

    def play(self):

        for player in self.players:
            _ = input(f"\nPlayer{player.player} roll the dice! ")
            player.roll_dice()

    def leaderboard(self):  # checks who is on the top and players score
        scores = [player.current_score() for player in self.players]
        highest_score = max(scores, key=lambda x: x[1])

        print(f"\n{Fore.magenta}Leaderboard: Player{highest_score[0]} is leading the game with score of {highest_score[1]}!{Fore.reset}")
        for x in self.players:
            print(x)

        return highest_score

    @staticmethod
    def _is_same_squares(squares):

        lucky_squares.extend(squares[0])
        penalty_squares.extend(squares[1])

        u1 = set(lucky_squares)
        u2 = set(penalty_squares)

        # check for same number in individual  squares list
        if len(u1) != len(lucky_squares) or len(u2) != len(penalty_squares):
            return True

        elif not u1.isdisjoint(u2):  # check if both sets are not disjoint(unique)
            return True
        elif 100 in u2:
            return True

        return False

    @staticmethod
    def _v_input(number):  # filter the wrong input
        p = number+1
        pattern = regex.compile(r"(\d{0,2})\s+(\d{0,2})")

        lucky_square = input(f"\n{Fore.magenta}Player{p} Enter two lucky squares (seperated by space) between \
{Game.MIN_PATH} and {Game.MAX_PATH}: ")
        mo1 = pattern.search(lucky_square)
        penalty_square = input(f"\n{Fore.red}Player{p} Enter two penalty squares (seperated by space) between \
{Game.MIN_PATH} and {Game.MAX_PATH}:{Fore.reset} ")
        mo2 = pattern.search(penalty_square)

        groups = Game.__str_to_ints(p, mo1, mo2)

        return groups

    @staticmethod
    def __str_to_ints(player,  # convert inputs into integers
                      mo1: regex.Match,
                      mo2: regex.Match):

        try:
            g1 = map(int, mo1.groups())
            g2 = map(int, mo2.groups())

            return [list(g1), list(g2)]

        except Exception as e:
            print(f"\nOops! Seems like Player{player} input something wrong.\nError: {e}.\nExited with error code 1")
            exit(1)

