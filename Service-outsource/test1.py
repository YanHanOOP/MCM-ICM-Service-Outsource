from PIL import Image
import pytesseract
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

#im = Image.open("C:/Users/YanHan/Desktop/waibao/data-1/train-1/0007.jpg")
#im = Image.open("C:/Users/YanHan/Desktop/waibao/data-1/for/0007.jpg")
#im = Image.open("C:/Users/YanHan/Desktop/waibao/data-3/train/0000.jpg")
im = Image.open("C:/Users/YanHan/Desktop/waibao/data-4/train/0000.jpg")
#im = Image.open("C:/Users/YanHan/Desktop/waibao/data-5/train/0000/0.jpg")

#转灰度图
im_l = im.convert('L')
im_l.show()
#print(im.format, im.size, im.mode)
#print(im_l.format, im_l.size, im_l.mode)

#threshold = ...
out = binarizing(im_l,200)
out.show()
print(pytesseract.image_to_string(out))

out = depoint(out)
out.show()
print(pytesseract.image_to_string(out, lang="chi_sim"))
"""
tiout = depoint(biout)
tiout.show()
print(pytesseract.image_to_string(tiout))

fiout = depoint(tiout)
fiout.show()
print(pytesseract.image_to_string(fiout))
"""

"""
out = deline(out)
out.show()
print(pytesseract.image_to_string(out, lang="eng",config="-psm 7 waibao1"))
"""


"""
cuts = [(11,17,51,71),(51,17,90,71),(90,17,133,71),(133,17,176,71),(176,17,218,71),(218,17,260,71),
        (260,17,300,71),(300,17,343,71)]
for i,n in enumerate(cuts,1):
    temp = lout.crop(n) # 调用crop函数进行切割
    temp.save("C:/Users/YanHan/Desktop/waibao/cut%s.jpg" % i)

"""




