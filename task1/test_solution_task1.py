import pytest
from solution_task1 import strict


@strict
def sum_two(a: int, b: int) -> int:
    return a + b


def test_sum_two_ok():
    assert sum_two(2, 3) == 5


def test_sum_two_typeerror():
    with pytest.raises(TypeError):
        sum_two(1, 2.0)
    with pytest.raises(TypeError):
        sum_two("1", 2)
    with pytest.raises(TypeError):
        sum_two(1, "2")


@strict
def concat(a: str, b: str) -> str:
    return a + b


def test_concat():
    assert concat("a", "b") == "ab"
    with pytest.raises(TypeError):
        concat("a", 2)


@strict
def only_bool(a: bool, b: bool) -> bool:
    return a and b


def test_only_bool():
    assert only_bool(True, False) is False
    with pytest.raises(TypeError):
        only_bool(1, 0)
