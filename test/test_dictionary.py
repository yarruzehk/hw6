from in_class.demo_2021_02_11.dictionary import function_required_for_homework


def test_name_gets_upper_cased():
    name = "zeke"
    output = "ZEKE"
    assert function_required_for_homework(name) == output


def test_strip_space_at_end():
    name = "zeke "
    output = "ZEKE"
    assert function_required_for_homework(name) == output


def test_strip_spaces():
    name = " zeke "
    output = "ZEKE"
    assert function_required_for_homework(name) == output


def test_remove_all_spaces():
    name = " zeke last name"
    output = "ZEKELASTNAME"
    assert function_required_for_homework(name) == output
