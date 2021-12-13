# 倉頡學習器

## 選題背景

倉頡，是一個字形輸入法，我一直以都是用這個輸入法的，但知道它的人少之又少。這款輸入法，是公認學習難度最高的，除此之外輔助學習倉頡的網頁或軟件太少了，直接勸退初學者，所以有了製作這款件的動機。

其次，其實我想起了以前用過的**倉頡之星**，只不過到了Windows 10以后就無法打開了，可能是不兼容了，所以才想到做了一個軟件給自己練習用。

最后，正當我有這個想法時，剛好學校的Python課有課程設計，所以我打算使用Python做出來。

## 方案論證

這次打算做成Python圖形化工具，所以使用了**Tkinter**。同時它也需要引用詞庫，這樣才能練習拆碼，這個詞庫有78,163個字，來自小狼毫輸入法(軟件)的詞庫，如何引用詞庫?使用了**Pandas**包讀取csv文件。如何隨機抽取出要拆的碼?當然是使用了**Random**包了

所以，這次使用的包有:
* Tkinter
* Pandas
* Random

### 功能

這次，我只做了兩個功能，第一個功能是**輸入法教學**，主要是用來介紹輸入法的，其實就是顯示文字。第二個功能就**拆字練習**，本軟件的核心功能，它首先會隨機顯示一個字出來，然后你可以直接在鍵盤上輸入即可，無需換成倉頡輸入法，直接使用英文鍵盤就可以了，同時它也有一個提示功能，如果不會拆字時可以看提示，基于方便演示，我直接打開了提示功能

### 軟件設計

首先，軟件打開時是使用`App.py`，它的功能主要用來做page的forward功能，它分別有三個pages，分別是MainPage, CoursePage, ExercisePage。MainPage提供了兩個按鈕，輸入法教學的按鈕，前往CoursePage，拆字練習的按鈕，前住ExercisePage。

如何進行前往別的Page?把當前的視窗destroy，然后把新的視窗init出來就可以，最簡單直接的方法

`App.py`只有forward功能，沒有圖形介面的，所以打開`App.py`時會直接轉到`demo.py`，它才是主介面，有實現圖形化介面

如果你前住CoursePage，相當於前住`course.py`，有一個按鈕和ScrolledText，按鈕是用來返回主頁的，而ScrolledText就是帶有滾動條的文字區域，顯示文字用

如果你前住ExercisePage，相當於前住`exercise.py`，有一個按鈕，顯示單字區域，輸入框，提示框

如何實現輸入功能?Tkinter提供了Bind方法，當你按了某個鍵，它就會運行你所綁定的方法，總共有三個方法，inputEvent, backEvent, simpleEvent。inputEvent就是把你輸入的英文字母變成倉頡字母，顯示在輸入框內。backEvent就是按下Backspace時退回輸入框的字。simpleEvent就是當你輸入全部倉頡碼時，按下空格進行驗證，若正确，會顯示下一個字，否則沒有任何動作

## 過程論證

展示出核心代碼，直接說明如何實現功能

`App.py`
```python=
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
```
在__init__的方法中，它默認是去到主頁的，若是從其他頁面轉回來的，則會轉到別的頁面

### 圖形化顯示

```python=
self.root = tk.Tk()
self.root.title("仓颉学习器")
self.root.geometry("600x600")
self.root.configure(background='white')
self.root.resizable(False, False)
```
設定並顯示標題，視窗大小，白色背景，禁止拉伸視窗

```python=
self.pixel = tk.PhotoImage(width=1, height=1)
```
某些組件不是以pixel為單位，這行代碼的意思是把組件設定作以pixel為單位

```python=
self.frameLeft = tk.Frame(width=100, height=600, bg="white")
```
划分並設定每個區域的大小，而它們的背景都是白色

```python=
tk.Button(self.frameCenter2, text="倉頡教學", width="400", height="100", font=('microsoft yahei', '30', 'bold'), image=self.pixel,
compound="center", command=self.goCoursePage).grid(row=0)
```
設定按鈕的所在區域，文字，大小，字體，位置，調用方法

```python=
self.frameLeft.grid(row=0, column=0, rowspan=5)
```
設定所在位置

```python=
self.frameLeft.grid_propagate(0)
```
區域固定不動

```python=
self.root.mainloop()
```
視窗顯示

### 帶有滾動條的文字區域
```python=
self.text_area = ScrolledText(self.frameBelow, height=25, width=58, font=("Times New Roman", 15))
```
初始化文字區域

```python=
with open('course.txt') as f:
    for line in f:
        self.text_area.insert('end',line)
```
讀取大量文字並插入到文字區域中

### 鍵盤讀取

```python=
self.root.bind("<Key>", inputEvent)
self.root.bind("<BackSpace>", backEvent)
self.root.bind("<space>", simpleEvent)
```
根據不同的鍵位而調用不同的方法

```python=
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
```
首先，會把英文字母轉成倉頡字母，然后會查看輸入框是否5個字內，因為每個字的倉頡碼最多只有5個，讀取text，把倉頡字母從utf-8解碼，加入到text內，如果己有5個字，則不進行任何動作

```python=
def backEvent(event):
    if self.n >= 0:
        if self.n > 0:
            self.n = self.n - 1
        tList = list(self.textLable['text'])
        tList[self.n] = "？".decode('utf-8')
        self.textLable['text'] = "".join(tList)
    elif self.n < 0:
        self.n = 0
```
同理，改變text內的文字，若輸入框內己經沒有字了，不進行任何動作

```python=
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
```
把文字框的倉頡碼和字庫里的倉頡碼進行對比，如果正确，則顯示下一個字，否則不進行任何動作

### 結果展示

結果展示是必要的

主頁
![](https://i.imgur.com/Ab0uvlB.png)

教學頁面
![](https://i.imgur.com/7YRDHqA.png)

練習頁面
![](https://i.imgur.com/JcPkOML.png)

按空格開始
![](https://i.imgur.com/Y5HgZbZ.png)

輸入正确后顯示下一個字
![](https://i.imgur.com/k3iSQlB.png)



