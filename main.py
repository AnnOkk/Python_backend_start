from collections import OrderedDict
from typing import Hashable, Generic, Iterator, TypeVar
from sortedcontainers import SortedDict

K = TypeVar('K', bound=Hashable)
V = TypeVar("V")


####################################################################################

class DictCache(OrderedDict[K, V]):
    def __init__(self, maxsize=128):
        super().__init__()  # calls constructor of OrderedDict that has all methods for keeping insertion order
        self.maxsize = maxsize

    # The  methods __getitem__ and __setitem__ should be overriden
    # Assumption: only following methods should be overriden for making tests from test_dict_cache.py passed
    # Hints as follows:
    # super().__getitem__(key) calls method __getitem__ of OrderedDict
    # super().__setitem__(key, value) calls method __setitem__ of OrderedDict
    # consider using self.move_to_end(key) of OrderedDict for making item with the given key as most recent
    # consider using self.popitem(last=False) for removing least recent (eldest item)

    def __getitem__(self, key) -> V:
        res = super().__getitem__(key)
        self.move_to_end(key)
        return res

    def __setitem__(self, key, value):
        super().__setitem__(key, value)
        self.move_to_end(key)
        if len(self) > self.maxsize:
            self.popitem(last=False)


class LfuDictCache(Generic[K, V]):
    def __init__(self, max_size: int):
        # TODO write constructor for defining encapsulated data structure
        self.max_size = max_size
        self.data = {}
        self.counter = 0
        self.frequency = {}  # for each key, how many times it was accessed
        self.last_used = {}  # for each key, when it was accessed last time
        self.sorted_keys = SortedDict()

    def __getitem__(self, key: K) -> V:
        # TODO method for square braces operator [] getting key and returning value with throwing
        # KeyError exception if key is missing
        if key not in self.data:
            raise KeyError()
        value = self.data[key]
        self.counter += 1
        self.frequency[key] += 1
        self.last_used[key] = self.counter
        return value

    def __setitem__(self, key: K, value: V):
        # TODO method for square braces operator [] either updating existing key-value association or adding a new one
        if key in self.data:
            self.data[key] = value
            self.counter += 1
            self.frequency[key] += 1
            self.last_used[key] = self.counter

        elif key not in self.data and len(self.data) < self.max_size:
            self._initialize_new_key(key, value)
        elif len(self.data) == self.max_size:
            candidate = None
            for k in self.last_used:
                if candidate is None:
                    candidate = k
                elif self.frequency[k] < self.frequency[candidate]:
                    candidate = k
                elif self.frequency[k] == self.frequency[candidate] and self.last_used[k] < self.last_used[candidate]:
                    candidate = k
            self.__delitem__(candidate)
            self._initialize_new_key(key, value)  # !!

    def __delitem__(self, key: K):
        # TODO method for deleting key-value association from a dictionary with throwing KeyError exception
        # in the case of missing key like del dict[key]
        if key not in self.data:
            raise KeyError()
        del self.data[key]
        del self.frequency[key]
        del self.last_used[key]

    def __iter__(self) -> Iterator[K]:
        # TODO method for iterating keys in arbitrary order
        return iter(self.data)

    # after doing sorted_keys must be return iter(self.sorted_keys)

    def __len__(self) -> int:
        # TODO method returning number of key-value associations (pairs)
        return len(self.data)

    def _initialize_new_key(self, key: K, value: V):
        self.data[key] = value
        self.counter += 1
        self.frequency[key] = 1
        self.last_used[key] = self.counter
