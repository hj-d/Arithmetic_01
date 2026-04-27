# Arithmetic_01

- **Author**: 이현진 (YiHyunjin)
- **Reviewer**: 이현진 (YiHyunjin)

## Description
콘솔 기반 사칙연산 계산기. 단일 책임 원칙(SRP)과 확장성을 고려한 계층형 구조.

## Requirements
- Python 3.10+

## Run
```powershell
python -m src.main
```
종료: `exit`, `quit`, `q` 또는 `Ctrl+Z` (Windows) / `Ctrl+D` (Unix)

## Test
```powershell
pip install -r requirements.txt
pytest
```

## Structure
```
src/
  main.py                     # 진입점 (의존성 조립)
  app/arithmetic_app.py       # 콘솔 루프 / 흐름 조율
  domain/                     # 순수 비즈니스 로직 (외부 의존성 없음)
    calculator.py             # 연산 실행 엔진
    operator_registry.py      # 기호 → Operator 매핑
    operator/                 # 연산자 추상화 + 4개 구현체
    exception/                # 도메인 예외
  parser/                     # 입력 문자열 → Expression
  console_io/                 # I/O 추상화 + 콘솔 구현체
tests/                        # pytest 단위 테스트
```

## Extension Points
- 새 연산자 추가: `domain/operator/`에 `Operator` 구현체 작성 후 `OperatorRegistry`에 등록
- 입력 매체 변경: `console_io/`에 `InputReader` 구현체 추가
- 복합식 지원: `parser/expression_parser.py`만 교체
