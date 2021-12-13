# coding=utf-8
from PIL import Image, ImageTk
import tkinter as tk
from page import course, exercise

class MainPage():

    def __init__(self, goCoursePage, goExercisePage):
        self.goCoursePage = goCoursePage
        self.goExercisePage = goExercisePage

        self.root = tk.Tk()
        self.root.title("倉頡之星2021")
        self.root.geometry("600x600")
        self.root.configure(background='white')
        self.root.resizable(False, False)

        self.pixel = tk.PhotoImage(width=1, height=1)

        self.frameLeft = tk.Frame(width=100, height=600, bg="white")
        self.frameCenter1 = tk.Frame(width=400, height=100, bg="white")
        self.frameCenter2 = tk.Frame(width=400, height=100, bg="white")
        self.frameCenter3 = tk.Frame(width=400, height=100, bg="white")
        self.frameCenter4 = tk.Frame(width=400, height=100, bg="white")
        self.frameCenter5 = tk.Frame(width=400, height=200, bg="white")
        self.frameRight = tk.Frame(width=100, height=600, bg="white")

        tk.Button(self.frameCenter2, text="倉頡教學", width="400", height="100", font=('microsoft yahei', '30', 'bold'), image=self.pixel,
                  compound="center", command=self.goCoursePage).grid(row=0)
        tk.Button(self.frameCenter4, text="倉頡拆碼練習", width="400", height="100", font=('microsoft yahei', '30', 'bold'), image=self.pixel,
                  compound="center", command=self.goExercisePage).grid(row=0)

        self.frameLeft.grid(row=0, column=0, rowspan=5)
        self.frameCenter1.grid(row=0, column=1, sticky="n")
        self.frameCenter2.grid(row=1, column=1, sticky="n")
        self.frameCenter3.grid(row=2, column=1, sticky="n")
        self.frameCenter4.grid(row=3, column=1, sticky="n")
        self.frameCenter5.grid(row=4, column=1, sticky="n")
        self.frameRight.grid(row=0, column=2, rowspan=5)

        self.frameLeft.grid_propagate(0)
        self.frameCenter1.grid_propagate(0)
        self.frameCenter2.grid_propagate(0)
        self.frameCenter3.grid_propagate(0)
        self.frameCenter4.grid_propagate(0)
        self.frameCenter5.grid_propagate(0)
        self.frameRight.grid_propagate(0)

        self.root.mainloop()

if __name__ == '__main__':
    root = tk.Tk()
    MainPage()
    root.mainloop()


