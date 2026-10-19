
import importlib

module = importlib.import_module("codes.40_gcd")


def test_gcd_of_two_numbers():
    assert module.gcd(12, 8) == 4


def test_one_number_divides_other():
    assert module.gcd(18, 6) == 6


def test_coprime_numbers():
    assert module.gcd(7, 3) == 1


def test_equal_numbers():
    assert module.gcd(5, 5) == 5


def test_zero_and_number():
    assert module.gcd(0, 8) == 8


def test_negative_numbers():
    assert module.gcd(-12, 8) == 4
