# ## ***Write generic class MyArray\[T\] with the following methods**
#
# - ***constructor taking amount of items (It may be very huge for example 1000000000)**
#
# - ***setAll - sets in all items the same given value**
#
# - ***set - sets a given value at a given index (index may be ether 0 or any positive number less than amount of items), raises IndexError exception if the index greater or equal the amount or less than 0**
#
# - ***get - returns the value at a given index (index may be ether 0 or any positive number less than amount of items), raises IndexError exception if the index greater or equal the amount or less than 0**
#
# ## ***Note all the above methods should have complexity O\[1\]**
#
# ## ***Write tests for class MyArray\[int\]**


class MyArray[T]:
    def __init__(self, amount,default_value=None):
        self.default_dict = {}
        self.amount = amount
        self.default_value = default_value


    def set_all(self,value):
        self.default_value = value #?
        self.default_dict = {}

    def set(self,key,value):
        if 0 <= key < self.amount:
            self.default_dict[key] = value
        else:
            raise IndexError

    def get(self,key):
        if  0 <= key < self.amount :
            if key in self.default_dict:
                return self.default_dict[key]
            else:return self.default_value
        else:
            raise IndexError










