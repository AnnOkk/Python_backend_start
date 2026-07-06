from unittest import TestCase,main
from main import Fibonacci


class TestFibo(TestCase):
    def test_fibonacci(self):
        fibonacci = Fibonacci(10)
        self.assertEqual(list(fibonacci), [1, 1, 2, 3, 5, 8, 13, 21, 34, 55])
        fibonacci = Fibonacci(20)
        self.assertEqual(list(fibonacci), [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765])


    def test_one_number(self):
        fib = Fibonacci(1)
        self.assertEqual([1], list(fib))

    def test_two_numbers(self):
        fib = Fibonacci(2)
        self.assertEqual([1, 1], list(fib))



if __name__ == '__main__':
    main()