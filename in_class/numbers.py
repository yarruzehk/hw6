from in_class.demo_2021_02_09.generic_imports import josh, jem

y = "hello world"

print(josh())
print(jem)


def foobar(i: int):
    x = 5
    if i > 10:
        x = i
    else:
        x = 5
    return x


def foo():
    x = 10 * 10
    print("x", x)


if __name__ == "__main__":
    print(y)
    print(__name__)
    foo()
    print(foobar(10))
