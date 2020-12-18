from random import randint


class Guess:

    def __init__(self, total_guesses=0, max_number=100):
        self.max_number = max_number
        self.total_guesses = total_guesses
        self.guess = None

    def start(self):
        if self.total_guesses == 0:
            max_number = self.prompt_max_size()
            self.set_max_size(max_number)
        self.answer = self.generate_correct_answer()

    def prompt_max_size(self):
        user_input = ''

        while user_input is not int:
            try:
                user_input = int(input('Enter a number: '))
                break
            except ValueError:
                print('Only int values!')

        max_number = user_input

        return max_number

    def set_max_size(self, max_number):
        self.max_number = max_number

    def set_total_guesses(self):
        self.total_guesses = int(input('What are the total number of guesses to be had?\n'))

    def set_guess(self):
        self.guess = int(input('What number are you thinking it is?\n'))
        return self.determine_correctness()

    def determine_correctness(self):
        if self.guess > self.answer:
            return 'guess > answer'
        elif self.guess < self.answer:
            return 'guess < answer'
        else:
            return '='

    def generate_correct_answer(self):
        return randint(0, self.max_number)
