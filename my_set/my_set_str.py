from my_set import MySet

set_of_str = MySet()
set_of_str.add("one")
set_of_str.add("two")
set_of_str.add("one")
print("one" in set_of_str)
print("three" in set_of_str)
for string in set_of_str:
    print(string)