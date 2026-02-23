# 作者：柚子皮
# 2026年02月23日21时05分51秒
# yexixi2333@gmail.com

import os


def read_conf():
    """
    读取配置文件
    :return:
    """

    file = open('file4', 'r+', encoding='utf-8')
    text_info = file.read()
    print(text_info)
    my_dict = eval(text_info)
    print(my_dict)
    file.close()


if __name__ == '__main__':
    # read_conf()
    eval("print('hello world')")
