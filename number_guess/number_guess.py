from random import randint


class Guess:

    def __init__(self, total_guesses=5, max_number=100):
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
            return False
        elif self.guess < self.answer:
            return False
        else:
            return True

    def correct_answer(self):
        return randint(0, self.max_number)
