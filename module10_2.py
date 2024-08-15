# Задача "За честь и отвагу!":
# Создайте класс Knight, наследованный от Thread, объекты которого будут обладать следующими свойствами:
# Атрибут name - имя рыцаря. (str)
# Атрибут power - сила рыцаря. (int)
# А также метод run, в котором рыцарь будет сражаться с врагами:
# При запуске потока должна выводится надпись "<Имя рыцаря>, на нас напали!".
# Рыцарь сражается до тех пор, пока не повергнет всех врагов (у всех потоков их 100).
# В процессе сражения количество врагов уменьшается на power текущего рыцаря.
# По прошествию 1 дня сражения (1 секунды) выводится строка "<Имя рыцаря> сражается <кол-во дней>
# ..., осталось <кол-во воинов> воинов."
# После победы над всеми врагами выводится надпись "<Имя рыцаря> одержал победу спустя <кол-во дней> дней(дня)!"
# Как можно заметить нужно сделать задержку в 1 секунду, инструменты для задержки выберите сами.
# Пункты задачи:
# Создайте класс Knight с соответствующими описанию свойствами.
# Создайте и запустите 2 потока на основе класса Knight.
# Выведите на экран строку об окончании битв.


from threading import Thread, Lock
from time import sleep

s_print_lock = Lock()


class Knight(Thread):
    def __init__(self, name, power):
        super(Knight, self).__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали!', flush=True)
        quantity_warriors = 100
        counter_days = 0
        while quantity_warriors > 0:
            quantity_warriors -= min(self.power, quantity_warriors)
            counter_days += 1
            sleep(1)
            with s_print_lock:
                print(f'{self.name} сражается {counter_days} день(дня)...,  осталось {quantity_warriors} воинов.',
                      flush=True)
        with s_print_lock:
            print(f'{self.name} одержал победу спустя {counter_days} дней(дня)!', flush=True)


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()
print('Все битвы закончились!')
