# Необходимо создать функцию, которая принимает объект (любого типа) в качестве аргумента
# и проводит интроспекцию этого объекта, чтобы определить его тип, атрибуты, методы, модуль,
# и другие свойства.
#
# 1. Создайте функцию introspection_info(obj), которая принимает объект obj.
# 2. Используйте встроенные функции и методы интроспекции Python для получения информации о переданном объекте.
# 3. Верните словарь или строки с данными об объекте, включающий следующую информацию:
#   - Тип объекта.
#   - Атрибуты объекта.
#   - Методы объекта.
#   - Модуль, к которому объект принадлежит.
#   - Другие интересные свойства объекта, учитывая его тип (по желанию).


def introspection_info(obj):

    info = {}
    if hasattr(obj, '__name__'):
        info['name'] = obj.__name__
    info['type'] = type(obj).__name__

    attributes = [attribute
                  for attribute in dir(obj)
                  if not callable(getattr(obj, attribute))]
    info['attributes'] = attributes
    methods = [method for method in dir(obj)
               if callable(getattr(obj, method))]
    info['methods'] = methods
    info['module'] = getattr(obj, '__module__', __name__)

    return info


class OneClass:
    def __init__(self, *arg):
        self.value = arg

    def one_method(self):
        pass


number_info = introspection_info(42)
print(number_info)

number_info = introspection_info((1, 2, 3))
print(number_info)

number_info = introspection_info(abs)
print(number_info)

number_info = introspection_info([1, 2, 3])
print(number_info)

number_info = introspection_info(list)
print(number_info)

number_info = introspection_info(sorted)
print(number_info)

number_info = introspection_info(OneClass)
print(number_info)

class_instance = OneClass(10)
number_info = introspection_info(class_instance)
print(number_info)


