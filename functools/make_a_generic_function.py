from functools import singledispatch


@singledispatch
def soon_to_be_generic_function(input):
    print(f"This is the case, which is not specified. The argument is {input}")


@soon_to_be_generic_function.register  # with type annotation
def _(input: int):
    print(f"This is the 'int' case. The argument is {input}")


@soon_to_be_generic_function.register(float)  # This is witout type annotation
def _(input):
    print(f"This is the 'float' case. The argument is {input}")


soon_to_be_generic_function.register(
    list, lambda input: print(f"This is the 'list' case. The argument is {input}")
)  # register a lambda or preexisting function

if __name__ == "__main__":
    soon_to_be_generic_function(None)
    soon_to_be_generic_function(27)
    soon_to_be_generic_function(3.14)
    soon_to_be_generic_function(["a", "b"])
