# -*- coding: utf-8 -*-
"""
**第 0007 题：**
有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。
"""

import os
import re
from os.path import join


def stat_code(dir_path):
    if not os.path.isdir(dir_path):
        return
    exp_re = re.compile(r'^#.*')
    print("%s\t%s\t%s\t%s\t%s" % ('file', 'all_lines', 'space_lines', 'code_lines', 'comment_lines'))
    for root, dirs, files in os.walk(dir_path):
        for name in files:
            if name.split('.')[-1] == 'py':
                all_lines = 0
                code_lines = 0
                space_lines = 0
                comment_lines = 0
                file_name = join(root, name)
                f = open(file_name)
                for line in f:
                    all_lines += 1
                    if line.strip() == '':
                        space_lines += 1
                    elif exp_re.match(line.strip()) != None:
                        comment_lines += 1
                    else:
                        code_lines += 1
                print("%s\t%s\t%s\t%s\t%s" % (name, all_lines, space_lines, code_lines, comment_lines))


def main():
    stat_code("../../电销/second_feature")


if __name__ == '__main__':
    main()