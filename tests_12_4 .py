from rt_with_exceptions import Runner
import unittest
import logging

logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='utf-8',
                    format='%(asctime)s --%(name)s - %(levelname)s - %(message)s')


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            runner_1 = Runner('Иван', -5)
            if runner_1.speed > 0:
                logging.info(f'"test_walk" выполнен успешно')
            for _ in range(10):
                runner_1.walk()
            self.assertEqual(runner_1.distance, 50)
        except ValueError:
            logging.warning("Неверная скорость для Runner")

    def test_run(self):
        try:
            runner_2 = Runner(12345, 5)
            if isinstance(runner_2.name, str):
                logging.info('"test_run" выполнен успешно')
            for _ in range(10):
                runner_2.run()
            self.assertEqual(runner_2.distance, 100)
        except TypeError:
            logging.warning("Неверный тип данных для объекта Runner")

    if __name__ == "__main__":
        unittest.main()
