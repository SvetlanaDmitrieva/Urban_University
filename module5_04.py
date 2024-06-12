# Создайте новый класс Building  с атрибутом total
# Создайте инициализатор для класса Building , который будет увеличивать атрибут количества
# созданных объектов класса Building total
# В цикле создайте 40 объектов класса Building и выведите их на экран командой print
# Полученный код напишите в ответ к домашнему заданию

from random import randint


class Building:
    total = 0

    def __init__(self, numberOfFloors: int, buildingType: str):
        self.numberOfFloors = numberOfFloors
        self.buildingType = buildingType
        Building.total += 1

    def __str__(self):
        return f'Количество этажей: {self.numberOfFloors},  Строение: {self.buildingType}'


Buildings = []
for i in range(40):
    B1 = Building(randint(1, 25), ('building ' + str(i + 1)))
    print(B1)
    Buildings.append(B1)
print('Общее количество созданных объектов: ', Building.total)
