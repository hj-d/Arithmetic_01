from abc import ABC, abstractmethod
from typing import Optional


class InputReader(ABC):
    """입력 추상화. 테스트 시 mock으로 대체하거나 파일/네트워크 입력으로 교체 가능."""

    @abstractmethod
    def read_line(self, prompt: str = "") -> Optional[str]:
        """다음 입력 라인을 반환. EOF 도달 시 None."""
