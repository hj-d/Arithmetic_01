from src.console_io.input_reader import InputReader
from src.console_io.output_writer import OutputWriter
from src.domain.calculator import Calculator
from src.domain.exception.divide_by_zero_exception import DivideByZeroException
from src.domain.exception.invalid_expression_exception import InvalidExpressionException
from src.domain.operator_registry import OperatorRegistry
from src.parser.expression_parser import ExpressionParser


class ArithmeticApp:
    """콘솔 사용자와 도메인을 잇는 흐름 조율자.

    한 줄을 입력받아 → 파싱 → 연산자 조회 → 계산 → 출력 한다.
    종료 명령 또는 EOF 시 루프를 끝낸다.
    """

    EXIT_COMMANDS = frozenset({"exit", "quit", "q"})
    PROMPT = "> "

    def __init__(
        self,
        reader: InputReader,
        writer: OutputWriter,
        parser: ExpressionParser,
        registry: OperatorRegistry,
        calculator: Calculator,
    ) -> None:
        self._reader = reader
        self._writer = writer
        self._parser = parser
        self._registry = registry
        self._calculator = calculator

    def run(self) -> None:
        self._writer.write("Arithmetic Calculator")
        self._writer.write(
            f"지원 연산: {' '.join(self._registry.supported_symbols())} | "
            f"종료: {', '.join(sorted(self.EXIT_COMMANDS))}"
        )
        self._writer.write("예) 3 + 4")
        while True:
            line = self._reader.read_line(self.PROMPT)
            if line is None:
                break
            stripped = line.strip()
            if not stripped:
                continue
            if stripped.lower() in self.EXIT_COMMANDS:
                break
            self._process(stripped)
        self._writer.write("Bye!")

    def _process(self, line: str) -> None:
        try:
            expression = self._parser.parse(line)
            operator = self._registry.get(expression.operator_symbol)
            result = self._calculator.calculate(expression, operator)
            self._writer.write(f"= {self._format(result)}")
        except (InvalidExpressionException, DivideByZeroException) as e:
            self._writer.write_error(f"오류: {e}")

    @staticmethod
    def _format(value: float) -> str:
        if value.is_integer():
            return str(int(value))
        return str(value)
