# 作者：柚子皮
# 2026年02月27日01时56分07秒
# yexixi2333@gmail.com

import re


def use_greedy():
    s = "This is a number 234-235-22-423"
    ret = re.match(r".+?(\d+-\d+-\d+-\d+)", s)
    print(ret.group(1))


if __name__ == '__main__':
    use_greedy()
