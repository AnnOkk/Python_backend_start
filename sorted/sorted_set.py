from sortedcontainers import SortedSet

sorted_set = SortedSet()

sorted_set.add('abcd')
sorted_set.add('aBc')
sorted_set.add('AbCd')
sorted_set.add('ac')
sorted_set.add('bdc')
sorted_set.add('ac')
sorted_set.add('aBc')

print(sorted_set)
