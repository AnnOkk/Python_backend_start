from unittest import TestCase,main
from my_set.my_set import MySet


class MySetTest(TestCase):
    def setUp(self):
        self.my_set = MySet()

    def test_init(self):
        self.assertEqual(self.my_set.capacity,16)
        self.assertEqual(self.my_set.load_factor,0.75)
        self.assertEqual(self.my_set.size,0)

    def test_len(self):
        self.assertEqual(len(self.my_set),0)
        self.my_set.add(10)
        self.assertEqual(len(self.my_set),1)

    def test_iter(self): #?
        self.my_set.add(10)
        self.my_set.add(20)
        res = list(self.my_set)

        self.assertIn(10,res)
        self.assertIn(20,res)
        self.assertEqual(2,len(res))

    def test_add_new(self):
        self.assertTrue(self.my_set.add(10))
        self.assertIn(10,self.my_set)
        self.assertEqual(1,len(self.my_set))
    def test_add_existing(self):
        self.assertTrue(self.my_set.add(10))
        self.assertFalse(self.my_set.add(10))
        self.assertEqual(1,len(self.my_set))

    def test_remove_existing(self):
        self.my_set.add(10)
        self.assertTrue(self.my_set.remove(10))
        self.assertNotIn(10,self.my_set)
        self.assertEqual(0,len(self.my_set))

    def test_remove_non_existing(self):
        self.assertFalse(self.my_set.remove(10))
        self.assertEqual(0,len(self.my_set))

    def test_contains(self):
        self.my_set.add(10)
        self.assertTrue(10 in self.my_set)
        self.assertFalse(20 in self.my_set)

    def test_get_bucket_index(self): # actually you do not need to control a private method
        my_set1 = MySet(6,0.75)
        capacity = my_set1.capacity
        self.assertEqual(hash(10) % capacity,my_set1._get_bucket_index(10))
        self.assertEqual(hash(17) % capacity,my_set1._get_bucket_index(17))


    def test_resize(self): #?
        my_set2 = MySet(2,0.75)
        my_set2.add(10)
        my_set2.add(20)

        self.assertIn(10,my_set2)
        self.assertIn(20,my_set2)
        self.assertEqual(2,len(my_set2))
        self.assertEqual(2,my_set2.capacity)#?





if __name__ == '__main__':
    main()