# Напишите 2 функции:
# Функция, которая складывает 3 числа (sum_three)
# Функция декоратор (is_prime), которая распечатывает "Простое", если результат 1ой функции будет
# простым числом и "Составное" в противном случае.


from functools import reduce


def is_prime(func):
    def wrapper(*args):
        summ_numbers = func(*args)
        k = 0
        for i in range(2, summ_numbers // 2 + 1):
            if summ_numbers % i == 0:
                k = k + 1
                break
        if (k <= 0):
            print("Простое")
        else:
            print("Составное")
        return summ_numbers
    return wrapper


@is_prime
def sum_three(*args):
    numbers_list = list(args)
    summ = reduce((lambda x, y: x + y), numbers_list)
    return summ


result = sum_three(5, 6, 7, 8, 9)
print(result)
