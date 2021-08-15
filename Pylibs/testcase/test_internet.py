import unittest
from internet.jsonEx import get_json_value
from grammar.context import ExceptionCapture


class MyTestCase(unittest.TestCase):
    def test_something(self):
        exc_list = []
        with ExceptionCapture(exc_list):
            t1 = {'a': 13}
            t2 = {'b': 32}
            t3 = [t1]
            t4 = [t2, t1]
            self.assertEqual(13, get_json_value('a', t1))
            self.assertEqual(13, get_json_value('a', t2))
            self.assertEqual(13, get_json_value('a', t3))
            self.assertEqual(13, get_json_value('a', t4))
        with ExceptionCapture(exc_list, True):
            pass


if __name__ == '__main__':
    unittest.main()
