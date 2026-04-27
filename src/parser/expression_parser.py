import re

from src.domain.exception.invalid_expression_exception import InvalidExpressionException
from src.parser.expression import Expression


class ExpressionParser:
    """'<숫자> <연산자> <숫자>' 형식의 단순 이항 식 문자열을 Expression으로 변환."""

    _PATTERN = re.compile(
        r"^\s*(?P<left>[-+]?\d+(?:\.\d+)?)"
        r"\s*(?P<op>[+\-*/])"
        r"\s*(?P<right>[-+]?\d+(?:\.\d+)?)\s*$"
    )

    def parse(self, source: str) -> Expression:
        match = self._PATTERN.match(source)
        if not match:
            raise InvalidExpressionException(
                f"식을 해석할 수 없습니다: {source!r}. 형식: '<숫자> <연산자> <숫자>'"
            )
        try:
            left = float(match.group("left"))
            right = float(match.group("right"))
        except ValueError as e:
            raise InvalidExpressionException(f"숫자 형식 오류: {e}") from e
        return Expression(left=left, operator_symbol=match.group("op"), right=right)
