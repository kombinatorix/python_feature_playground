def get_dict_of_function(func):
    """
    decorator for printing __dict__ of a function
    see: https://docs.python.org/3/library/stdtypes.html#object.__dict__
    """

    def change_of_behavior():
        print(f"{func.__dict__=}")
        func()

    return change_of_behavior


@get_dict_of_function
def func_dict():
    print('"func_dict" is executed')


def get_class_of_function(func):
    """
    decorator for printing __class__ of a function
    see: https://docs.python.org/3/library/stdtypes.html#instance.__class___
    """

    def change_of_behavior():
        print(f"{func.__class__=}")
        func()

    return change_of_behavior


@get_class_of_function
def func_class():
    print('"func_class" is executed')


def get_bases_of_function(func):
    """
    decorator for printing __bases__ of a function
    see: https://docs.python.org/3/library/stdtypes.html#class.__bases__
    """

    def change_of_behavior():
        print(f"{func.__class__.__bases__=}")
        func()

    return change_of_behavior


@get_bases_of_function
def func_bases():
    print('"func_bases" is executed')


def get_name_of_function(func):
    """
    decorator for printing __name__ of a function
    see: https://docs.python.org/3/library/stdtypes.html#definition.__name__
    """

    def change_of_behavior():
        print(f"{func.__name__=}")
        func()

    return change_of_behavior


@get_name_of_function
def func_name():
    print('"func_name" is executed')


def get_qualname_of_function(func):
    """
    decorator for printing __name__ of a function
    see: https://docs.python.org/3/library/stdtypes.html#definition.__qualname__
    """

    def change_of_behavior():
        print(f"{func.__qualname__=}")
        func()

    return change_of_behavior


@get_qualname_of_function
def func_qualname():
    print('"func_qualname" is executed')


def get_mro_of_function(func):
    """
    decorator for printing __name__ of a function
    see: https://docs.python.org/3/library/stdtypes.html#class.__mro__
    """

    def change_of_behavior():
        print(f"{func.__class__.__mro__=}")
        func()

    return change_of_behavior


@get_mro_of_function
def func_mro():
    print('"func_mro" is executed')


def get_subclasses_of_function(func):
    """
    decorator for printing __name__ of a function
    see: https://docs.python.org/3/library/stdtypes.html#class.__subclasses__
    """

    def change_of_behavior():
        print(f"{func.__class__.__subclasses__()=}")
        func()

    return change_of_behavior


@get_subclasses_of_function
def func_subclasses():
    print('"func_subclasses" is executed')


if __name__ == "__main__":
    func_dict()
    func_class()
    func_bases()
    func_name()
    func_qualname()
    func_mro()
    func_subclasses()
