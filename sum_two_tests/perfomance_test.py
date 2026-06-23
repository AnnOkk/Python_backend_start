from time import time
from sum_two_tests.sum_two import is_sum_two2, is_sum_two1
if __name__ == '__main__':
    large_numbers = list(range(100_000))
    print(f'test with {len(large_numbers)} numbers')
    target_sum = 200_000
    #testing is_sim_two1
    start_time = time()
    result = is_sum_two1(large_numbers, target_sum)
    end_time = time()
    print(f'time: {end_time - start_time} seconds, result: {result}')

    # testing is_sim_two2
    start_time = time()
    result = is_sum_two2(large_numbers, target_sum)
    end_time = time()
    print(f'time: {end_time - start_time} seconds, result: {result}')




