from tkinter import *
import tkinter as tk


class mainpage:
    def __init__(self, master):

        self.root = master
        self.root.title("会员管理软件")
        self.root.geometry("500x300")

    def creatpage(self):
        menubar = tk.Menu(self.root)
        menubar.add_command(label="添加会员", command="")
        menubar.add_command(label="会员列表", command="")
        menubar.add_command(label="删除会员", command="")
        menubar.add_command(label="关于软件", command="")


if __name__ == "__main__":
    # 初始化
    root = tk.Tk()
    mainpage(root)
    # 循环刷新界面
    root.mainloop()
