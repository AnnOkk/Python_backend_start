from sortedcontainers import SortedList,SortedKeyList
#O(log) because of binary trees
# sorted_list = SortedList()
# sorted_list.add(50)
# sorted_list.add(20)
# sorted_list.add(20)
# sorted_list.add(10)
# sorted_list.add(30)
#
# print(sorted_list)

# sorted_list = SortedList()
# sorted_list.add('abcd')
# sorted_list.add('aBc')
# sorted_list.add('AbCd')
# sorted_list.add('ac')
# sorted_list.add('bdc')
#
# print(sorted_list)


sorted_list = SortedKeyList(key=str.casefold) #case-insensitive compare
sorted_list.add('abcd')
sorted_list.add('aBc')
sorted_list.add('AbCd')
sorted_list.add('ac')
sorted_list.add('bdc')

print(sorted_list)