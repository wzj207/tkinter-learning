from tkinter import *
from PIL import ImageTk,Image
import numpy as np
import matplotlib.pyplot as plt
import win32api,win32con

# 获得屏幕分辨率
x_pixels = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)  # 获得屏幕分辨率X轴
y_pixels = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)  # 获得屏幕分辨率Y轴

root = Tk()
root.title('Learn Tkinter')
root.iconbitmap('./images/favicon.ico')  # add icon
# root.geometry('650x260')
root.geometry(str(x_pixels)+'x'+str(y_pixels)+'+0+0')
# root.geometry(str(int(x_pixels*3/4))+'x'+str(int(y_pixels/2))+'+0+0')

# house_prise = np.random.normal(200000, 2500, y 5000)

x = np.array([1,2,3,4,5,6,7])
y = x**2
def graph(x,y):
    plt.plot(x,y)
    plt.show()

my_button = Button(root, text='Graph It!', command=lambda :graph(x,y))
my_button.pack()

root.mainloop()




