from PIL import Image
import pytesseract
import os
def depoint(img):
    """传入二值化后的图片进行降噪"""
    pixdata = img.load()
    w, h = img.size
    for y in range(1,h-1):
        for x in range(1,w-1):
            count = 0
            if pixdata[x,y-1] > 245:#上
                count = count + 1
            if pixdata[x,y+1] > 245:#下
                count = count + 1
            if pixdata[x-1,y] > 245:#左
                count = count + 1
            if pixdata[x+1,y] > 245:#右
                count = count + 1
            if pixdata[x-1,y-1] > 245:#左上
                count = count + 1
            if pixdata[x-1,y+1] > 245:#左下
                count = count + 1
            if pixdata[x+1,y-1] > 245:#右上
                count = count + 1
            if pixdata[x+1,y+1] > 245:#右下
                count = count + 1
            if count > 4:
                pixdata[x,y] = 255
    return img

def deline(img):
    """deline"""
    pixdata = img.load()
    w, h = img.size
    for y in range(2,h-2):
        for x in range(2,w-2):
            count = 0
            if pixdata[x,y] == 0:
                if pixdata[x,y-2] == 255:
                    count = count + 1
                if pixdata[x,y+2] == 255:
                    count = count + 1
                if pixdata[x-2,y]:
                    count = count + 1
                if pixdata[x+2,y]:
                    count = count + 1
                if count >=3:
                    pixdata[x,y] = 255

    return img

def get_feature(img):
    width, height = img.size
    print(img.size)
    pixel_cnt_list = []
    #height = 10
    for y in range(height):
        pix_cnt_x = 0
        for x in range(width):
            if img.getpixel((x, y)) <= 1:  # 黑色点
                pix_cnt_x += 1

        pixel_cnt_list.append(pix_cnt_x)

    for x in range(width):
        pix_cnt_y = 0
        for y in range(height):
            if img.getpixel((x, y)) <= 1:  # 黑色点
                pix_cnt_y += 1

        pixel_cnt_list.append(pix_cnt_y)

    return pixel_cnt_list

def binarizing(img,threshold):
    """传入image对象进行二值处理"""
    pixdata = img.load()
    w, h = img.size
    for y in range(h):
        for x in range(w):
            if pixdata[x, y] < threshold:
                pixdata[x, y] = 0
            else:
                pixdata[x, y] = 255
    return img


#im = Image.open("C:/Users/YanHan/Desktop/waibao/data-1/for/0007.jpg")
"""
folder = "C:/Users/YanHan/Desktop/waibao/data-1/train-1/"
for filename in os.listdir(folder):
        print((os.path.join(folder,filename)))
        im = Image.open((os.path.join(folder,filename)))
        im_l = im.convert('L')#灰度

        out = binarizing(im_l,160)#二值化
        
        biout = depoint(out)#去点
        
        biout = deline(biout)#去线
        #biout.show()
        #print(pytesseract.image_to_string(biout))
        cuts = [(10,17,51,71),(50,17,91,71),(90,17,131,71),(133,17,174,71),(176,17,217,71),(218,17,259,71),
                (260,17,301,71),(303,17,344,71)]
        for i,n in enumerate(cuts,1):
            temp = biout.crop(n) # 调用crop函数进行切割
            temp.save("C:/Users/YanHan/Desktop/waibao/data-1/train-set/%s-%s.jpg" % (filename,i))
"""
im = Image.open("C:/Users/YanHan/Desktop/waibao/data-1/train-set/-/0069.jpg-3.jpg")
print(get_feature(im))



