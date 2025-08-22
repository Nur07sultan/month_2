# homeworks/distance.py

class Distance:
    # коэффициенты для перевода в метры
    _units_to_meters = {
        "mm": 0.001,
        "cm": 0.01,
        "m": 1,
        "km": 1000,
    }

    def __init__(self, value: float, unit: str = "m"):
        if unit not in self._units_to_meters:
            raise ValueError(f"Неподдерживаемая единица измерения: {unit}")
        if value < 0:
            raise ValueError("Расстояние не может быть отрицательным")
        self.value = value
        self.unit = unit

    def __str__(self):
        return f"{self.value} {self.unit}"

    # преобразование в метры
    def to_meters(self):
        return self.value * self._units_to_meters[self.unit]

    # конвертация в другую единицу
    def to_unit(self, unit: str):
        if unit not in self._units_to_meters:
            raise ValueError(f"Неподдерживаемая единица измерения: {unit}")
        value_in_meters = self.to_meters()
        return value_in_meters / self._units_to_meters[unit]

    # сложение
    def __add__(self, other):
        if not isinstance(other, Distance):
            return NotImplemented
        total_meters = self.to_meters() + other.to_meters()
        return Distance(total_meters / self._units_to_meters[self.unit], self.unit)

    # вычитание
    def __sub__(self, other):
        if not isinstance(other, Distance):
            return NotImplemented
        result_meters = self.to_meters() - other.to_meters()
        if result_meters < 0:
            raise ValueError("Результат вычитания не может быть отрицательным")
        return Distance(result_meters / self._units_to_meters[self.unit], self.unit)

    # сравнения
    def __eq__(self, other):
        return self.to_meters() == other.to_meters()

    def __lt__(self, other):
        return self.to_meters() < other.to_meters()

    def __le__(self, other):
        return self.to_meters() <= other.to_meters()

    def __gt__(self, other):
        return self.to_meters() > other.to_meters()

    def __ge__(self, other):
        return self.to_meters() >= other.to_meters()
