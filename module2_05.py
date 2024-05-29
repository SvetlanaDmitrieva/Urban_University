# Напиши функцию get_matrix с тремя параметрами n, m и value, которая будет создавать матрицу
# (вложеный список) размерами n строк и m столбцов, заполненную значениями value и возвращать
# эту матрицу в качестве результата работы.
#
# Пункты задачи:
# Объявите функцию get_matrix и напишите в ней параметры n, m и value.
# Создайте пустой список matrix внутри функции get_matrix.
# Напишите первый(внешний) цикл for для кол-ва строк матрицы, n повторов.
# В первом цикле добавляйте пустой список в список matrix.
# Напишите второй(внутренний) цикл for для кол-ва столбцов матрицы, m повторов.
# Во втором цикле пополняйте ранее добавленный пустой список значениеми value.
# После всех циклов верните значение переменной matrix.
# Выведите на экран(консоль) результат работы функции get_matrix.
def get_matrix(n, m, value):
    matrix = []
    for i in range(0, n):
        sub = []
        for j in range(0, m):
            sub.append(value)
        matrix.append(sub)
    return matrix

result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)

