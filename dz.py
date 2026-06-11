import random

start = 10
end = 99
quantity = 10
lst = []

# dz 1
random_list = [random.randint(start // 2, end // 2) * 2 + 1 for n in range(quantity)]
print(random_list)  # even/odd

# dz2
random_list = [n for n in random.sample(range(start, end + 1), quantity) if n % 2 != 0]
print(random_list)

# dz3
result = [x + 1 if x % 2 == 0 else x for x in random.sample(range(start, end + 1), quantity)]
print(result)

# result = [x  if x % 2 != 0 else x + 1  for x in random.sample(range(start, end + 1), quantity)]
# print(result)

# dz4
list4 = [random.randrange(start + 1, end, 2) for n in range(quantity)]
print(list4)

# dz5
list5 = range(start + 1, end, 2)
rand_lst5 = [random.choice(list5) for n in range(quantity)]
print(rand_lst5)

#dz6
list6 = [n for n in range(start,end) if n % 2 != 0]
r_list = random.sample(list6, quantity)
print(r_list)





