import pytest

from src.domain.arithmetic import add, divide, multiply, subtract
from src.domain.exception.divide_by_zero_exception import DivideByZeroException


class TestAdd:
    @pytest.mark.parametrize("a,b,expected", [
        (2, 3, 5),
        (-1, 1, 0),
        (0, 0, 0),
        (-5, -3, -8),
        (1.5, 2.5, 4.0),
        (1_000_000, 2_000_000, 3_000_000),
    ])
    def test_returns_sum(self, a: float, b: float, expected: float) -> None:
        assert add(a, b) == expected

    def test_floating_point_precision(self) -> None:
        assert add(0.1, 0.2) == pytest.approx(0.3)

    def test_is_commutative(self) -> None:
        assert add(3, 5) == add(5, 3)

    def test_identity_with_zero(self) -> None:
        assert add(42, 0) == 42
        assert add(0, 42) == 42


class TestSubtract:
    @pytest.mark.parametrize("a,b,expected", [
        (5, 3, 2),
        (0, 0, 0),
        (-1, -1, 0),
        (3, 5, -2),
        (10.5, 0.5, 10.0),
        (-5, -3, -2),
    ])
    def test_returns_difference(self, a: float, b: float, expected: float) -> None:
        assert subtract(a, b) == expected

    def test_is_not_commutative(self) -> None:
        assert subtract(3, 5) != subtract(5, 3)

    def test_self_subtraction_is_zero(self) -> None:
        assert subtract(7, 7) == 0
        assert subtract(-3.14, -3.14) == 0


class TestMultiply:
    @pytest.mark.parametrize("a,b,expected", [
        (3, 4, 12),
        (0, 5, 0),
        (-2, 3, -6),
        (-2, -3, 6),
        (1.5, 2, 3.0),
    ])
    def test_returns_product(self, a: float, b: float, expected: float) -> None:
        assert multiply(a, b) == expected

    def test_zero_property(self) -> None:
        assert multiply(0, 1234567) == 0
        assert multiply(987654, 0) == 0

    def test_is_commutative(self) -> None:
        assert multiply(3, 5) == multiply(5, 3)

    def test_identity_with_one(self) -> None:
        assert multiply(42, 1) == 42
        assert multiply(1, 42) == 42


class TestDivide:
    @pytest.mark.parametrize("a,b,expected", [
        (10, 2, 5),
        (7, 2, 3.5),
        (-6, 3, -2),
        (0, 5, 0),
        (1, 4, 0.25),
        (100, 25, 4),
    ])
    def test_returns_quotient(self, a: float, b: float, expected: float) -> None:
        assert divide(a, b) == expected

    def test_self_division_is_one(self) -> None:
        assert divide(7, 7) == 1
        assert divide(-3.14, -3.14) == 1

    def test_divide_by_zero_raises(self) -> None:
        with pytest.raises(DivideByZeroException):
            divide(1, 0)

    def test_zero_divided_by_zero_also_raises(self) -> None:
        with pytest.raises(DivideByZeroException):
            divide(0, 0)

    def test_negative_divided_by_zero_raises(self) -> None:
        with pytest.raises(DivideByZeroException):
            divide(-5, 0)

    def test_divide_by_negative_zero_also_raises(self) -> None:
        with pytest.raises(DivideByZeroException):
            divide(1, -0.0)

    def test_exception_message_describes_problem(self) -> None:
        with pytest.raises(DivideByZeroException) as exc_info:
            divide(1, 0)
        assert "0으로 나눌 수 없습니다" in str(exc_info.value)


class TestPurity:
    """순수성 (referential transparency) 검증."""

    def test_same_input_same_output(self) -> None:
        for _ in range(3):
            assert add(2, 3) == 5
            assert subtract(10, 4) == 6
            assert multiply(3, 4) == 12
            assert divide(8, 2) == 4

    def test_no_mutation_of_inputs(self) -> None:
        a, b = 5.5, 3.3
        add(a, b)
        subtract(a, b)
        multiply(a, b)
        divide(a, b)
        assert a == 5.5
        assert b == 3.3
