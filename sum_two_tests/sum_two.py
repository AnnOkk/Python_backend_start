def is_sum_two1(numbers, sum):
    helper = set()
    indx = 0
    res = False
    length = len(numbers)
    while indx < length and not res:
        if sum - numbers[indx] in helper:
            res = True
        else:
            helper.add(numbers[indx])
            indx += 1
    return res

def is_sum_two2(numbers, sum):
    res = False
    for i in range(len(numbers)):
        sub =sum-numbers[i]
        if sub in numbers[i+1:]:
            res = True
            break
    return res