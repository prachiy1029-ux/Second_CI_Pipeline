import importlib

module = importlib.import_module("codes.32_count_words")


def test_count_words():
    assert module.count_words("I love Python") == 3


def test_extra_spaces():
    assert module.count_words("  Hello   World  ") == 2


def test_empty_sentence():
    assert module.count_words("") == 0


def test_only_spaces():
    assert module.count_words("    ") == 0
