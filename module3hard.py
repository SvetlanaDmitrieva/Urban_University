# Все ученики урбана, без исключения, - очень умные ребята. Настолько умные, что иногда
# по утру сами путаются в том, что намудрили вчера вечером.
# Один из таких учеников уснул на клавиатуре в процессе упорной учёбы (ещё и трудолюбивые).
# Тем не менее, даже после сна, его код остался рабочим и выглядел следующим образом:
#
# data_structure = [
#     [1, 2, 3],
#     {'a': 4, 'b': 5},
#     (6, {'cube': 7, 'drum': 8}),
#     "Hello",
#     ((), [{(2, 'Urban', ('Urban2', 35))}])
# ]
# Увидев это студент задался вопросом: "А есть ли универсальное решение для подсчёта суммы
# всех чисел и длин всех строк?"
# Да, выглядит страшно, да и обращаться нужно к каждой внутренней структуре (списку, словарю
# и т.д.) по разному.
# Ученику пришлось каждый раз использовать индексацию и обращение по ключам -
# универсального  для таких структур он не нашёл.
def calculate_structure_sum(list_number):
    if '+' in list_number:
        index_n_ = list_number.index('+')
        list_number[index_n_ - 1] = str(int(list_number[index_n_ - 1]) + int(list_number[index_n_ + 1]))
        del list_number[index_n_]
        del list_number[index_n_]
        calculate_structure_sum(list_number)
        if len(list_number) == 1:
            result_1 = int(list_number[0])
            return result_1


data_structure = [[1, 2, 3], {'a': 4, 'b': 5},
                  (6, {'cube': 7, 'drum': 8}), "Hello", ((), [{(2, 'Urban', ('Urban2', 35))}])]
list_data_structure = str(data_structure)
new_list = (((list_data_structure.replace('[', '').replace(']', '')
              .replace('{', '').replace('}', '').replace('(', '')
              .replace(')', '').replace(':', '+')).replace(',', '+')
              .replace(' ', '')).replace('++', '+')
              .replace('+', ' + ').split())
new_list_2 = list()
for str_ in new_list:
    if "'" in str_:
        new_list_2.append(str(len(str_) - 2))
    else:
        new_list_2.append(str_)
result = calculate_structure_sum(new_list_2)
print("Сумма всех чисел и длин всех строк: ", result)
