# import time

# start_time = time.time()

# # Your code segment to measure





# for i in range(12344,78905):
#     print(i*4567)

# end_time = time.time()
# execution_time = end_time - start_time
# print(f"Execution Time: {execution_time} seconds")


import numba

@numba.jit
def solve_problem():
    result = 0
    for i in range(10**6):
        result += i

# Measure the execution time using timeit
execution_time = timeit.timeit(solve_problem, number=1)

# Print the execution time
print(f"Execution time with Numba: {execution_time} seconds")
