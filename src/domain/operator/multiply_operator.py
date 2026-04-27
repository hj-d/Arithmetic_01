from src.domain.operator.operator import Operator


class MultiplyOperator(Operator):
    @property
    def symbol(self) -> str:
        return "*"

    def apply(self, left: float, right: float) -> float:
        return left * right
