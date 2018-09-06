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


def binarizing(img,threshold):
    pixdata = img.load()
    w, h = img.size
    for y in range(h):
        for x in range(w):
            if pixdata[x, y] < threshold:
                pixdata[x, y] = 0
            else:
                pixdata[x, y] = 255
    return img

path="C:/Users/YanHan/Desktop/test-1"
files=os.listdir(path)
map_file = open("C:/Users/YanHan/Desktop/map-1.txt","w")
i=0
for file in files:
    name = file.replace(" ","")
    im=Image.open(path+"/"+file)
    im_l = im.convert('L')
    out = binarizing(im_l,160)
    biout = depoint(out)
    lout = deline(biout)
    lout = depoint(lout)
    lout = deline(lout)
    #lout.save("C:/Users/YanHan/Desktop/waibao/data-1/waibao1-temp/temp%s.jpg" %i)
    result = pytesseract.image_to_string(lout, lang="eng",config="-psm 7 waibao1")
    result = result.replace(" ","")
    try:
        calcu = eval(result)
    except:
        calcu = 0
    
    calcu_str = str(calcu)
    
    result_to_file = name[0:4] + "," + result + "="+calcu_str + "\n"
    map_file.write(result_to_file)
    #print(result_to_file)
    i=i+1
map_file.close()






