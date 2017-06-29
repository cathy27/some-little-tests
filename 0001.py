# -*- coding:utf-8 -*-

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