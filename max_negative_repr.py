def max_negative_repr(numbers):
    result = -1
    set1 = set(numbers)
    for num in numbers:
        if num > 0 and -num in set1:
            if num > result:
                result = num

    return result


print(max_negative_repr([100, 4, 1, -1, -4, -100]))
print(max_negative_repr([100, 4, 1, 1, 4, 100, -1]))
