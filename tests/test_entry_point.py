import sys
sys.path.append(".")

from number_guess.number_guess import Guess

def test_setting_max_number():
    guess = Guess()
    guess.set_max_size(10)

    assert guess.max_number == 10

def test_generated_correct_answer_is_within_bounds():
    guess = Guess()
    guess.set_max_size(2)

    correct_answer = guess.generate_correct_answer()

    assert correct_answer >= 0
    assert correct_answer <= 2
