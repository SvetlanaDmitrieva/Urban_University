# Задача "Банковские операции":
# Необходимо создать класс Bank со следующими свойствами:
#
# Атрибуты объекта:
# balance - баланс банка (int)
# lock - объект класса Lock для блокировки потоков.
#
# Методы объекта:
# Метод deposit:
# Будет совершать 100 транзакций пополнения средств.
# Пополнение - это увеличение баланса на случайное целое число от 50 до 500.
# Если баланс больше или равен 500 и замок lock заблокирован - lock.locked(), то разблокировать его методом release.
# После увеличения баланса должна выводится строка "Пополнение: <случайное число>. Баланс: <текущий баланс>".
# Также после всех операций поставьте ожидание в 0.001 секунды, тем самым имитируя скорость выполнения пополнения.
# Метод take:
# Будет совершать 100 транзакций снятия.
# Снятие - это уменьшение баланса на случайное целое число от 50 до 500.
# В начале должно выводится сообщение "Запрос на <случайное число>".
# Далее производится проверка: если случайное число меньше или равно текущему балансу, то произвести
# снятие, уменьшив balance на соответствующее число и вывести на экран "Снятие: <случайное число>.
# Баланс: <текущий баланс>".
# Если случайное число оказалось больше баланса, то вывести строку "Запрос отклонён,
# недостаточно средств" и заблокировать поток методом acquiere.
# Далее создайте объект класса Bank и создайте 2 потока для его методов deposit и take. Запустите эти потоки.
# После конца работы потоков выведите строку: "Итоговый баланс: <баланс объекта Bank>".
#
# По итогу вы получите скрипт блокирующий поток до баланса равному 500 и больше или блокирующий,
# когда происходит попытка снятия при недостаточном балансе.


import random
from threading import Thread, Lock
from time import sleep

thr_lock = Lock()


class Bank():
    counter = 0

    def __init__(self):
        self.balance = 0.0
        self.lock = Lock()

    def deposit(self):
        while Bank.counter < 199:
            if Bank.counter % 2 == 0:
                with thr_lock:
                    random_deposit = random.randint(50, 500)
                    self.balance += random_deposit
                    print(f"Пополнение: {random_deposit}. Баланс: {self.balance}")
                    if self.balance >= 500 and self.lock.locked():
                        self.lock.release()
                    sleep(0.001)
                    Bank.counter += 1

    def take(self):
        while Bank.counter <= 199:
            if Bank.counter % 2 == 1:
                with thr_lock:
                    random_take = random.randint(50, 500)
                    print(f"Запрос на {random_take}")
                    if self.balance >= random_take:
                        self.balance -= random_take
                        print(f'Снятие: {random_take}. Баланс: {self.balance}')
                    else:
                        print(f'Запрос отклонён, недостаточно средств')
                        if not self.lock.locked():
                            self.lock.acquire()
                sleep(0.001)
                Bank.counter += 1


bk = Bank()
th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')