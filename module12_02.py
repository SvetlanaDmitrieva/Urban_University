# В первую очередь скачайте исходный код, который нужно обложить тестами с GitHub. (Можно скопировать)
# В этом коде сможете обнаружить дополненный с предыдущей задачи класс Runner и новый класс Tournament.
# Изменения в классе Runner:
# Появился атрибут speed для определения скорости бегуна.
# Метод __eq__ для сравнивания имён бегунов.
# Переопределены методы run и walk, теперь изменение дистанции зависит от скорости.
# Класс Tournament представляет собой класс соревнований, где есть дистанция, которую нужно пробежать и
# список участников. Также присутствует метод start, который реализует логику бега по предложенной дистанции.
#
# Напишите класс TournamentTest, наследованный от TestCase. В нём реализуйте следующие методы:
#
# setUpClass - метод, где создаётся атрибут класса all_results. Это словарь в который будут сохраняться
# результаты всех тестов.
# setUp - метод, где создаются 3 объекта:
# Бегун по имени Усэйн, со скоростью 10.
# Бегун по имени Андрей, со скоростью 9.
# Бегун по имени Ник, со скоростью 3.
# tearDownClass - метод, где выводятся all_results по очереди в столбец.
#
# Так же методы тестирования забегов, в которых создаётся объект Tournament на дистанцию 90. У объекта
# класса Tournament запускается метод start, который возвращает словарь в переменную all_results. В конце
# вызывается метод assertTrue, в котором сравниваются последний объект из all_results (брать по наибольшему
# ключу) и предполагаемое имя последнего бегуна.
# Напишите 3 таких метода, где в забегах участвуют (порядок передачи в объект Tournament соблюсти):
# Усэйн и Ник
# Андрей и Ник
# Усэйн, Андрей и Ник.
# Как можно понять: Ник всегда должен быть последним.
#
# Дополнительно (не обязательно, не влияет на зачёт):
# В данной задаче, а именно в методе start класса Tournament, допущена логическая ошибка. В результате его
# работы бегун с меньшей скоростью может пробежать некоторые дистанции быстрее, чем бегун с большей.
# Попробуйте решить эту проблему и обложить дополнительными тестами.


import unittest
from runner_and_tournament import Runner, Tournament


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = list()

    def setUp(self):
        self.runner_1 = Runner('Усэйн', 10)
        self.runner_2 = Runner('Андрей', 9)
        self.runner_3 = Runner('Ник', 3)

    def test_tournament_01(self):
        tournament_1 = Tournament(90, self.runner_1, self.runner_3)
        TournamentTest.all_results.append(tournament_1.start())
        self.assertTrue(TournamentTest.all_results[-1][2] == self.runner_3)

    def test_tournament_02(self):
        tournament_2 = Tournament(90, self.runner_2, self.runner_3)
        TournamentTest.all_results.append(tournament_2.start())
        self.assertTrue(TournamentTest.all_results[-1][2] == self.runner_3)

    def test_tournament_03(self):
        tournament_3 = Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        TournamentTest.all_results.append(tournament_3.start())
        self.assertTrue(TournamentTest.all_results[-1][3] == self.runner_3)

    def test_tournament_04(self):
        if self.prepare_test4() != self.runner_3:
            with self.assertRaises(Exception):
                self.prepare_test4()
        else:
            self.assertTrue(self.prepare_test4() == self.runner_3)

    def prepare_test4(self):
        tournament_4 = Tournament(81, self.runner_3, self.runner_2, self.runner_1)
        TournamentTest.all_results.append(tournament_4.start())
        last_runner = TournamentTest.all_results[-1][3]
        second_runner =  TournamentTest.all_results[-1][2]
        if last_runner != self.runner_3: 
            raise Exception(f'Самый медленный {self.runner_3} должен быть на 3-м месте, а не {last_runner} ')
        elif second_runner != self.runner_2:
            raise Exception(f'Вторым должен быть {self.runner_2}, а не {second_runner} ')
        else:
            return  self.runner_3

    @classmethod
    def tearDownClass(cls):
        for test in cls.all_results:
            print(test)

    if __name__ == "__main__":
        unittest.main()