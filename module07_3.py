# Напишите класс WordsFinder, объекты которого создаются следующим образом:
# WordsFinder('file1.txt, file2.txt', 'file3.txt', ...).
# Объект этого класса должен принимать при создании неограниченного количество названий
# файлов и записывать их в атрибут file_names в виде списка или кортежа.
#
# Также объект класса WordsFinder должен обладать следующими методами:
# get_all_words - подготовительный метод, который возвращает словарь следующего вида:
# {'file1.txt': ['word1', 'word2'], 'file2.txt': ['word3', 'word4'], 'file3.txt': ['word5', 'word6', 'word7']}
# Где:
# 'file1.txt', 'file2.txt', ''file3.txt'' - названия файлов.
# ['word1', 'word2'], ['word3', 'word4'], ['word5', 'word6', 'word7'] - слова содержащиеся в этом файле.
# Алгоритм получения словаря такого вида в методе get_all_words:
# Создайте пустой словарь all_words.
# Переберите названия файлов и открывайте каждый из них, используя оператор with.
# Для каждого файла считывайте единые строки, переводя их в нижний регистр (метод lower()).
# Избавьтесь от пунктуации [',', '.', '=', '!', '?', ';', ':', ' - '] в строке.
# (тире обособлено пробелами, это не дефис в слове).
# Разбейте эту строку на элементы списка методом split(). (разбивается по умолчанию по пробелу)
# В словарь all_words запишите полученные данные, ключ - название файла, значение - список из слов этого файла.
#
# find(self, word) - метод, где word - искомое слово. Возвращает словарь, где ключ -
# название файла, значение - позиция первого такого слова в списке слов этого файла.
# count(self, word) - метод, где word - искомое слово. Возвращает словарь, где ключ -
# название файла, значение - количество слова word в списке слов этого файла.
# В методах find и count пользуйтесь ранее написанным методом get_all_words для получения
# названия файла и списка его слов.
# Для удобного перебора одновременно ключа(названия) и значения(списка слов) можно
# воспользоваться методом словаря - item().
#
# for name, words in get_all_words().items():

import re
# from pprint import pprint


class WordsFinder():
    def __init__(self, *text_files):
        list_files_txt = []
        extension = ".txt"
        for txt_file in text_files:
            if txt_file.endswith(extension):
                list_files_txt.append(txt_file)
            else:
                print("Файл {} не имеет правильного формата".format(txt_file))
        if len(list_files_txt) > 0:
            self.file_names = list_files_txt
        else:
            print('Во веденном списке отсутствуют файлы типа txt')

    def get_all_words(self):
        all_words = {}
        delimiters = r"[',', '.', '=', '!', '?', ';', ':', ' - ', '\n']"
        for file_ in self.file_names:
            with open(file_, mode='r', encoding='utf-8') as file:
                string_whole_file = file.read().lower()
                list_from_file = re.split(delimiters, string_whole_file)
                all_words[file_] = list_from_file
        return all_words

    def find(self, word):
        dict_word_in_files = {}
        word_lower = word.lower()
        for name, words in self.get_all_words().items():
            for i in range(len(words)):
                if words[i] == word_lower:
                    dict_word_in_files[name] = i + 1
                    break
        if len(dict_word_in_files) == 0:
            print('Искомое слово отсутствует в текстовых файлах')
            return
        else:
            return dict_word_in_files

    def count(self, word):
        word_lower = word.lower()
        dict_count_word_in_files = {}
        for name, words in self.get_all_words().items():
            count = 0
            for i in range(len(words)):
                if words[i] == word_lower:
                    count += 1
            if count > 0:
                dict_count_word_in_files[name] = count
        if len(dict_count_word_in_files) == 0:
            print('Искомое слово отсутствует в текстовых файлах')
            return
        else:
            return dict_count_word_in_files


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего

# finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
#                       'Rudyard Kipling - If.txt',
#                       'Mother Goose - Monday’s Child.txt')
# pprint(finder1.get_all_words())
# print(finder1.find('the'))
# print(finder1.count('the'))
