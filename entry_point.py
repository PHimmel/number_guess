from time import sleep
from number_guess.number_guess import Guess


def play_game():
    game = Guess()
#    game.set_max_size()
    answer = False
    while answer is False:
        evaluation = game.set_guess()
        print(evaluation)
        if evaluation == '=':
            print('You won!')
            break
        sleep(1)


def main():
    play_game()


if __name__ == '__main__':
    main()

