from utils import utils
import unittest


class TestCode(unittest.TestCase):

    def test_sort(self):
        self.assertEqual(len(utils.sort_by_date(6)), 6)

    def test_input(self):
        self.assertEqual(utils.right_input("6"), 6)
