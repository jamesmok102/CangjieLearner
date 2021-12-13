# coding=utf-8
import pandas as pd
import random

data = pd.read_csv("../wordV2.csv")
for x in range(0,11):
    n = random.randint(1, 78163)
    text = data['word'][n] + ":" + data['answer'][n]
    print(n)
    print(unicode(text, encoding="utf-8"))

