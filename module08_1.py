# Реализуйте следующую функцию:
# add_everything_up, будет складывать числа(int, float) и строки(str)
#
# Описание функции:
# add_everything_up(a, b) принимает a и b, которые могут быть как числами(int, float), так и строками(str).
# TypeError - когда a и b окажутся разными типами (числом и строкой), то возвращать строковое
# представление этих двух данных вместе (в том же порядке). Во всех остальных случаях выполнять
# стандартные действия.

def add_everything_up(number_01 = None, number_02 = None):
    try:
        sum_numbers = number_01 + number_02
    except TypeError as exc:
        if not (number_01 and number_02):
            f_string = f'Отсутствует по крайней мере 1 аргумент - {exc} :{number_01} {number_02}'
        else:
            f_string = f"{number_01} {number_02}"
    else:
        f_string = sum_numbers
    return f_string


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
print(add_everything_up(12))
print(add_everything_up())
