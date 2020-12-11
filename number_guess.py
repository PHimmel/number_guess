from random import randint
from time import sleep


class Guess:

    def __init__(self, set_size=None):
        self.set_size = set_size
        if set_size is None:
            self.set_size = self.get_set_size()
        self.guess = None
        self.answer = self.correct_answer()

    def get_set_size(self):
        self.set_size = int(input('What is the total size of the numbers to draw from?'))
        return self.set_size

    def get_guess(self):
        self.guess = int(input('What number are you thinking it is?'))

    def guess_number(self):
        pass

    def correct_answer(self):
        return randint(0, self.set_size)

