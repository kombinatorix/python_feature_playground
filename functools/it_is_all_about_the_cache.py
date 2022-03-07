from timeit import timeit
from functools import cache, lru_cache


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


@lru_cache
def quadratic_numbers_1(list_of_ints):
    return [el**2 for el in list_of_ints]


if __name__ == "__main__":
    # cache
    print(
        f'Uncached version of Fibonacci n=20: {timeit("fibonacci_1(20)", globals=globals(), number=1_000)} seconds (1000it)'
    )
    fibonacci_2.cache_clear()
    print(
        f'Cached version of Fibonacci n=20: {timeit("fibonacci_2(20)", globals=globals(), number=1_000)} seconds (1000it)'
    )

    # lru_cache
    try:
        quadratic_numbers_1([0, 1, 2, 3, 4])
    except TypeError as e:
        print(
            "lru_cache doesn't except non-hashable function inputs, becausee it is based internally as dictionary"
        )
