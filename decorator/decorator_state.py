from typing import Callable


class FunctionExecutionCounter:
    func: Callable
    counter = 0

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        self.counter += 1
        print(f"Called {self.func.__name__} {self.counter} time(s)")

        return self.func(
            *args, **kwargs
        )  # return is important, otherwise the returnvalue of func disappears


@FunctionExecutionCounter
def simple_function():
    return "5"


@FunctionExecutionCounter
def simple_function2():
    pass


if __name__ == "__main__":
    for i in range(2):
        a = simple_function()
        print(a)
        b = simple_function2()
        print(b)
