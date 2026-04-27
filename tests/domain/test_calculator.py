import pytest

from src.domain.calculator import Calculator
from src.domain.operator_registry import OperatorRegistry
from src.parser.expression import Expression


@pytest.fixture
def calculator() -> Calculator:
    return Calculator()


@pytest.fixture
def registry() -> OperatorRegistry:
    return OperatorRegistry.with_default_operators()


@pytest.mark.parametrize("left,symbol,right,expected", [
    (2, "+", 3, 5),
    (10, "-", 4, 6),
    (3, "*", 4, 12),
    (8, "/", 2, 4),
])
def test_calculator_with_each_operator(
    calculator: Calculator,
    registry: OperatorRegistry,
    left: float,
    symbol: str,
    right: float,
    expected: float,
) -> None:
    expression = Expression(left, symbol, right)
    operator = registry.get(symbol)
    assert calculator.calculate(expression, operator) == expected
