import unittest
import mock
from unittest.mock import patch


def hash_md5():
    from hashlib import md5
    return md5('SomeClass'.encode())


class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

    def test_profile(self):
        profile = mock.Mock(first_name='Ivan')
        print(profile.first_name)
        profile.balance.return_value=15
        print(profile.balance())
        profile.balance.side_effect = Exception("Some error")
        print(profile.balance())

    @patch('hashlib.md5')
    def test_profile(self, mock_md5):
        mock_md5.return_value = 'Some_hash'

        hash_md5()

        mock_md5.assert_called_with('SomeClass'.encode())
        print(mock_md5.calls)


if __name__ == '__main__':
    unittest.main()