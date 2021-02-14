from datetime import datetime


def function_required_for_homework(name: str) -> str:
    """
    convert name to upper case and remove all spaces in a name
    :param name:
    :return:
    """
    return name.upper().replace(" ", "")


d = {
    "key": "value",
    "key2": "value2",
    "f": "f",
    "g": "g",
    "some_super_long_key": "some_super_long_value",
}
l = [["key", "value"], ("key2", "value2"), ("f", "f")]

complex_list = [{"a": 0, "b": "string", "c": float(0.0)}, {"a": 1, "b": 3}]
# getting the first value that matches "key"
key = "key"
o = next(i[1] for i in l if i[0] == key)
print(datetime.now())
print("list", o)
print("dict", d[key])
print("complex", complex_list)
# print(l[0])
