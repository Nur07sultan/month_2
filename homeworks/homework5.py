# homeworks/homework_5.py
from homeworks.distance import Distance

# создаём несколько экземпляров
d1 = Distance(10, "m")
d2 = Distance(2, "km")
d3 = Distance(1200, "m")

print("Инициализация и вывод:")
print(d1)  # 10 m
print(d2)  # 2 km
print(d3)  # 1200 m

print("\nСложение:")
print(d1 + d3)  # 1210 m
print(d2 + d1)  # 2010 m (в метрах, потому что d2 приведётся к метрам)

print("\nВычитание:")
print(d3 - d1)  # 1190 m
try:
    print(d1 - d2)  # должно выбросить ошибку (отрицательный результат)
except ValueError as e:
    print("Ошибка:", e)

print("\nСравнения:")
print(d1 == Distance(1000, "cm"))   # True
print(d2 > d3)                      # True (2000 m > 1200 m)
print(d1 < d3)                      # True
