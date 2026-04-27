from abc import ABC, abstractmethod


class Operator(ABC):
    """이항 연산자 추상화. 새 연산자를 추가하려면 본 클래스를 상속해 구현한다."""

    @property
    @abstractmethod
    def symbol(self) -> str:
        """연산자 기호 (예: '+', '-', '*', '/')."""

    @abstractmethod
    def apply(self, left: float, right: float) -> float:
        """두 피연산자에 연산을 적용해 결과를 반환한다."""
