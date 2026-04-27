import pytest

from src.domain.exception.invalid_expression_exception import InvalidExpressionException
from src.parser.expression import Expression
from src.parser.expression_parser import ExpressionParser


@pytest.fixture
def parser() -> ExpressionParser:
    return ExpressionParser()


@pytest.mark.parametrize("source,expected", [
    ("3 + 4", Expression(3.0, "+", 4.0)),
    ("10-2", Expression(10.0, "-", 2.0)),
    ("5 * 6", Expression(5.0, "*", 6.0)),
    ("8 / 2", Expression(8.0, "/", 2.0)),
    ("  7  +  3  ", Expression(7.0, "+", 3.0)),
    ("-3 + 4", Expression(-3.0, "+", 4.0)),
    ("3 + -4", Expression(3.0, "+", -4.0)),
    ("3.14 * 2", Expression(3.14, "*", 2.0)),
    ("0.5 / 0.25", Expression(0.5, "/", 0.25)),
])
def test_parse_valid(parser: ExpressionParser, source: str, expected: Expression) -> None:
    assert parser.parse(source) == expected


@pytest.mark.parametrize("source", [
    "",
    "   ",
    "3",
    "3 +",
    "+ 4",
    "3 + 4 + 5",
    "abc",
    "3 ^ 4",
    "3 + four",
    "3 ++ 4",
])
def test_parse_invalid_raises(parser: ExpressionParser, source: str) -> None:
    with pytest.raises(InvalidExpressionException):
        parser.parse(source)
