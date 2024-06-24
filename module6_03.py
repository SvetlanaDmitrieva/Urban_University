# Создайте родительский(базовый) класс Vehicle, который имеет свойство vehicle_type = "none"
# Создайте родительский(базовый) класс Car, который имеет свойство price = 1000000 и
# функцию def horse_powers, которая возвращает количество лошидиных сил для автомобиля
# Создайте наследника класса Car и Vehicle - класс Nissan и переопределите свойство price
# и vehicle_type, а также переопределите функцию horse_powers
# Создайте экзмепляр класса Nissan и распечайте через функцию print vehicle_type, price


class Vehicle:
    def __init__(self,vehicle_type = 'none'):
        self.vehicle_type = vehicle_type

class Car:
    def __init__(self, price = 1000000,horse_powers_num = 0 ):
        self.price = price
        self.horse_powers_num = horse_powers_num

    def horse_powers(self):
        return self.horse_powers_num

class Nissan (Vehicle, Car):
    def __init__(self):
        self.vehicle_type = 'Nissan'
        self.price = 2000000

    def __str__(self):
        return (f'Тип автомобиля: {self.vehicle_type}, цена: {self.price}')# ,'

    def horse_powers(self):
        self.horse_powers_num = 200
        return self.horse_powers_num


Nissan_car = Nissan()
print(Nissan_car)
print(Nissan_car.horse_powers())