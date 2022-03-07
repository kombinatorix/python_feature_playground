from timeit import timeit
from functools import cache


def fibonacci_1(n):
    if n <= 1:
        return n
    else:
        return fibonacci_1(n - 1) + fibonacci_1(n - 2)


@cache
def fibonacci_2(n):
    if n <= 1:
        return n
    else:
        return fibonacci_2(n - 1) + fibonacci_2(n - 2)


print(
    f'Uncached version of Fibonacci n=20: {timeit("fibonacci_1(20)", globals=globals(), number=1_000)} seconds (1000it)'
)
print(
    f'Cached version of Fibonacci n=20: {timeit("fibonacci_2(20)", globals=globals(), number=1_000)} seconds (1000it)'
)
