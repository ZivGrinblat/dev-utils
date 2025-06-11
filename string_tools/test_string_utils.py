# test_string_utils.py

from string_utils import reverse_string, count_vowels, capitalize_words


def test_reverse_string():
    assert reverse_string("hello") == "olleh"
    assert reverse_string("") == ""
    assert reverse_string("A") == "A"


def test_count_vowels():
    assert count_vowels("hello") == 2
    assert count_vowels("xyz") == 0
    assert count_vowels("AEIOUaeiou") == 10


def test_capitalize_words():
    assert capitalize_words("hello world") == "Hello World"
    assert capitalize_words("python is fun") == "Python Is Fun"
