from src.app.arithmetic_app import ArithmeticApp
from src.console_io.console_input_reader import ConsoleInputReader
from src.console_io.console_output_writer import ConsoleOutputWriter
from src.domain.calculator import Calculator
from src.domain.operator_registry import OperatorRegistry
from src.parser.expression_parser import ExpressionParser


def main() -> None:
    """진입점: 의존성을 조립하고 ArithmeticApp을 실행한다."""
    app = ArithmeticApp(
        reader=ConsoleInputReader(),
        writer=ConsoleOutputWriter(),
        parser=ExpressionParser(),
        registry=OperatorRegistry.with_default_operators(),
        calculator=Calculator(),
    )
    app.run()


if __name__ == "__main__":
    main()
