import win32gui
import win32api
import win32con
import os
import time
import threading
import win32file


def run_exe():
    base_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    print(base_dir)
    # 返回base_dir指定的文件夹包含的文件或文件夹的名字的列表
    base_dir1 = os.listdir(base_dir)
    for filename in base_dir1:
        print(filename)
        if filename.endswith(".exe"):
            print(filename)
             # 找到文件所在位置
            file_path =os.path.join(base_dir,filename)
            print("old_file is {}".format(file_path))
            os.system(file_path)

def cover_install():
    #获取窗口句柄
    time.sleep(10)
    hwd = win32gui.FindWindow("FrmSetup1Wnd", "安装向导")
    time.sleep(3)
    #获取窗口左上角和右下角坐标
    x1, y1, x2, y2 = win32gui.GetWindowRect(hwd)
    point = (x1+293, y1+288)
    win32api.SetCursorPos(point) #鼠标定位
    #执行左单击
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    time.sleep(2)
    hwd1 = win32gui.FindWindow("MessageBoxWnd", "提示")
    time.sleep(2)
    x11, y11, x22, y22 = win32gui.GetWindowRect(hwd1)
    point1 = (x11+125, y11+159)
    win32api.SetCursorPos(point1)
    #执行左单击
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    time.sleep(2)
    # 关闭窗口立即体验窗口
    for i in range(0, 300):
        time.sleep(1)
        hwd3 = win32gui.FindWindow("FrmSetup3Wnd","安装向导")
        time.sleep(2)
        if hwd3 != 0:
            time.sleep(2)
            win32gui.SendMessage(hwd3, win32con.WM_CLOSE, 0, 0)
            break

def delete_exe():
    base_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    print(base_dir)
    # 返回base_dir指定的文件夹包含的文件或文件夹的名字的列表
    base_dir1 = os.listdir(base_dir)
    for filename in base_dir1:
        print(filename)
        if filename.endswith(".exe"):
            print(filename)
             # 找到文件所在位置
            file_path =os.path.join(base_dir,filename)
            print("old_file is {}".format(file_path))
            os.remove(file_path)
            print("删除成功")

t1 = threading.Thread(target=run_exe)
t2 = threading.Thread(target=cover_install)
t3 = threading.Thread(target=delete_exe)
t1.start()
time.sleep(5)
t2.start()
t1.join()
time.sleep(3)
t3.start()
time.sleep(5)
if os.path.exists("C:\Program Files (x86)\Actoma") and os.path.exists("C:\Program Files (x86)\Actoma\Actoma.exe"):
    print("安装成功")
    os.system("python -m pytest")
else:
    raise FileNotFoundError("安装失败")

