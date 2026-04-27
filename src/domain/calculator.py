from src.domain.operator.operator import Operator
from src.parser.expression import Expression


class Calculator:
    """Expression과 Operator를 받아 계산을 수행하는 도메인 서비스.

    어떤 연산자가 어떤 일을 하는지는 알지 못하며, Operator.apply에 위임한다.
    """

    def calculate(self, expression: Expression, operator: Operator) -> float:
        return operator.apply(expression.left, expression.right)
