from rgbprint.color import Color as Fore
from rgbprint.gradient import gradient_print
from game import Game
import time

"""
Made by 0xHaris
Github: https://github.com/0xHaris
Email: 0xbitshot@gmail.com
"""


LOGO = f"""
▄▄▄         ▄▄▄· ▄▄▄ .    .▄▄ ·   ▐  ▄  ▄▄▄· ▄ •▄ ▄▄▄ .
▀▄ █·▪     ▐█ ▄█ ▀▄.▀·    ▐█ ▀. • █▌▐█ ▐█ ▀█ █▌▄▌▪▀▄.▀·
▐▀▀▄  ▄█▀▄  ██▀· ▐▀▀▪▄    ▄▀▀▀█▄ ▐█▐▐▌ ▄█▀▀█ ▐▀▀▄·▐▀▀▪▄
▐█•█▌▐█▌.▐▌▐█▪·• ▐█▄▄▌    ▐█▄▪▐█ ██▐█▌ ▐█ ▪▐▌▐█.█▌▐█▄▄▌
.▀  ▀ ▀█▄▀▪.▀     ▀▀▀      ▀▀▀▀  ▀▀ █▪  ▀  ▀ ·▀  ▀ ▀▀▀ """


def main():  # main function This is where the program will be executed
    gradient_print(LOGO, start_color="red", end_color="white")  # print logo to the console
    r = input(f"\n{Fore.red}Do you want to play the game? (y/n): ")
    if r.strip().lower() == "n":
        exit(0)  # exit

    for i in range(0, 101):
        time.sleep(0.01)
        print(f"{Fore.green}[{i}%] Loading...", end="\r")

    resp = input(f"\nHow many players want to play the game?:{Fore.reset} ")
    if resp.isdecimal():  # input must be integers
        players = int(resp.strip())
        game = Game(players)
        game.start_game()
        while True:
            game.play()
            top = game.leaderboard()
            if top[1] >= game.MAX_PATH:
                print(f"\n{Fore.green}Player{top[0]} won the game!")
                exit(0)
    else:
        print("Wrong input!")
        exit(1)


if __name__ == '__main__':
    main()
