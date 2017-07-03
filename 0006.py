# -*- coding: utf-8 -*-
"""
**第 0006 题：**
你有一个目录，放了你一个月的日记，都是 txt，
为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词。
"""
import os
import re


def find_word(dir_path):
    if not os.path.isdir(dir_path):
        return
    file_list = os.listdir(dir_path)
    re_obj = re.compile('\b?(\w+)\b?')
    for file in file_list:
        file_path = os.path.join(dir_path, file)
        if os.path.isfile(file_path) and os.path.splitext(file_path)[1] == '.txt':
            with open(file_path) as f:
                data = f.read()
                words = re_obj.findall(data)
                word_dict = dict()
                for word in words:
                    word = word.lower()
                    if word in ['a', 'the', 'to']:
                        continue
                    if word in word_dict:
                        word_dict[word] += 1
                    else:
                        word_dict[word] = 1
            ansList = sorted(word_dict.items(), key=lambda t: t[1], reverse=True)
            print('file: %s->the most word: %s' % (file, ansList[0]))


def main():
    find_word('source/0006')


if __name__ == '__main__':
    main()
