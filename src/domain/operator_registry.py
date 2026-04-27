from src.domain.exception.invalid_expression_exception import InvalidExpressionException
from src.domain.operator.add_operator import AddOperator
from src.domain.operator.divide_operator import DivideOperator
from src.domain.operator.multiply_operator import MultiplyOperator
from src.domain.operator.operator import Operator
from src.domain.operator.subtract_operator import SubtractOperator


class OperatorRegistry:
    """기호("+", "-", ...) → Operator 인스턴스 매핑 저장소.

    새 연산자를 추가할 때는 register()로 등록만 하면 된다.
    Calculator/Parser/App은 본 레지스트리에만 의존하므로 다른 코드는 변경 불필요.
    """

    def __init__(self) -> None:
        self._operators: dict[str, Operator] = {}

    @classmethod
    def with_default_operators(cls) -> "OperatorRegistry":
        registry = cls()
        for op in (AddOperator(), SubtractOperator(), MultiplyOperator(), DivideOperator()):
            registry.register(op)
        return registry

    def register(self, operator: Operator) -> None:
        self._operators[operator.symbol] = operator

    def get(self, symbol: str) -> Operator:
        if symbol not in self._operators:
            raise InvalidExpressionException(f"지원하지 않는 연산자입니다: {symbol!r}")
        return self._operators[symbol]

    def supported_symbols(self) -> list[str]:
        return list(self._operators.keys())
