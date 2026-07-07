from unittest import TestCase,main

from main import LfuDictCache


class TestDictCache(TestCase):
    def test_dict_cache(self):
        cache = LfuDictCache(2)
        cache['A'] = 100
        cache['B'] = 200

        assert len(cache) == 2
        assert cache['A'] == 100
        assert cache['B'] == 200

    def test_dict_cache_delete(self):
        cache = LfuDictCache(2)
        cache['A'] = 100
        cache['B'] = 200
        cache['A']
        cache['C'] = 300
        with self.assertRaises(KeyError):
            cache['B']
        self.assertEqual(cache['A'], 100)
        self.assertEqual(cache['C'], 300)


    def test_dict_cache_eq_frequency(self):
        cache = LfuDictCache(2)
        cache['A'] = 100
        cache['B'] = 200
        cache['C'] = 300
        with self.assertRaises(KeyError):
            cache['A']
        self.assertEqual(cache['B'], 200)
        self.assertEqual(cache['C'], 300)





if __name__ == '__main__':
    main()