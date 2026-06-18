


def is_sum_two(lst,sum):
    seen = set(lst)

    for num in lst:
        needed = sum - num
        if needed in seen:
            return True
        seen.add(num)
    return False





# print(is_sum_two([1,2,3,4,5],6))
# print(is_sum_two([1,2,3,4,5],15))