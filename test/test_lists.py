from in_class.demo_2021_02_04.list import foo, layout
from in_class.demo_2021_02_04.list import compare_elements


def test_compare_lists_simple_for_loop_with_a_filter():
    a = ["a", "b", "c"]
    expect = ["b", "c"]
    assert expect == foo(a)


def test_list_comp():

    a = ["a", "b", "c"]
    expect = ["b", "c"]
    assert expect == compare_elements(a)


def test_bad_compare():
    a = ["a", "b", "c", 1]
    expect = ["b", "c", 1]
    assert expect == compare_elements(a)


def test_filter_layout():
    output = []
    for lay in layout:
        output.append(compare_elements(lay))
    assert output == [["b", "c"], ["b", "c"], []]
