from tkinter import *
from page.course import CoursePage
from page.exercise import ExercisePage
from page.demo import MainPage

class App(MainPage, CoursePage, ExercisePage):

    def __init__(self):
        self.root = Tk()
        self.goMainPage()

    def goMainPage(self):
        self.root.destroy()
        MainPage.__init__(self, goCoursePage=self.goCoursePage, goExercisePage=self.goExercisePage)

    def goCoursePage(self):
        self.root.destroy()
        CoursePage.__init__(self, goMainPage=self.goMainPage)

    def goExercisePage(self):
        self.root.destroy()
        ExercisePage.__init__(self, goMainPage=self.goMainPage)

if __name__ == '__main__':
    App()