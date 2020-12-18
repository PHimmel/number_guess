import sys
sys.path.append(".")

#import mock
from unittest import mock
#import module
#from mock import patch, MagicMock
from io import StringIO

import builtins
from number_guess.number_guess import Guess
#from number_guess.entry_point.py import play_game
import entry_point as entry_point
#import *

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

def test_game_can_be_won(capsys, monkeypatch):
    # Start game with max number of 5
    number_inputs = StringIO('5\n5\n4\n3\n2\n1\n0\n')
    monkeypatch.setattr('sys.stdin', number_inputs)
    
    assert entry_point.play_game() == 0

def test_game_can_be_won_with_large_numbers(capsys, monkeypatch):
    # Start game with max number of 10000
    max_number = 10000
    input_string = str(max_number) + "\n"

    # Generate input string
    for x in range(0, max_number + 1):
        input_string += str(x) + "\n"

    number_inputs = StringIO(input_string)
    monkeypatch.setattr('sys.stdin', number_inputs)

    assert entry_point.play_game() == 0
