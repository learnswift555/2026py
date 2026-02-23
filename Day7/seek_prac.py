# 作者：柚子皮
# 2026年02月22日22时53分40秒
# yexixi2333@gmail.com
import os
from fileinput import close


def seek_start():
    """
    相对于开头进行偏移
    :return:
    """
    file = open('file3', mode='r+', encoding='utf-8')
    file.seek(6, os.SEEK_SET)  # 汉字的偏移是3的整数倍
    text = file.read(5)
    print(text)
    file.close()


def seek_end():
    """
    相对于文件尾部
    :return:
    """
    file = open('file3', mode='r+', encoding='utf-8')
    file.seek(0, os.SEEK_END)
    text = file.read(6)
    print(text)
    file.close()


def seek_b_cur():
    """
    b模式下读取的是字节流
    :return:
    """
    file = open('file3', mode='rb+')
    file.seek(5, os.SEEK_CUR)
    file.seek(-3, os.SEEK_END)
    b = file.read()
    print(b)
    file.close()


def copy_file():
    file1 = open('jia.png', mode='rb+')
    file2 = open('jia_copy.png', mode='wb')
    b = file1.read()
    file2.write(b)
    file1.close()
    file2.close()

if __name__ == '__main__':
    # seek_start()
    # seek_end()
    # seek_b_cur()
    copy_file()