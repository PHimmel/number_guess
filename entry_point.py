from time import sleep
from number_guess.number_guess import Guess


def play_game():
    game = Guess()
#    game.set_max_size()

    while game.set_guess() is False:
        sleep(1)


def main():
    play_game()


if __name__ == '__main__':
    main()

