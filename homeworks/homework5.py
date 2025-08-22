class Distance:
    conversion_factors = {
        'centimeters': 1,
        'meters': 100,
        'kilometers': 100000,
    }

    def __init__(self, value, unit):
        if unit not in self.conversion_factors:
            raise ValueError(f"Unsupported unit: {unit}")
        self.value = value
        self.unit = unit

    def __str__(self):
        return f"{self.value} {self.unit}"

    @staticmethod
    def convert(value, from_unit, to_unit):
        if from_unit == to_unit:
            return value
        return value * (Distance.conversion_factors[from_unit] / Distance.conversion_factors[to_unit])

    def __add__(self, other):
        if not isinstance(other, Distance):
            return NotImplemented
        total_value = self.convert(self.value, self.unit, other.unit) + other.value
        return Distance(total_value, other.unit)

    def __sub__(self, other):
        if not isinstance(other, Distance):
            return NotImplemented
        total_value = self.convert(self.value, self.unit, other.unit) - other.value
        if total_value < 0:
            raise ValueError("Resulting distance cannot be negative")
        return Distance(total_value, other.unit)

    def __lt__(self, other):
        if not isinstance(other, Distance):
            return NotImplemented
        return self.convert(self.value, self.unit, other.unit) < other.value

    def __le__(self, other):
        return self < other or self == other

    def __eq__(self, other):
        if not isinstance(other, Distance):
            return NotImplemented
        return self.convert(self.value, self.unit, other.unit) == other.value

    def __gt__(self, other):
        return not (self <= other)

    def __ge__(self, other):
        return not (self < other)


def main():
    d1 = Distance(10, 'meters')
    d2 = Distance(2, 'kilometers')
    d3 = Distance(500, 'centimeters')

    print("Distance 1:", d1)
    print("Distance 2:", d2)
    print("Distance 3:", d3)

    # Сложение
    sum_distance = d1 + d2
    print("Sum:", sum_distance)

    # Вычитание
    sub_distance = d2 - d1
    print("Subtraction:", sub_distance)

    # Проверка сравнения
    print("Is d1 < d2?", d1 < d2)
    print("Is d2 > d3?", d2 > d3)


if __name__ == "__main__":
    main()