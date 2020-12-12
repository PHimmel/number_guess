from time import sleep
from number_guess.number_guess import Guess


def play_game():
    game = Guess()
    answer = False

    while answer is False:
        try:
            evaluation = game.set_guess()
            print(evaluation)

            if evaluation == '=':
                print('You won!\n')
                break

        except ValueError:
            print('Only int values!')
            continue

        sleep(1)


def main():
    play_game()


if __name__ == '__main__':
    main()

