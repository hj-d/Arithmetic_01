import pytest

from src.domain.exception.invalid_expression_exception import InvalidExpressionException
from src.domain.operator.add_operator import AddOperator
from src.domain.operator.divide_operator import DivideOperator
from src.domain.operator.multiply_operator import MultiplyOperator
from src.domain.operator.subtract_operator import SubtractOperator
from src.domain.operator_registry import OperatorRegistry


def test_default_registry_has_four_basic_operators() -> None:
    registry = OperatorRegistry.with_default_operators()
    assert set(registry.supported_symbols()) == {"+", "-", "*", "/"}


@pytest.mark.parametrize("symbol,expected_type", [
    ("+", AddOperator),
    ("-", SubtractOperator),
    ("*", MultiplyOperator),
    ("/", DivideOperator),
])
def test_get_returns_correct_operator(symbol: str, expected_type: type) -> None:
    registry = OperatorRegistry.with_default_operators()
    assert isinstance(registry.get(symbol), expected_type)


def test_get_unknown_symbol_raises() -> None:
    registry = OperatorRegistry.with_default_operators()
    with pytest.raises(InvalidExpressionException):
        registry.get("^")


def test_register_custom_operator() -> None:
    registry = OperatorRegistry()
    registry.register(AddOperator())
    assert registry.get("+").symbol == "+"
