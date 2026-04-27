import sys

from src.console_io.output_writer import OutputWriter


class ConsoleOutputWriter(OutputWriter):
    def write(self, message: str) -> None:
        print(message)

    def write_error(self, message: str) -> None:
        print(message, file=sys.stderr)
