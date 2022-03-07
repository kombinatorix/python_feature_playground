from functools import wraps
import ast
import inspect


def decorator1(func):
    @wraps(func)
    def wrapper():
        print("decorator1")

        func()

    return wrapper


def decorator2(func):
    @wraps(func)
    def wrapper():
        print("decorator2")
        func()

    return wrapper


def decorator3(func):
    @wraps(func)
    def wrapper():
        print("decorator3")
        func()

    return wrapper


def get_decorators(cls):  # see https://stackoverflow.com/a/31197273
    target = cls
    decorators = {}

    def visit_FunctionDef(node):
        decorators[node.name] = []
        for n in node.decorator_list:
            name = ""
            if isinstance(n, ast.Call):
                name = n.func.attr if isinstance(n.func, ast.Attribute) else n.func.id
            else:
                name = n.attr if isinstance(n, ast.Attribute) else n.id

            decorators[node.name].append(name)

    node_iter = ast.NodeVisitor()
    node_iter.visit_FunctionDef = visit_FunctionDef
    node_iter.visit(ast.parse(inspect.getsource(target)))
    return decorators


def enforce_decorator_sequence(func):
    @wraps(func)
    def wrapper():
        tmp_func = func
        while "__wrapped__" in tmp_func.__dir__():
            tmp_func = tmp_func.__wrapped__
        vals = sorted(list(get_decorators(func).values())[0])
        func_to_be_rewrapped = tmp_func.__call__
        for val in vals:
            if val != "enforce_decorator_sequence":
                func_to_be_rewrapped = globals()[val](func_to_be_rewrapped)
        func_to_be_rewrapped()

    return wrapper


@enforce_decorator_sequence
@decorator1
@decorator3
@decorator2
def function():
    print("function call")


function()


def sort_decorators(list_of_decorators):
    def wrapper_looking_like_decorator(func):
        @wraps(func)
        def wrapper():
            print("wrapper function of sort decorators")
            tmp_func = func
            list_of_decorators.sort(key=lambda x: x.__name__)
            for dec in list_of_decorators:
                tmp_func = dec(tmp_func)
            tmp_func()

        return wrapper

    return wrapper_looking_like_decorator


@sort_decorators([decorator2, decorator3, decorator1])
def function2():
    print("function2 call")


function2()
