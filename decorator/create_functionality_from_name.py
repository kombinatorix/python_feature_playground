from functools import wraps


def eval_funcname(func):
    def change_behavior():
        func_name = func.__name__
        mapping = {"leftbracket": "(", "quote": "'", "rightbracket": ")"}
        eval(
            "".join(
                [
                    mapping[el] if el in mapping.keys() else el
                    for el in func_name.split("_")
                ]
            )
        )

    return change_behavior


@eval_funcname
def print_leftbracket_quote_funky_quote_rightbracket():
    pass


def eval_funcname_with_original_name(func):
    def change_behavior():
        func_name = func.__name__
        mapping = {"leftbracket": "(", "quote": "'", "rightbracket": ")"}
        eval(
            "".join(
                [
                    mapping[el] if el in mapping.keys() else el
                    for el in func_name.split("_")
                ]
            )
        )

    change_behavior.__name__ = func.__name__
    return change_behavior


@eval_funcname_with_original_name
def print_leftbracket_quote_funky_with_the_original_quote_rightbracket():
    pass


def eval_funcname_with_original_name2(func):
    @wraps(func)
    def change_behavior():
        func_name = func.__name__
        mapping = {"leftbracket": "(", "quote": "'", "rightbracket": ")"}
        eval(
            "".join(
                [
                    mapping[el] if el in mapping.keys() else el
                    for el in func_name.split("_")
                ]
            )
        )

    change_behavior.__name__ = func.__name__
    return change_behavior


@eval_funcname_with_original_name2
def print_leftbracket_quote_funky_with_the_original2_quote_rightbracket():
    pass


if __name__ == "__main__":
    print(f"{print_leftbracket_quote_funky_quote_rightbracket.__name__=}")
    print_leftbracket_quote_funky_quote_rightbracket()
    print(
        f"{print_leftbracket_quote_funky_with_the_original_quote_rightbracket.__name__=}"
    )
    print_leftbracket_quote_funky_with_the_original_quote_rightbracket()
    print(
        f"{print_leftbracket_quote_funky_with_the_original2_quote_rightbracket.__name__=}"
    )
    print_leftbracket_quote_funky_with_the_original2_quote_rightbracket()
