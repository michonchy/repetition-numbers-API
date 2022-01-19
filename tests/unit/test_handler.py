import json

from repetition_numbers import app

def test_is_repetition_numbers():
    assert app.is_repetition_numbers(2) == 1
