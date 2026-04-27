from src.domain.arithmetic import subtract
from src.domain.operator.operator import Operator


class SubtractOperator(Operator):
    @property
    def symbol(self) -> str:
        return "-"

    def apply(self, left: float, right: float) -> float:
        return subtract(left, right)
