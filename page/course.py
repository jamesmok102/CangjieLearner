# coding=utf-8

from tkinter import *
from tkinter.scrolledtext import *

class CoursePage(object):

    def backMainPage(self):
        self.goMainPage()

    def __init__(self, goMainPage):
        self.goMainPage = goMainPage

        self.root = Tk()
        self.root.title("倉頡之星2021")
        self.root.geometry("600x600")
        self.root.configure(background='white')
        self.root.resizable(False, False)

        self.frameTop = Frame(width=600, height=50)
        self.frameBelow = Frame(width=600, height=550, bg="blue")

        self.title = Label(self.frameTop, text="倉頡教學", font=('microsoft yahei', 24, 'bold'))
        self.back = Button(self.frameTop, text="返回主頁", font=('microsoft yahei', 16, 'bold'), command=self.backMainPage)
        self.text_area = ScrolledText(self.frameBelow, height=25, width=58, font=("Times New Roman", 15))

        with open('course.txt') as f:
            for line in f:
                self.text_area.insert('end',line)


        self.frameTop.grid(row=0, column=0)
        self.frameBelow.grid(row=1, column=0)
        self.title.grid(row=0, column=0)
        self.back.grid(row=0, column=1)
        self.text_area.grid(row=0, column=0)

        self.frameTop.grid_propagate(0)
        self.frameBelow.grid_propagate(0)

        self.root.mainloop()

if __name__ == '__main__':
    root = Tk()
    CoursePage(None)
    root.mainloop()