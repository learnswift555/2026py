# 作者：柚子皮
# 2026年02月25日22时00分59秒
# yexixi2333@gmail.com

import copy


def use_list_copy():
    """
    使用列表自身的copy
    :return:
    """
    a = [1, 2, 3]
    b = copy.copy(a)
    a = [1, 2, 3]
    b = a.copy()
    b[0] = 2
    print(a)
    print(b)


def use_copy():
    """
    使用copy包里面的copy
    :return:
    """
    c = [1, 2, 3]
    d = copy.copy(c)
    print(id(c))
    print(id(d))


def use_copy2():
    a = [1, 2]
    b = [3, 4]
    c = [a, b]
    d = copy.copy(c)
    print(id(c))
    print(id(d))
    a[0] = 10
    print(f'c={c}')
    print(f'd={d}')


def use_deepcopy():
    a = [1, 2]
    b = [3, 4]
    c = [a, b]
    d = copy.deepcopy(c)
    print(id(c[0]), id(c[1]))
    print(id(d[0]), id(d[1]))
    print(id(c))
    print(id(d))
    a[0] = 10
    print(f'c={c}')
    print(f'd={d}')


if __name__ == '__main__':
    # use_copy()
    # use_copy2()
    use_deepcopy()
