from tkinter import *
import tkinter as tk


class mainpage:
    def __init__(self, master):

        self.root = master
        self.root.title("会员管理软件")
        self.root.geometry("500x300")


if __name__ == "__main__":
    # 初始化
    root = tk.Tk()
    mainpage(root)
    # 循环刷新界面
    root.mainloop()
