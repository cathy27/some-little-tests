# coding=utf8=
# 第0004题： 任一个英文的纯文本文件，统计其中的单词出现的个数。

import re
from collections import Counter


def word_count(txt):
    word_pattern = r'[a-zA-Z-]+'
    words = re.findall(word_pattern, txt)
    return Counter(words).items()


def main():
    txt = open('test.txt','r').read().lower()
    print word_count(txt)


if __name__ == '__main__':
    main()