from src.domain.exception.divide_by_zero_exception import DivideByZeroException
from src.domain.operator.operator import Operator


class DivideOperator(Operator):
    @property
    def symbol(self) -> str:
        return "/"

    def apply(self, left: float, right: float) -> float:
        if right == 0:
            raise DivideByZeroException("0으로 나눌 수 없습니다.")
        return left / right
