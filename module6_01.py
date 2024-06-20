# Создайте:
# 2 класса родителя: Animal, Plant
# Для класса Animal атрибуты alive = True(живой) и fed = False(накормленный),
# name - индивидуальное название каждого животного.
# Для класса Plant атрибут edible = False(съедобность), name - индивидуальное название каждого растения
#
# 4 класса наследника:
# Mammal, Predator для Animal.
# Flower, Fruit для Plant.
#
# У каждого из объектов класса Mammal и Predator должны быть атрибуты и методы:
# eat(food) - метод, где food - это параметр, принимающий объекты классов растений.
#
# Метод eat должен работать следующим образом:
# Если переданное растение (food) съедобное - выводит на экран "<self.name> съел <food.name>",
# меняется атрибут fed на True.
# Если переданное растение (food) не съедобное - выводит на экран "<self.name> не стал есть <food.name>",
# меняется атрибут alive на False.
# Т.е если животному дать съедобное растение, то животное насытится, если не съедобное - погибнет.
#
# У каждого объекта Fruit должен быть атрибут edible = True (переопределить при наследовании)
#
# Создайте объекты классов и проделайте действия затронутые в примере результата работы программы.
#
# Пункты задачи:
# Создайте классы Animal и Plant с соответствующими атрибутами и методами
# Создайте(+унаследуйте) классы Mammal, Predator, Flower, Fruit с соответствующими атрибутами и
# методами. При необходимости переопределите значения атрибутов.
# Создайте объекты этих классов.

class Animal:
    def __init__(self,name):
        self.alive = True
        self.fed = False
        self.name = name

    def eat(self, food):
        if food.edible :
            print('{} съел {}>'.format(self.name, food.name))
            self.fed = True
        else:
            print('{} не стал есть {}>'.format(self.name, food.name))
            self.alive = False


class Plant:
    def __init__(self,name ):
        self.name = name
        self.edible = False


class Mammal(Animal):
    def __init__(self,name):
        super().__init__(name)


class Predator(Animal):
    def __init__(self,name):
        super().__init__(name)


class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = True

class Flower(Plant):
    def __init__(self, name):
        super().__init__(name)


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)

# Волк с Уолл-Стрит
# Цветик семицветик
# True
# False
# Волк с Уолл-Стрит не стал есть Цветик семицветик
# Хатико съел Заводной апельсин
# False
# True
