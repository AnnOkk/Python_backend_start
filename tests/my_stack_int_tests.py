from unittest import TestCase,main
from main import MyStackInt


class MyStackTests(TestCase):
    def test_push(self):
        self.my_stack = MyStackInt()
        self.my_stack.push(1)
        self.my_stack.push(2)
        self.my_stack.push(3)
        self.assertEqual(self.my_stack.stack, [1,2,3])

    def test_pop(self):
        self.my_stack = MyStackInt()
        with self.assertRaises(IndexError):
            self.my_stack.pop()
        self.my_stack.push(1)
        self.my_stack.push(2)
        self.my_stack.push(3)
        self.assertEqual(self.my_stack.pop(), 3)


    def test_max(self):
        self.my_stack = MyStackInt()
        with self.assertRaises(IndexError):  #expected error
            self.my_stack.max()
        self.my_stack.push(1)
        self.my_stack.push(2)
        self.my_stack.push(3)
        self.assertEqual(self.my_stack.max(), 3)

        self.my_stack.push(4)
        self.my_stack.push(1)
        self.assertEqual(self.my_stack.max(), 4)

    def test_max_after_pop(self):
        self.my_stack = MyStackInt()

        self.my_stack.push(1)
        self.my_stack.push(8)
        self.my_stack.push(9)
        self.my_stack.push(1)

        self.assertEqual(9, self.my_stack.max())

        self.my_stack.pop()
        self.assertEqual(9, self.my_stack.max())

        self.my_stack.pop()
        self.assertEqual(8, self.my_stack.max())




if __name__ == '__main__':
    main()