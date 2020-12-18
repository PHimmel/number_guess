import sys
sys.path.append(".")

from number_guess.number_guess import Guess

def test_setting_max_number():
    guess = Guess()
    guess.set_max_size(10)

    assert guess.max_number == 10
