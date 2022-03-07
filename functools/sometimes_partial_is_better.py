from functools import partial
from tkinter import W


def func_with_too_many_arguments(foo, bar, baz, foobar=0, barbaz=None, bazfoo="bar"):
    print(foo, bar, baz, foobar, barbaz, bazfoo)


new_function_with_less_arguments = partial(
    func_with_too_many_arguments, bar="bar", baz=None, barbaz=1
)

new_function_with_less_arguments(foo=2)
