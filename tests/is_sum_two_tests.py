from unittest import TestCase, main
from is_sum_two import is_sum_two

class TestIsSumTwo(TestCase):
    def setUp(self):
        self.numbers = [1,2,3,4,5]
    def test_is_sum_two(self):
        self.assertEqual(True,is_sum_two(self.numbers,6))
        self.assertEqual(True,is_sum_two(self.numbers,7))
        self.assertEqual(True,is_sum_two(self.numbers,8))
        self.assertEqual(True,is_sum_two(self.numbers,9))
    def test_is_not_sum_two(self):
        self.assertEqual(False,is_sum_two(self.numbers,15) )
        self.assertEqual(False,is_sum_two(self.numbers,16) )
        self.assertEqual(False,is_sum_two(self.numbers,-17) )

if __name__ == '__main__':
    main()