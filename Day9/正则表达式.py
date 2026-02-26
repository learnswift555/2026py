# 作者：柚子皮
# 2026年02月25日23时26分31秒
# yexixi2333@gmail.com

import re


def simple():
    result = re.match("wangdao", "wangdao.cn")

    if result:
        print(result.group())


def single():
    """
    匹配单个字符
    :return:
    """
    ret = re.match(".", "abc")
    print(ret.group())

    ret = re.match("t.", "too")
    print(ret.group())

    ret = re.match("t.o", "two")
    print(ret.group())


def muti_alp():
    """
    匹配多个字符
    :return:
    """
    ret = re.match("[A-Z][a-z]*", "M")
    print(ret.group())

    ret = re.match("[A-Z][a-z]*[A-Z]", "MnnM")
    print(ret.group())

    ret = re.match("[A-Z][a-z]*[A-Z]*", "AabcdefSDFA")
    print(ret.group())

    print('-' * 55)

    names = ["name2", "_name", "2_name", "__name__"]
    for name in names:
        ret = re.match(r'[a-zA-Z_]\w*', name)
        if ret:
            print(f'{ret.group()}符合命名规范')
        else:
            print(f'{name}不符合命名规范')
    print('-' * 55)

    ret = re.match(r"[1-9]?[0-9]", "7")
    print(ret.group())

    ret = re.match(r"[1-9]?\d", "33")
    print(ret.group())

    ret = re.match(r"[1-9]?\d", "09")
    print(ret.group())

    ret = re.match(r"[1-9]?\d$", "09")
    if ret:
        print(ret.group())
    else:
        print('输入的数字不合法')

    print('-' * 55)

    ret = re.match(r"[a-zA-Z0-9_]{6}", "1231435")
    print(ret.group())

    mail = input("输入邮箱：")
    ret = re.match(r"\w{4,20}@163\.com$", mail)
    print(ret.group())


def split_group():
    """
    匹配分组
    :return:
    """
    ret = re.match(r'[1-9]\d$|100|[0-9]$', '66')
    if ret:
        print(ret.group())
    else:
        print("不在范围中")

    ret = re.match(r'([^-]+)-(\d+)', '010-12345678')
    print(ret.group())
    print(ret.group(1))
    print(ret.group(2))


def prac1():
    ret = re.match(r'<[a-zA-Z]*>\w*</[a-zA-Z]*>', '<html>hh</html>')
    print(ret.group())
    ret = re.match(r'<([a-zA-Z]*)>\w*</\1>', '<html>hh</html>')
    print(ret.group())


def prac2():
    labels = ["<html><h1>www.cskaoyan.com</h1></html>", "<html><h1>www.cskaoyan.com</h2></html>"]

    for label in labels:
        ret = re.match(r"<(\w*)><(\w*)>.*</\2></\1>", label)
        if ret:
            print("%s 是符合要求的标签" % ret.group())
        else:
            print("%s 不符合要求" % label)


def prac3():
    labels = ["<html><h1>www.cskaoyan.com</h1></html>", "<html><h1>www.cskaoyan.com</h2></html>"]

    for label in labels:
        ret = re.match(r"<(?P<name1>\w*)><(?P<name2>\w*)>.*</(?P=name2)></(?P=name1)>", label)
        if ret:
            print(ret.group())
        else:
            print("不符合要求")


def prac4():
    """
    search
    :return:
    """
    ret = re.search(r"\d+", "阅读次数为9999")
    print(ret.group())


def find_second(my_pattern, my_text):
    matches = re.finditer(my_pattern, my_text)
    try:
        next(matches)
        sec_match = next(matches)
        return sec_match.group()
    except StopIteration:
        return None


def find_iter():
    text = 'abc123def456ghi789'
    pattern = r'\d+'
    second_match = find_second(pattern, text)
    print(second_match)


def prac_sub():
    ret = re.sub(r"\d+", '999', 'python=9975')
    print(ret)
    # lambda  参数  :  返回值
    ret = re.sub(r"\d+", lambda x: str(int(x.group()) + 100), 'python=997')
    print(ret)


def usr_findall():
    s = 'hello world, now is 2020/7/20 18:48, 现在是2020年7月20日18时48分。'
    ret_s = re.sub(r'年|月', r'/', s)
    ret_s = re.sub(r'日|分', r' ', ret_s)
    ret_s = re.sub(r'时', r':', ret_s)
    print(ret_s)
    pattern = re.compile(r'\d{4}/[01]?[0-9]/[1-3]?[0-9]\s(?:0[0-9]|1[0-9]|2[0-4])\:[0-5][0-9]')
    # - findall
    # 没有括号 → 返回整体匹配
    # 有() → 返回括号里的内容
    # 有(?:) → 括号只用来分组，不影响返回值，还是返回整体
    ret = pattern.findall(ret_s)
    print(ret)


def use_sub():
    long_test = """
<dic>
<p>必备要求：</p>
<p>良好的自我驱动力和职业素养，工作积极主动、结果导向</p>
<p>&nbsp;<br></p>
<p>技术要求：</p>
<p>1、一年以上 Python 开发经验，掌握面向对象分析和设计，了解设计模式</p>
<p>2、掌握 HTTP 协议，熟悉 MVC、MVVM 等概念以及相关 WEB 开发框架</p>
<p>3、掌握关系数据库开发设计，掌握 SQL，熟练使用 MySQL/PostgreSQL 中的一种<br></p>
<p>4、掌握 NoSQL、MQ，熟练使用对应技术解决方案</p>
<p>5、熟悉 Javascript/CSS/HTML5，JQuery、React、Vue.js</p>
<p>&nbsp;<br></p>
<p>加分项：</p>
<p>大数据，数理统计，机器学习，sklearn，高性能，大并发。</p>
</div>
    """
    # print(long_test)
    ret = re.sub(r'<[^>]*>|&nbsp;|\n|\s', '', long_test)
    print(ret)


def use_split():
    ret = re.split(f":| ", "info:xiaozhang 33 shandong")
    print(ret)


if __name__ == '__main__':
    # simple()
    # single()
    # muti_alp()
    # split_group()
    # prac1()
    # prac2()
    # prac3()
    # prac4()
    # prac_sub()
    # usr_findall()
    # use_sub()
    use_split()