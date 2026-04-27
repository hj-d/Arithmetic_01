from abc import ABC, abstractmethod


class OutputWriter(ABC):
    """출력 추상화. 표준출력/표준오류를 분리해 다룬다."""

    @abstractmethod
    def write(self, message: str) -> None: ...

    @abstractmethod
    def write_error(self, message: str) -> None: ...
