import importlib

module = importlib.import_module("codes.33_first_non_repeating")


def test_first_non_repeating_character():
    assert module.first_non_repeating_char("swiss") == "w"


def test_first_character_is_unique():
    assert module.first_non_repeating_char("hello") == "h"


def test_no_non_repeating_character():
    assert module.first_non_repeating_char("aabb") is None


def test_empty_string():
    assert module.first_non_repeating_char("") is None