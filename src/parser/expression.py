from dataclasses import dataclass


@dataclass(frozen=True)
class Expression:
    """파싱된 이항 식의 불변 데이터 구조."""

    left: float
    operator_symbol: str
    right: float
