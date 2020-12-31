#-*- coding:utf-8 -*-

# 项目名称：Photoshop
# 程序名称：main.py
# 功能：python实现图像处理功能
# 作者：广东工业大学信息工程学院18级信息工程1班3118003290曾胤宁
# 参考文档：CSDN，opencv官方文档，numpy官方文档
# 运行该代码前置条件：python安装numpy以及opencv-python库
# 最后更新时间：2020-12-31
# 该程序需求：数字图像处理作业
# 可执行文件(mian.exe)位置：.\dist\main.exe

from tkinter import *
from tkinter import filedialog
import tkinter.messagebox
import numpy as np
import cv2 as cv


global src
global new

def main():
    def selectJpgfile():
        global src,new
        sfname = filedialog.askopenfilename(title='选择jpg文件', filetypes=[('JPG', '*.jpg'), ('All Files', '*')])
        print(sfname)
        text1.delete(0,END)
        text1.insert(INSERT, sfname)
        src = cv.imread(sfname)
        cv.imshow('Source img', src)

    #关闭窗口
    def closeThisWindow():
        root.destroy()

    #图片底片化
    def doNegative():
        global src, new
        try:
            tkinter.messagebox.showinfo('提示', '实现图片底片化')

            #此处实现图像转变算法
            new = 255 - src

            cv.imshow('Nagative',new)
        except:
            tkinter.messagebox.showinfo('错误', '尚未有源图像')

    #灰度增强
    def doGrayEnhance():
        global src, new
        tkinter.messagebox.showinfo('提示', '利用gamma=0.5实现灰度增强，如果是RGB则自动转换成灰度图像')
        try:
            new = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
            # 归1
            Cimg = new / 255
            # 伽玛变换
            gamma = 0.5
            new = np.power(Cimg, gamma)
            cv.imshow('GrayEnhance', new)
        except:
            tkinter.messagebox.showinfo('错误', '尚未有源图像')

    #中值滤波
    def doMidValueFliter():
        global src, new
        try:
            tkinter.messagebox.showinfo('提示', '对图像使用中值滤波')
            new = cv.medianBlur(src,5)
            cv.imshow('MidValueFliter', new)
        except:
            tkinter.messagebox.showinfo('错误', '尚未有源图像')

    # 双边滤波
    def doBilateralFilter():
        global src, new
        try:
            tkinter.messagebox.showinfo('提示', '使用双边滤波')
            new = cv.bilateralFilter(src, 0,100,15)
            cv.imshow('BilateralFilter', new)
        except:
            tkinter.messagebox.showinfo('错误', '尚未有源图像')

    #生成灰度图像
    def doGrayImage():
        global src, new
        try:
            tkinter.messagebox.showinfo('提示', '生成灰度图像')
            new = cv.cvtColor(src,cv.COLOR_BGR2GRAY)
            cv.imshow('GrayImage', new)
        except:
            tkinter.messagebox.showinfo('错误', '尚未有源图像')

    #直方图均衡化
    def doHistBalance():
        global src, new
        try:
            tkinter.messagebox.showinfo('提示', '自动转化为灰度图并使用直方图均衡')
            temp = cv.cvtColor(src,cv.COLOR_BGR2GRAY)
            new = cv.equalizeHist(temp)
            cv.imshow('HistBalance', new)
        except:
            tkinter.messagebox.showinfo('错误', '尚未有源图像')

    #保存修改后图像
    def imgSafe():
        global new
        if new.any()==0:
            tkinter.messagebox.showinfo('错误', '执行此操作请先生成一副图像')
        else:
            temp = filedialog.askdirectory(title='选择保存路径')
            temp = temp + 'New.jpg'
            try:
                cv.imwrite(temp, new)
            except:
                tkinter.messagebox.showinfo('提示', '保存失败')
            else:
                tkinter.messagebox.showinfo('提示', '保存成功')


    # 初始化
    global new
    root = Tk()
    new = 0

    # 设置窗体标题
    root.title('Python实现photoshop部分功能')

    # 设置窗口大小和位置
    root.geometry('500x300+570+200')

    label0 = Label(root,text='作者：信息工程1班3118003290曾胤宁')
    label1 = Label(root, text='请选择文件:')
    text1 = Entry(root, bg='white', width=45)
    button1 = Button(root, text='浏览', width=10, command=selectJpgfile)
    button2 = Button(root, text='底片化', width=10, command=doNegative)
    button3 = Button(root,text='灰度增强',width=10,command=doGrayEnhance)
    button4 = Button(root, text='中值滤波', width=10, command=doMidValueFliter)
    button5 = Button(root, text='双边滤波', width=10, command=doBilateralFilter)
    button6 = Button(root, text='灰度化图像', width=10, command=doGrayImage)
    button7 = Button(root, text='直方图均衡化', width=10, command=doHistBalance)
    button8 = Button(root, text='保存图像', width=10, command=imgSafe)
    button9 = Button(root, text='退出', width=10, command=closeThisWindow)

    label0.pack()
    label1.pack()
    text1.pack()
    button1.pack()
    button2.pack()
    button3.pack()
    button4.pack()
    button5.pack()
    button6.pack()
    button8.pack()
    button7.pack()
    button9.pack()

    label0.place(x=130,y=60)
    label1.place(x=30, y=110)
    text1.place(x=100, y=110)
    button1.place(x=390, y=106)
    button2.place(x=55, y=180)
    button3.place(x=155, y=180)
    button4.place(x=255, y=180)
    button5.place(x=355, y=180)
    button6.place(x=55,y=220)
    button7.place(x=155,y=220)
    button8.place(x=255,y=220)
    button9.place(x=355, y=220)
    root.mainloop()


if __name__ == "__main__":
    main()