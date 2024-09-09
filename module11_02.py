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

class Introspection_info:

    def __init__(self, name):
        self.name = name
        self.type = self.get_type()
        self.attributes = self.get_attributes()
        self.methods = self.get_methods()
        self.module = self.get_module()

    def get_type(self):
        return type(self.name)

    def get_attributes(self):
        return dir(self.name)

    def get_methods(self):
        methods = [meth for meth in self.attributes if callable(getattr(self.name, meth))]
        return methods

    def get_module(self):
        return self.name.__class__.__module__

    def __str__(self):
        return (f'name : {self.name} \ntype: {self.type}\nattributes : {self.attributes} \n'
                f'methods: {self.methods} \nmodule : {self.module}')


number_info = Introspection_info(42)
print(number_info)

number_info = Introspection_info((1,2,3))
print(number_info)

number_info = Introspection_info(abs)
print(number_info)

number_info = Introspection_info([1,2,3])
print(number_info)

number_info = Introspection_info(list)
print(number_info)

number_info = Introspection_info(sorted)
print(number_info)

number_info = Introspection_info(Introspection_info)
print(number_info)


