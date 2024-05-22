# 2. Работа со списками:
#   - Создайте переменную my_list и присвойте ей список из нескольких элементов, например, фруктов.
#   - Выведите на экран список my_list.
#   - Выведите на экран первый и последний элементы списка my_list.
#   - Выведите на экран подсписок my_list с третьего до пятого элементов.
#   - Измените значение третьего элемента списка my_list.
#   - Выведите на экран измененный список my_list.
#
# 3. Работа со словарями:
#   - Создайте переменную my_dict и присвойте ей словарь с парами ключ-значение, например,
#           переводами некоторых слов.
#   - Выведите на экран словарь my_dict.
#   - Выведите на экран значение для заданного ключа в my_dict.
#   - Измените значение для заданного ключа или добавьте новый в my_dict.
#   - Выведите на экран измененный словарь my_dict.
#  (strawberry клубника)   (raspberries малина ) (blackberry ежевика  )
#   (blueberry голубика )  ( cloudberry морошка ) ( cranberry клюква )
#   ( cowberry брусника )

my_list = ['strawberry', 'raspberries', 'blackberry','blueberry', 'cloudberry', 'cranberry']
print('Список: ', my_list)
print('Первый элемент списка: ', my_list[0])
print('Последний элемент списка: ', my_list[-1])
print('Подсписок с третьего по пятый элемент списка: ',my_list[2:5])
my_list.append('cowberry')
print('Измененный список: ', my_list)
my_dict = {'strawberry':'клубника', 'raspberries':'малина','blackberry':'ежевика',
           'blueberry':'голубика', 'cloudberry':'морошка', 'cranberry':'клюква'}
print('Словарь my_dict: ', my_dict)
translation_word = 'Перевод слова raspberries: ' + (my_dict.get('raspberries'))
print(translation_word)
my_dict['cowberry'] = 'брусника'
print('Измененный слоаврь: ', my_dict)
