from typing import Iterable


def add(numbers: Iterable[float]) -> float:
    total = 0.0
    for n in numbers:
        total += float(n)
    return total
