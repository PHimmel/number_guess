from time import sleep
from number_guess.number_guess import Guess


def play_game():
    game = Guess()
    game.set_max_size()
    correct_answer_received = False

    while correct_answer_received is False:
        game.set_guess()
        sleep(2)
        pass


def main():
    print(3)
    play_game()


if __name__ == '__main__':
    main()

