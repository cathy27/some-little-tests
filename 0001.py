# -*- coding:utf-8 -*-
# 第0001题： 做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码
# （或者优惠券）？

import random, string

num_select = string.ascii_letters + "0123456789"


def generate(count, length):
    # count = 200
    # length = 20

    for x in range(count):
        ran_No = ""
        for y in range(length):
            ran_No += random.choice(num_select)
        print(ran_No )


def main():
    generate(200, 20)


if __name__ == '__main__':
    main()