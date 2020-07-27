from PIL import Image
import os
import shutil

def haha(path, backname, pathorg):
    im = Image.open(path)  # 返回一个Image对象

    # os模块中的path目录下的getSize()方法获取文件大小，单位字节Byte
    size = os.path.getsize(path) / 1024  # 计算图片大小即KB
    print(size)
    # size的两个参数
    width, height = im.size[0], im.size[1]
    # 用于保存压缩过程中的temp路径,每次压缩会被不断覆盖
    newPath = pathorg + "/temp/" + "temp" + backname + ".jpg"
    while size > 350:
        width, height = round(width * 0.9), round(height * 0.9)
        print(width, height)
        im = im.resize((width, height), Image.ANTIALIAS)
        im.save(newPath)
        size = os.path.getsize(newPath) / 1024

    # 压缩完成
    im.save(pathorg + "compressed/" + backname + '.jpg')


# 通过使用循环进行改名
def convertrgb(path,num,pathorg):
    try:
        im = Image.open(path)
        rgb_im = im.convert('RGB')
        rgb_im.save(pathorg + "/" + str(num) +'.jpg')
    except:
        print('fail失败')


def rename(pathorg, formatt, nms):  # 重命名函数
    path = pathorg + '/compressed'
    n = 0
    fileList = os.listdir(path)
    for i in fileList:
        oldname = path + os.sep + fileList[n]  # os.sep添加系统分隔符
        newname = path + os.sep + nms + str(n + 1) + '.' + formatt
        os.rename(oldname, newname)  # 用os模块中的rename方法对文件改名
        print(oldname + '======>' + newname)
        n += 1


# rename('compressed', 'jpg','食来食往')


def excute(path, formatt, nms, pathorg):

    try:
        os.mkdir(pathorg + '/compressed')

    except:
        print("compressed文件夹已存在,系统不会创建新文件夹")
    try:
        os.mkdir(pathorg + '/temp')
    except:
        print("temp文件夹已存在，系统不会创建新的")
    fileList = os.listdir(path)
    i = 1

    for picname in fileList:



        haha(path + '/' + picname, str(i) + 'compressed', pathorg)
        i += 1

    rename(pathorg, formatt, nms)
    shutil.rmtree(pathorg + "temp")
    print(">>>>>>>>>>>>>>主人，任务完成啦！！！")


#excute('C://pythonimg/testimg', 'jpg', 'dabinjia', 'C://pythonimg/')
excute(input('图片存放路径(最后不要带斜杠)：'),input('格式：'),input('餐厅名字:'),input('源目录路径(最后不要忘记带斜杠！)：'))
