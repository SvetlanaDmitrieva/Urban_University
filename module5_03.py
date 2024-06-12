# Создайте новый класс Building
# Создайте инициализатор для класса Building, который будет задавать целочисленный атрибут
# этажности self.numberOfFloors и строковый атрибут self.buildingType
# Создайте(перегрузите) __eq__, используйте атрибут numberOfFloors и buildingType для сравнения
# Полученный код напишите в ответ к домашнему заданию
import self


class Building:
    def __init__(self,  numberOfFloors :int, buildingType :str):
        self.numberOfFloors = numberOfFloors
        self.buildingType = buildingType

    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType


B1 = Building(3, 'дом')
B2 = Building(3, 'дом')
print(B1 == B2)

B3 = Building(3, 'дом')
B4 = Building(4, 'дом')
print(B3 == B4)

B5 = Building(3, 'дом')
B6 = Building(3, 'Дом')
print(B5 == B6)
