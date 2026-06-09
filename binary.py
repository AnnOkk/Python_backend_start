arr1 = [22, 79, 4, 66, 123, 7, 9, 0, -8, 74]


def bubblesort_arr(arr):
    for i in range(0, len(arr) - 1):
        for j in range(0, len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    return arr


print(bubblesort_arr(arr1))

num = int(input("enter the number: "))
def binary_search(arr):
    arr = bubblesort_arr(arr)
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (right + left) // 2
        if arr[mid] == num:
            return mid
        elif arr[mid] > num:
            right = mid - 1
        elif arr[mid] < num:
            left = mid + 1
    return -1


print(f'Index of {num} = ',binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(f'Index of {num} = ',binary_search(arr1))
print(f'Index of {num} = ',binary_search([]))








# const arr = [5, 2, 8, 1, 3];
#
# for (let i = 0; i < arr.length - 1; i++) {
#     for (let j = 0; j < arr.length - 1 - i; j++) {
#         if (arr[j] > arr[j + 1]) {
#             let temp = arr[j];
#             arr[j] = arr[j + 1];
#             arr[j + 1] = temp;
#         }
#     }
# }
#
# console.log(arr);
