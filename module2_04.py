# Дан список чисел  numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# Испольуя этот список составьте второй список primes содержащий только простые числа.
# А так же третий список not_primes, содержащий все не простые числа.
# Выведите списки primes и not_primes на экран(в консоль).
# Пункты задачи:
# Создайте пустые списки primes и not_primes.
# При помощи цикла for переберите список numbers.
# Напишите ещё один цикл for (вложенный), где будут подбираться делители для числа из 1ого цикла.
# Отметить простоту числа можно переменной is_prime, записав в неё значение True перед проверкой.
# В процессе проверки на простоту записывайте числа из списка numbers в списки primes и not_primes
# в зависимости от значения перменной is_prime после проверки (True - в prime, False - в not_prime).
# Выведите списки primes и not_primes на экран(в консоль).
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = list()
not_primes = list()
for i in range(1, len(numbers)):
    is_prime = True
    for j in range(1, i):
        if numbers[i] % numbers[j] == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(numbers[i])
    else:
        not_primes.append(numbers[i])
print('Список простых чисел: ', primes)
print('Список непростых чисел: ', not_primes)
