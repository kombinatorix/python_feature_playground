# see https://www.python.org/dev/peps/pep-0498/ and
# https://docs.python.org/3/reference/lexical_analysis.html#formatted-string-literals for more information
f"""
Whoa, we can use f-strings in {3}-quoted strings
"""

first_string = "first_string"
print(f"{first_string}\n with just f")
print(rf"{first_string}\n with f and r (combining f and raw strings)")


class ClassToExperimentWith(object):
    def __init__(self, content) -> None:
        self.content = content

    def __str__(self) -> str:
        return self.content

    def __repr__(self) -> str:
        return f"ClassToExperiment({self.content})"


instance = ClassToExperimentWith("My Umlauts ÄäÖöÜü")
print(f"a!: {instance!a}")
print(f"r!: {instance!r}")
print(f"s!: {instance!s}")

print(f"Let's capitalize our {'f-string'.capitalize()}")

print(f"A lambda in need is a {(lambda x: x)('lambda') =} indeed.")

print(f"More that three digits of pi are not needed: {3.1415:.2f}")
import locale

locale.setlocale(locale.LC_ALL, "de_DE.UTF-8")
print(f"One in a {1000000:n} for our German friends")
