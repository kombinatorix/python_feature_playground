import types


class MyClass(object):
    def __init__(self) -> None:
        self.name = "MyClass"

    def change_name_to(self, new_name) -> None:
        self.name = new_name
        print(self.name)


instance = MyClass()

instance.change_name_to("foo")


def name_is_allways_bar(self, new_name):
    self.name = "bar"
    print(self.name)


instance.change_name_to = types.MethodType(name_is_allways_bar, instance)

instance.change_name_to("Foo")
