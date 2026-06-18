import unittest
from unittest import TestCase, main
from max_negative_repr import max_negative_repr


class TestMaxNegativeRepr(TestCase):
    def setUp(self):
        self.numbers = [100, 4, 1, -1, -4, -100]
    def test_max_negative_repr(self):
        self.assertEqual(100,max_negative_repr([100, 4, 1, -1, -4, -100]),'found it')
        self.assertEqual(4,max_negative_repr([100, 4, 1, -1, -4, 200]),'found it')
        self.assertEqual(1, max_negative_repr([100, 4, 1, -1, -44, 100]), 'found it')
    def test_not_found_max_negative_repr(self):
        self.assertEqual(-1,max_negative_repr([100, 4, 1, -11, -444, 100]),'not found it')
        self.assertEqual(-1,max_negative_repr([100, 4, 1, 1, -44, 1000]))

if __name__ == '__main__':
    main()
