# Необходимо создать функцию wite_words(word_count, file_name), где word_count - количество
# записываемых слов, file_name - название файла, куда будут записываться слова.
# Функция должна вести запись слов "Какое-то слово № <номер слова по порядку>" в соответствующий
# файл с прерыванием после записи каждого на 0.1 секунду.
# Сделать паузу можно при помощи функции sleep из модуля time, предварительно импортировав
# её: from time import sleep.
# В конце работы функции вывести строку "Завершилась запись в файл <название файла>".
#
# После создания файла вызовите 4 раза функцию wite_words, передав в неё следующие значения:
# 10, example1.txt
# 30, example2.txt
# 200, example3.txt
# 100, example4.txt
# После вызовов функций создайте 4 потока для вызова этой функции со следующими аргументами
# для функции:
# 10, example5.txt
# 30, example6.txt
# 200, example7.txt
# 100, example8.txt
# Запустите эти потоки методом start не забыв, сделать остановку основного потока при помощи join.
# Также измерьте время затраченное на выполнение функций и потоков. Как это сделать рассказано
# в лекции к домашнему заданию.


from time import sleep
from datetime import datetime
from threading import Thread


def wite_words(word_count, file_name):
    with open(file_name, 'w') as f_n:
        for i in range(1, word_count + 1):
            f_n.write('Какое-то слово № '+ str(i) +'\n')
            sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')
    return


time_start = datetime.now()
wite_words(10, 'example1.txt')
wite_words(30, 'example2.txt')
wite_words(200, 'example3.txt')
wite_words(100, 'example4.txt')
time_end = datetime.now()
print('Работа потоков ',time_end - time_start)

time_start = datetime.now()
thr_first = Thread(target= wite_words, args = (10, 'example5.txt'))
thr_second = Thread(target= wite_words, args = (30, 'example6.txt'))
thr_third = Thread(target= wite_words, args = (200, 'example7.txt'))
thr_fourth = Thread(target= wite_words, args = (100, 'example8.txt'))

thr_first.start()
thr_second.start()
thr_third.start()
thr_fourth.start()

thr_first.join()
thr_second.join()
thr_third.join()
thr_fourth.join()

time_end = datetime.now()
print('Работа потоков ',time_end - time_start)