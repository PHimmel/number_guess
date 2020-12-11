from random import randint
from time import sleep


class Guess:

    def __init__(self, total_guesses=None, max_number=None):
        self.max_number = max_number
        self.total_guesses = total_guesses
        self.guess = None
        self.answer = self.correct_answer()

    def set_max_size(self):
        self.max_number = int(input('What is the total size of the numbers to draw from?\n'))

    def set_total_guesses(self):
        self.total_guesses = int(input('What are the total number of guesses to be had?\n'))

    def set_guess(self):
        self.guess = int(input('What number are you thinking it is?\n'))
        return self.determine_correctness()

    def determine_correctness(self):
        if self.guess > self.answer:
            pass
        elif self.guess < self.answer:
            pass
        else:
            return True

    def correct_answer(self):
        return randint(0, self.max_number)


def play_game():
    game = Guess()
    correct_answer_received = False

    while correct_answer_received is False:
        game.set_guess()
        sleep(2)
        pass


def main():
    pass
