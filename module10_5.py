# Задача "Многопроцессное считывание":
# Необходимо считать информацию из нескольких файлов одновременно, используя многопроцессный подход.
# Подготовка:
# Скачайте архив с файлами для считывания данных и распакуйте его в проект для дальнейшего использования.
# Выполнение:
# Создайте функцию read_info(name), где name - название файла. Функция должна:
# Создавать локальный список all_data.
# Открывать файл name для чтения.
# Считывать информацию построчно (readline), пока считанная строка не окажется пустой.
# Во время считывания добавлять каждую строку в список all_data.
# Этих операций достаточно, чтобы рассмотреть преимущество многопроцессного выполнения программы над линейным.
# Создайте список названий файлов в соответствии с названиями файлов архива.
# Вызовите функцию read_info для каждого файла по очереди (линейно) и измерьте время
# выполнения и выведите его в консоль.
# Вызовите функцию read_info для каждого файла, используя многопроцессный подход: контекстный
# менеджер with и объект Pool. Для вызова функции используйте метод map, передав в него
# функцию read_info и список названий файлов. Измерьте время выполнения и выведите его в консоль.


from multiprocessing import Pool
from time import sleep
from datetime import datetime


def read_info(name):
    all_data = []
    with open(name, 'r') as f_n:
        while True:
            line = f_n.readline()
            if not line:
                break
            all_data.append(line)


if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]
# # Линейный вызов
#     start = datetime.now()
#     for file in filenames:
#         read_info(file)
#     end = datetime.now()
#     print(f'Линейный вызов: {end - start}')
# Многопроцессный
    start = datetime.now()  
    with Pool(4) as pool:
        pool.map(read_info, filenames)
    end = datetime.now()
    print(f'Многопроцессный вызов: {end - start}')

