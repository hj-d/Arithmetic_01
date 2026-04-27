import pytest

from src.domain.operator.add_operator import AddOperator


@pytest.fixture
def op() -> AddOperator:
    return AddOperator()


def test_symbol(op: AddOperator) -> None:
    assert op.symbol == "+"


@pytest.mark.parametrize("left,right,expected", [
    (2, 3, 5),
    (-1, 1, 0),
    (0, 0, 0),
    (-5, -3, -8),
])
def test_apply(op: AddOperator, left: float, right: float, expected: float) -> None:
    assert op.apply(left, right) == expected


def test_apply_floating_point(op: AddOperator) -> None:
    assert op.apply(0.1, 0.2) == pytest.approx(0.3)
