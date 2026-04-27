from typing import Optional

from src.console_io.input_reader import InputReader


class ConsoleInputReader(InputReader):
    def read_line(self, prompt: str = "") -> Optional[str]:
        try:
            return input(prompt)
        except EOFError:
            return None
