import importlib

module = importlib.import_module("codes.34_check_sorted")


def test_sorted_list():
    assert module.is_sorted([1, 2, 3, 4]) is True


def test_unsorted_list():
    assert module.is_sorted([1, 3, 2]) is False


def test_empty_list():
    assert module.is_sorted([]) is True


def test_duplicate_elements():
    assert module.is_sorted([1, 2, 2, 3]) is True


def test_descending_list():
    assert module.is_sorted([5, 4, 3, 2]) is False
