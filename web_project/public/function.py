# -*- coding: utf-8 -*-
import os
import psutil,time
from PIL import ImageGrab
from datetime import *
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=14)
import string

# 截图函数
def insert_img(file_name):

    base_dir = os.path.dirname(os.path.dirname(__file__))
    base_dir = str(base_dir)
    base = base_dir.split('test_case')[0]
    file_path = base + "report\\image\\" + file_name
    im = ImageGrab.grab()
    im.save(file_path,"png")

'''打印系统内存信息到txt文档中'''
#查看系统全部进程
def memory_monitoring():
    print("memory_monitoring")
    pidList = psutil.pids()

    pidListAll = []
    for eachPid in pidList:
        p = psutil.Process(eachPid)
        if p.name() == "Actoma.exe":
            pidListAll.append(eachPid)
            # print (len(pidListAll))
    i = 0
    if pidListAll != []:
        while True:
            try:
                fileHandle = open('Log.txt', 'a')
                # NowTime=str(datetime.now())
                NowTime = time.strftime("%Y-%m-%d %H:%M:%S")
                fileHandle.write("\n")
                i = i + 1
                print(i)
                print(p.name())
                fileHandle.write(str(i))
                fileHandle.write(",")
                fileHandle.write(str(NowTime))

                print(NowTime)

                for pid in range(0, len(pidListAll)):
                    p = psutil.Process(pidListAll[pid])
                    if p:
                        total_memory = (psutil.virtual_memory())[0]
                        percent = p.memory_percent(memtype="uss")     #进程p占用的内存比
                        memValue = (percent / 100) * total_memory
                        print(memValue / 1024 / 1024)
                        cpercent = p.cpu_percent(None)
                        print(p.cpu_percent(None))
                        fileHandle.write(",")
                        fileHandle.write(str(memValue / 1024 / 1024))
                        fileHandle.write("")
                    else:
                        " no error Process Named: %s" % ("Actoma.exe")
                        break

                print("")
                time.sleep(3)
            except:
                print("error")
                break
            finally:
                fileHandle.close()

def get_data():
    inFile = open("Log.txt",'r')  #以只读方式打开某fileName文件
    lineList = inFile.readlines()
    print(lineList)
    # print(lineList)


    # 定义两个空list，用来存放文件中的数据
    x = []
    y = []
    z = []
    j = []
    q = []
    p = []

    for line in lineList:
        lineList = line.split(',')
        inFile.close()
        # print(lineList)
        x.append(lineList[0])
        y.append(lineList[1])
        z.append(lineList[2])
        j.append(lineList[3])
        q.append(lineList[4])
        p.append(lineList[5])

    plt.plot(x,z,'r')
    plt.plot(x,j,'g')
    plt.plot(x,q,'b')
    plt.plot(x,p,'k')


    plt.title(u'内存大小曲线图',fontproperties=font)
    plt.xlabel(u'检测次数(s)',fontproperties=font)
    plt.ylabel(u'内存大小（M）',fontproperties=font)

    plt.show()