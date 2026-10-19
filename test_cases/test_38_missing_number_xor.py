import importlib

module = importlib.import_module("codes.38_missing_number_xor")


def test_missing_number_in_middle():
    assert module.find_missing_number([1, 2, 4, 5]) == 3


def test_missing_number_at_start():
    assert module.find_missing_number([2, 3, 4, 5]) == 1


def test_missing_number_at_end():
    assert module.find_missing_number([1, 2, 3, 4]) == 5


def test_two_numbers():
    assert module.find_missing_number([1]) == 2


def test_larger_list():
    assert module.find_missing_number([1, 2, 3, 5, 6, 7, 8]) == 4


def test_missing_number_near_start():
    assert module.find_missing_number([1, 3, 4, 5, 6]) == 2
