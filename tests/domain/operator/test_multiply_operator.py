import pytest

from src.domain.operator.multiply_operator import MultiplyOperator


@pytest.fixture
def op() -> MultiplyOperator:
    return MultiplyOperator()


def test_symbol(op: MultiplyOperator) -> None:
    assert op.symbol == "*"


@pytest.mark.parametrize("left,right,expected", [
    (3, 4, 12),
    (0, 5, 0),
    (-2, 3, -6),
    (-2, -3, 6),
    (1.5, 2, 3.0),
])
def test_apply(op: MultiplyOperator, left: float, right: float, expected: float) -> None:
    assert op.apply(left, right) == expected
