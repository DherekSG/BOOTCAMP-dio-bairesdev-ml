import pytest
import math_utils

def test_add_two_positive_numbers():
    assert math_utils.add(2, 3) == 5

def test_add_with_zero():
    assert math_utils.add(0, 5) == 5

def test_add_negative_and_positive():
    assert math_utils.add(-2, 3) == 1

def test_add_two_floats():
    assert math_utils.add(1.5, 2.5) == 4.0

def test_divide_integers():
    assert math_utils.divide(10, 2) == 5

def test_divide_floats():
    assert math_utils.divide(7.5, 2.5) == 3.0

def test_divide_by_zero_raises():
    with pytest.raises(ZeroDivisionError):
        math_utils.divide(5, 0)