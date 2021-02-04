
layout = [['a','b','c'],['b','c'],['a','a','a']]
def simple_array():
    x = []
    x.append('a')
    x.extend(['a','b'])
    x.extend(list(range(10)))
    return x

def foo(array: list):
    ret = []
    for i in array:
        if str(i) != 'a':
            ret.append(i)
    return ret

def compare_elements(array: list):
    print('length of the array', len(array))
    try:
        return [i for i in array if str(i) != 'a']
    except Exception as e:
        return None

def set_of_array(array: list):
    return set(array)


if __name__ == '__main__':
    # print(list(range(5)))
    # print(simple_array())
    print(compare_elements(simple_array()))

    # print(set_of_array(simple_array()))