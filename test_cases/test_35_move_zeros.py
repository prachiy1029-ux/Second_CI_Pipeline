
import importlib

module = importlib.import_module("codes.35_move_zeros")


def test_zeros_at_end():
    assert module.move_zeros([1, 0, 2, 0, 3]) == [1, 2, 3, 0, 0]


def test_no_zeros():
    assert module.move_zeros([1, 2, 3]) == [1, 2, 3]


def test_all_zeros():
    assert module.move_zeros([0, 0, 0]) == [0, 0, 0]


def test_empty_list():
    assert module.move_zeros([]) == []


def test_zeros_at_start():
    assert module.move_zeros([0, 0, 4, 5]) == [4, 5, 0, 0]


def test_preserves_negative_numbers():
    assert module.move_zeros([-1, 0, -2, 3]) == [-1, -2, 3, 0]
