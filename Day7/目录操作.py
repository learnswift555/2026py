# 作者：柚子皮
# 2026年02月23日16时50分31秒
# yexixi2333@gmail.com
import os


def use_rename():
    # os.rename('dir1\\file2', 'dir1\\file1')
    os.remove('dir1\\file1')


def use_dir_func():
    file_list = os.listdir('.')
    print(file_list)
    try:
        os.mkdir('dir2')
    except FileExistsError:
        print("dir2已经存在，不需要再次创建")
    try:
        os.rmdir('dir1')
    except FileNotFoundError:
        print("dir1不存在，无法删除")
    print(os.getcwd())

    os.chdir('dir2')
    file = open('file1', 'w', encoding='utf-8')
    file.close()


def change_dir():
    """
    改变路径
    :return:
    """
    print(os.getcwd())
    os.chdir('dir2')
    print(os.getcwd())


def scan_dir(width, current_path):  # 这个写的真牛逼
    """
    深度优先遍历
    :param current_path:
    :return:
    """
    file_list = os.listdir(current_path)
    for file in file_list:
        print(width * ' ', file)
        new_path = current_path + '/' + file
        if os.path.isdir(new_path):
            scan_dir(width + 4, new_path)


def use_state(file_path):
    file_info = os.stat(file_path)
    print('size{},uid{},mode{:x},mtime{}'.format(file_info.st_size, file_info.st_uid,
                                                 file_info.st_mode, file_info.st_mtime))
    # print(file_info.st_size)

if __name__ == '__main__':
    # use_rename()
    # use_dir_func()
    # change_dir()
    # scan_dir(0, '.')
    use_state('file2.txt')
