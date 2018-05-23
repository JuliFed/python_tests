import unittest
from datetime import datetime
from mock import patch
from lesson_zadanie import Greeter


class TestGreeter(unittest.TestCase):
    def test_greet(self):
        test_str = 'Привет Вася'
        res = Greeter().greet('Вася')
        self.assertEqual(res, test_str)
        
    def test_greet_2(self):
        test_str = 'Привет Вася'
        res = Greeter().greet('   Вася  ')
        self.assertEqual(res, test_str)

    def test_greet_3(self):
        test_str = 'Привет Вася'
        res = Greeter().greet('вася')
        self.assertEqual(res, test_str)

    @patch('lesson_zadanie.datetime')
    def test_greet_4(self, mock_dt):
        mock_dt.now.return_value = datetime.strptime('2018-05-23 07:56:06.498238',"%Y-%m-%d %H:%M:%S.%f")
        test_str = 'Доброе утро Вася'
        res = Greeter().greet('Вася')
        self.assertEqual(res, test_str)

    @patch('lesson_zadanie.datetime')
    def test_greet_5(self, mock_dt):
        mock_dt.now.return_value = datetime.strptime('2018-05-23 20:56:06.498238',"%Y-%m-%d %H:%M:%S.%f")
        test_str = 'Добрый вечер Вася'
        res = Greeter().greet('Вася')
        self.assertEqual(res, test_str)

    @patch('lesson_zadanie.datetime')
    def test_greet_6(self, mock_dt):
        mock_dt.now.return_value = datetime.strptime('2018-05-23 00:56:06.498238', "%Y-%m-%d %H:%M:%S.%f")
        test_str = 'Доброй ночи Вася'
        res = Greeter().greet('Вася')
        self.assertEqual(res, test_str)

    @patch('lesson_zadanie.logging')
    def test_greet_7(self, mock_logger):
        res = Greeter().greet('Вася')
        mock_logger.warning.assert_called_with(res)


if __name__ == '__main__':
    unittest.main()