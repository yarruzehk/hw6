def simple_string_example() -> None:
    name = "Zeke Zumbro"
    v = "foo"

    v = f"hello {name}"
    name = 0.1
    print(v)
    print("helo ", name)


def compare_strings(x1: str, x2: str) -> bool:
    return x1.lower() == x2.lower().strip()


def string_compare():
    jbu = "john Brown University"
    x = "John Brown University"
    return compare_strings(jbu, x)


def string_compare_with_space():
    jbu = "John Brown University"
    x = "John Brown University "
    return compare_strings(jbu, x)


if __name__ == "__main__":
    print(string_compare())
    print(string_compare_with_space())
    q = simple_string_example()
    print(str(q))
