# Создайте новую функцию def test_function
# Создайте другую функцию внутри функции inner_function, функция должна печатать значение
# "Я в области видимости функции test_function"
# Вызовите функцию inner_function внутри функции test_function
# Попробуйте вызывать inner_function вне функции test_function и посмотрите на результат
# выполнения программы
# Полученный код напишите в ответ к домашему заданию

def test_function():
    # nonlocal inner_function
    def inner_function():
        print('Я в области видимости функции test_function')
        return
    inner_function()
    return
inner_function()    # ошибка: NameError: name 'inner_function' is not defined.
                    # Did you mean: 'test_function'?
# test_function()   # выводит на печать строку: 'Я в области видимости функции test_function'