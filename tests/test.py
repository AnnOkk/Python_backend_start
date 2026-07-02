from unittest import TestCase,main
from dz import MyArray


class Test(TestCase):
    def test_set_all(self):
        new_array = MyArray(5)
        new_array.set_all(1)
        self.assertEqual(new_array.get(0),1)
        self.assertEqual(new_array.get(1),1)
        self.assertEqual(new_array.get(2),1)

    def test_set(self):
        new_array = MyArray(5)
        new_array.set(0,1)
        self.assertEqual(new_array.get(0),1)
        new_array.set(3, 100)
        self.assertEqual(new_array.get(3),100)
        with self.assertRaises(IndexError):
            new_array.set(100,1)
    def test_get(self):
        new_array = MyArray(100)
        new_array.set_all(1)
        self.assertEqual(new_array.get(0),1)
        self.assertEqual(new_array.get(55),1)
        self.assertEqual(new_array.get(29),1)
        with self.assertRaises(IndexError):
            new_array.get(100)
    def test_version(self):
        new_array = MyArray(100)
        new_array.set_all(1)
        self.assertEqual(new_array.version,1)
        new_array.set_all(55)
        self.assertEqual(new_array.version,2)



if __name__ == '__main__':
    main()

