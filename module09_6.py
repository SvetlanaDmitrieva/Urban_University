# Напишите функцию-генератор all_variants(text), которая принимает строку text и возвращает
# объект-генератор, при каждой итерации которого будет возвращаться подпоследовательности переданной строки.
#
# Пункты задачи:
# Напишите функцию-генератор all_variants(text).
# Опишите логику работы внутри функции all_variants.
# Вызовите функцию all_variants и выполните итерации.


def all_variants(text):
    len_text = len(text)
    for i in range(len_text):
        for j in range(len_text - i):
            str_txt = text[j:j+i+1:1]
            yield str_txt


a = all_variants("abcdef")
for i in a:
    print(i)