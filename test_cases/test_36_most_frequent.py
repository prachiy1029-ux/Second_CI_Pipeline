
import importlib

module = importlib.import_module("codes.36_most_frequent")


def test_most_frequent_element():
    assert module.most_frequent([1, 2, 2, 3, 2, 4]) == 2


def test_first_element_most_frequent():
    assert module.most_frequent([4, 4, 2, 2, 3]) == 4


def test_single_element():
    assert module.most_frequent([7]) == 7


def test_empty_list():
    assert module.most_frequent([]) is None


def test_negative_numbers():
    assert module.most_frequent([-1, -2, -1, -3]) == -1


def test_all_elements_equal():
    assert module.most_frequent([5, 5, 5]) == 5