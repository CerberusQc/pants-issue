from .example import ExampleClass
from .not_working import BadExample


def main():
    print("This is my main package")

    example = ExampleClass(value="test")
    print(example.value)

    bad_example = BadExample(value="test2")
    print(bad_example.value)
