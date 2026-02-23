# 作者：柚子皮
# 2026年02月22日09时50分31秒
# yexixi2333@gmail.com


def open_r():
    """
    读文件
    :return:
    """
    file = open('file1.txt', mode='r+', encoding='utf-8')
    print(file.read())
    file.close()


def file_wr():
    """
    读写文件
    :return:
    """
    file = open('file1.txt', mode='r+', encoding='utf-8')
    print(file.read())
    file.write('今天天气还可以奥')
    file.seek(0)
    print(file.read())
    file.close()


def open_w():
    """
    练习w模式
    :return:
    """
    file = open('file3', mode='w+', encoding='utf-8')
    file.write('sdf')
    print(file.read())
    file.close()


def open_a():
    """
    练习a模式，每次写到文件末尾
    :return:
    """
    file = open('file3', mode='a+', encoding='utf-8')
    file.write('地方')  # r+模式，光标在开头直接覆盖
    file.seek(0)
    print(file.read())
    file.close()


def use_readline():
    file = open("file3", encoding="utf-8")
    while True:
        text = file.readline()
        if not text: break
        print(text, end='')
    file.close()


if __name__ == '__main__':
    # open_r()
    # file_wr()
    # open_w()
    # open_a()
    use_readline()
