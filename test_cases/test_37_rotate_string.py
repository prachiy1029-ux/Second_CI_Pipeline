
import importlib

module = importlib.import_module("codes.37_rotate_string")


def test_rotate_left_by_two():
    assert module.rotate_string("hello", 2) == "llohe"


def test_rotate_by_one():
    assert module.rotate_string("python", 1) == "ythonp"


def test_rotate_by_length():
    assert module.rotate_string("hello", 5) == "hello"


def test_rotate_by_more_than_length():
    assert module.rotate_string("hello", 7) == "llohe"


def test_empty_string():
    assert module.rotate_string("", 2) == ""


def test_zero_positions():
    assert module.rotate_string("hello", 0) == "hello"
