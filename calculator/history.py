from calculator.calculation import Calculation


class History:
    def __init__(self) -> None:
        self._calculations: list[Calculation] = []

    def add(self, calculation: Calculation) -> None:
        self._calculations.append(calculation)

    def get_all(self) -> list[Calculation]:
        return list(self._calculations)

    def remove(self, index: int) -> Calculation:
        if not 0 <= index < len(self._calculations):
            raise IndexError("No history entry at that position.")
        return self._calculations.pop(index)