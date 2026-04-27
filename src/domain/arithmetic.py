"""순수 사칙연산 함수 모듈.

이 모듈은 도메인 계층의 *정식 수학 로직 위치* 다.
- 부수 효과 없음 (입력값을 바꾸지 않고, I/O를 수행하지 않음)
- 외부 라이브러리 의존성 없음 (도메인 예외만 import)
- 같은 입력 → 항상 같은 출력 (referential transparency)

Operator 전략 클래스들은 본 모듈의 함수에 위임하여 수학 로직 중복을 제거한다.
"""

from src.domain.exception.divide_by_zero_exception import DivideByZeroException


def add(left: float, right: float) -> float:
    """두 수의 합을 반환한다.

    Args:
        left: 좌측 피연산자.
        right: 우측 피연산자.

    Returns:
        left + right.
    """
    return left + right


def subtract(left: float, right: float) -> float:
    """좌변에서 우변을 뺀 값을 반환한다.

    Args:
        left: 피감수.
        right: 감수.

    Returns:
        left - right.
    """
    return left - right


def multiply(left: float, right: float) -> float:
    """두 수의 곱을 반환한다.

    Args:
        left: 좌측 피연산자.
        right: 우측 피연산자.

    Returns:
        left * right.
    """
    return left * right


def divide(left: float, right: float) -> float:
    """좌변을 우변으로 나눈 몫을 반환한다.

    Args:
        left: 피제수.
        right: 제수. 0이면 DivideByZeroException.

    Returns:
        left / right.

    Raises:
        DivideByZeroException: right가 0인 경우.
    """
    if right == 0:
        raise DivideByZeroException("0으로 나눌 수 없습니다.")
    return left / right
