import unittest
from unittest.mock import patch
from hash import hash_md5


class TestStringMethods(unittest.TestCase):
    @patch('hash.md5')
    def test_hash(self, mock_md5):
        hash_md5('SomeStr')
        mock_md5.assert_called_with('SomeStr'.encode())

    def test_stuff(self):
        self.assertEqual(2+2, 4)


if __name__ == '__main__':
    unittest.main()
