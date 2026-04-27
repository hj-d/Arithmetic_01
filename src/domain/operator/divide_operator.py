from src.domain.arithmetic import divide
from src.domain.operator.operator import Operator


class DivideOperator(Operator):
    @property
    def symbol(self) -> str:
        return "/"

    def apply(self, left: float, right: float) -> float:
        return divide(left, right)
