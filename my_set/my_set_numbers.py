from my_set import MySet

set_of_numbers = MySet()
set_of_numbers.add(10)
set_of_numbers.add(20)
set_of_numbers.add(10)
print(10 in set_of_numbers)
print(30 in set_of_numbers)

print(len(set_of_numbers))

for number in set_of_numbers:
    print(number)