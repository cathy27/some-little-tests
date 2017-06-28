# coding=utf8=
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random as rd

#随机字母
def randchar():
    return chr(rd.randint(65,90))

#随机颜色1
def randcolor():
    return (rd.randint(64,255), rd.randint(64,255), rd.randint(64,255))

#随机颜色2
def randcolor2():
    return (rd.randint(32,127), rd.randint(32,127), rd.randint(32,127))

def gen_yanzhengma(base_len, alp_Num, name, is_filter):
    width = base_len * alp_Num
    height = base_len
    image = Image.new('RGB', (width, height), (255, 255, 255))
    font = ImageFont.truetype('Arial.ttf', 36)  #创建font
    draw = ImageDraw.Draw(image)  #创建draw
    #填充每个像素
    for x in range(width):
        for y in range(height):
            draw.point((x,y), fill=randcolor())
    #输出文字
    for t in range(alp_Num):
        draw.text((base_len * t + 10, 10), randchar(), font=font, fill=randcolor2())
    #是否模糊
    if is_filter == 1:
        image = image.filter(ImageFilter.BLUR)
    image.save('%s.jpg' % name, 'jpeg')

def main():
    para1 = 60
    para2 = 5
    para3 = 'code'
    para4 = 0
    gen_yanzhengma(para1, para2, para3, para4)


if __name__ == '__main__':
    main()
