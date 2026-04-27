import pytest

from src.domain.operator.subtract_operator import SubtractOperator


@pytest.fixture
def op() -> SubtractOperator:
    return SubtractOperator()


def test_symbol(op: SubtractOperator) -> None:
    assert op.symbol == "-"


@pytest.mark.parametrize("left,right,expected", [
    (5, 3, 2),
    (0, 0, 0),
    (-1, -1, 0),
    (3, 5, -2),
])
def test_apply(op: SubtractOperator, left: float, right: float, expected: float) -> None:
    assert op.apply(left, right) == expected
