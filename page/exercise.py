# coding=utf-8

from tkinter import *
import pandas as pd
import random

class ExercisePage(object):
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
        self.frameCenter1 = Frame(width=300, height=275)
        self.frameCenter2 = Frame(width=300, height=275, bg="orange")
        self.frameBelow = Frame(width=600, height=275)

        self.title = Label(self.frameTop, text="倉頡拆字練習", font=('microsoft yahei', 24, 'bold'))
        self.back = Button(self.frameTop, text="返回主頁", font=('microsoft yahei', 16, 'bold'), command=self.backMainPage)

        self.bigWord = Label(self.frameCenter1, text="?", font=('JetBrains Mono', 170, 'bold'))

        self.inputlist = "？？？？？"

        self.inputLable = Label(self.frameBelow, text="請輸入倉頡碼:", font=('microsoft yahei', 24, 'bold'))
        self.textLable = Label(self.frameBelow, text=self.inputlist, font=('microsoft yahei', 24, 'bold'))
        self.inputLable2 = Label(self.frameBelow, text="倉頡字母提示:", font=('microsoft yahei', 24, 'bold'))
        self.textLable2 = Label(self.frameBelow, text=self.inputlist, font=('microsoft yahei', 24, 'bold'))
        self.inputLable3 = Label(self.frameBelow, text="英文字母提示:", font=('microsoft yahei', 24, 'bold'))
        self.textLable3 = Label(self.frameBelow, text=self.inputlist, font=('microsoft yahei', 24, 'bold'))
        self.startButton = Button(self.frameBelow, text="提示", font=('microsoft yahei', 16, 'bold'))

        self.n = 0

        data = pd.read_csv("wordV2.csv")

        self.dict = {"a": "日", "b": "月", "c": "金", "d": "木",
                "e": "水", "f": "火", "g": "土", "h": "竹",
                "i": "戈", "j": "十", "k": "大", "l": "中",
                "m": "一", "n": "弓", "o": "人", "p": "心",
                "q": "手", "r": "口", "s": "尸", "t": "廿",
                "u": "山", "v": "女", "w": "田", "y": "卜",
                "x": "難"}

        def inputEvent(event):
            temp = ""
            if "a" <= event.char <= "y":
                temp = self.dict[event.char]
                if 0 <= self.n <= 4:
                    tList = list(self.textLable['text'])
                    tList[self.n] = temp.decode('utf-8')
                    self.textLable['text'] = "".join(tList)
                    self.n = self.n + 1
                else:
                    self.n = 5

        def backEvent(event):
            if self.n >= 0:
                if self.n > 0:
                    self.n = self.n - 1
                tList = list(self.textLable['text'])
                tList[self.n] = "？".decode('utf-8')
                self.textLable['text'] = "".join(tList)
            elif self.n < 0:
                self.n = 0

        def simpleEvent(event):

            self.textLable['text'] = "？？？？？"
            self.n = 0
            x = random.randint(1, 78163)
            word = data['word'][x]
            answer = data['answer'][x]
            self.textLable3['text'] = answer
            answer_list = list(answer)
            answer_list2 = []
            for y in answer_list:
                if "a" <= y <= "y":
                    answer_list2.append(self.dict[y])
            answer = "".join(answer_list2)
            #if(self.bigWord['text'] == "?"):
            self.bigWord['text'] = unicode(word, encoding="utf-8")
            self.textLable2['text'] = answer
            #print(word)
            #print(self.bigWord['text'])

        self.flag = 0

        def hint():
            answer = self.textLable2['text']
            if self.flag == 1:
                pass




        self.root.bind("<Key>", inputEvent)
        self.root.bind("<BackSpace>", backEvent)
        self.root.bind("<space>", simpleEvent)

        self.frameTop.grid(row=0, column=0, columnspan=2)
        self.frameCenter1.grid(row=1, column=0, sticky="w")
        self.frameCenter2.grid(row=1, column=1, sticky="w")
        self.frameBelow.grid(row=2, column=0, columnspan=2)
        self.title.grid(row=0, column=0)
        self.back.grid(row=0, column=1)
        self.bigWord.grid(row=0, column=0)
        self.inputLable.grid(row=0, column=0)
        self.textLable.grid(row=0, column=1)
        self.inputLable2.grid(row=1, column=0)
        self.textLable2.grid(row=1, column=1)
        self.inputLable3.grid(row=2, column=0)
        self.textLable3.grid(row=2, column=1)
        self.startButton.grid(row=3, column=0)


        self.frameTop.grid_propagate(0)
        self.frameCenter1.grid_propagate(0)
        self.frameCenter2.grid_propagate(0)
        self.frameBelow.grid_propagate(0)

        self.root.mainloop()

if __name__ == '__main__':
    root = Tk()
    ExercisePage(None)
    root.mainloop()