from sum_two_tests.sum_two import is_sum_two2
from unittest import TestCase, main




class TestIsSumTwo(TestCase):
    def setUp(self):
        self.numbers = [100, -40, 80, 1, 3, 10]


    def test_exist_positive_sum(self):
        self.assertTrue(is_sum_two2(self.numbers, 11))
        self.assertTrue(is_sum_two2(self.numbers, 110))
        self.assertTrue(is_sum_two2(self.numbers, 60))


    def test_exist_negative_sum(self):
        self.assertTrue(is_sum_two2(self.numbers, -37))
        self.assertTrue(is_sum_two2(self.numbers, -30))


    def test_not_exist_positive_sum(self):
        self.assertFalse(is_sum_two2(self.numbers, 5))
        self.assertFalse(is_sum_two2(self.numbers, 80))


    def test_not_exist_negative_sum(self):
        self.assertFalse(is_sum_two2(self.numbers, -40))
        self.assertFalse(is_sum_two2(self.numbers, -20))




if __name__ == "__main__":
    main()
