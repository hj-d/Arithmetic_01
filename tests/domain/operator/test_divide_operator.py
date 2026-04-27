import pytest

from src.domain.exception.divide_by_zero_exception import DivideByZeroException
from src.domain.operator.divide_operator import DivideOperator


@pytest.fixture
def op() -> DivideOperator:
    return DivideOperator()


def test_symbol(op: DivideOperator) -> None:
    assert op.symbol == "/"


@pytest.mark.parametrize("left,right,expected", [
    (10, 2, 5),
    (7, 2, 3.5),
    (-6, 3, -2),
    (0, 5, 0),
])
def test_apply(op: DivideOperator, left: float, right: float, expected: float) -> None:
    assert op.apply(left, right) == expected


def test_divide_by_zero_raises(op: DivideOperator) -> None:
    with pytest.raises(DivideByZeroException):
        op.apply(1, 0)


def test_zero_divided_by_zero_also_raises(op: DivideOperator) -> None:
    with pytest.raises(DivideByZeroException):
        op.apply(0, 0)
