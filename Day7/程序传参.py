# 作者：柚子皮
# 2026年02月23日20时13分40秒
# yexixi2333@gmail.com

import sys


# print(type(sys.argv))
# print(sys.argv)
def write_hello(file_path):
    file = open(file_path, 'w+', encoding='utf-8')
    file.write('hello啊')
    file.close()


if __name__ == '__main__':
    write_hello(sys.argv[1])
