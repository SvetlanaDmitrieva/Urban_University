# Необходимо реализовать 2 класса Product и Shop, с помощью которых будет производиться запись
# в файл с продуктами.
# Объекты класса Product будут создаваться следующим образом - Product('Potato', 50.0, 'Vagetables')
# и обладать следующими свойствами:
# Атрибут name - название продукта (строка).
# Атрибут weight - общий вес товара (дробное число) (5.4, 52.8 и т.п.).
# Атрибут category - категория товара (строка).
# Метод __str__, который возвращает строку в формате '<название>, <вес>, <категория>'.
# Все данные в строке разделены запятой с пробелами.
#
# Объекты класса Shop будут создаваться следующим образом - Shop() и обладать следующими свойствами:
# Инкапсулированный атрибут __file_name = 'products.txt'.
# Метод get_products(self), который считывает всю информацию из файла __file_name, закрывает его
# Метод add(self, *products), который принимает неограниченное количество объектов класса Product.
# Добавляет в файл __file_name каждый продукт из products, если его ещё нет в файле (по названию).
# Если такой продукт уже есть, то не добавляет и выводит строку 'Продукт <название> уже есть в магазине' .

class Product():
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return self.name + ', ' + str(self.weight) + ', ' + self.category


class Shop():
    __file_name = 'products.txt'

    def get_products(self):
        with open(self.__file_name, mode = 'r') as file:
            if file.readable():
                print(file.read())
                return
            print(f'Прочесть {self.__file_name} невозможно')
            return

    def add(self, *products):
        with open(self.__file_name, mode='a+') as file:
            for product in products:
                file.seek(0)
                name_product = product.name
                fl = 0
                for item in file:
                    words = item.split(', ')
                    if words[0] == name_product:
                        print(f'Продукт {name_product} уже есть в магазине')
                        fl = 1
                        break
                if fl == 0:
                    str_product = product.name + ', ' + str(product.weight) + ', ' + product.category + " \n"
                    file.write(str_product)


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())