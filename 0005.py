# coding=utf8=
# 第0005题：你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。

from PIL import Image
import os


def resize_image(image):
    im = Image.open(image)
    width, height = im.size
    if height > 1136 or width > 640:
        th = height / 1136
        td = width / 640
        ts = max(th,td)
        nh = int(height / ts)
        nw = int(width / ts)
        im = im.resize((nw, nh))
        im.save(image)
        print('Successfully resized %s. New width is %i, new height is %i.'%(image, nh, nw))
    else:
        print("There's no need to resize %s."%image)


def main():
    path = './photo'
    for i in os.listdir(path):
        try:
            resize_image(i)
        except IOError:
            print("Oops! %s is not supported to make the change!"%i)


if __name__ == '__main__':
    main()