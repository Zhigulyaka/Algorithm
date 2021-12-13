# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 12:16:10 2021

@author: 1
"""

import subprocess as sbp
import matplotlib.pyplot  as plt
from scipy.signal import savgol_filter

def handinput():
    ownWord, searchWord="",""
    print("Введите исходную строку: ", end="")
    ownWord=input()
    print("Введите искомую строку: ", end="")
    searchWord=input()
    result =sbp.run(r"C:\Users\1\source\repos\Algorithm\Debug\Algorithm.exe" + " " + str(0) + " " + ownWord + " " + searchWord + " " + str(0), stdout=sbp.PIPE)
    r=str(result.stdout)
    print(r)

def alphabetinput():
    letters =""
    countOwn, countSearch = 0, 0
    print("Введите буквы алфавита подряд без пробела: ", end="")
    letters=input()
    print("Введите длину исходной строки: ", end="")
    countOwn=input()
    print("Введите длину искомой строки: ", end="")
    countSearch = input()
    result =sbp.run(r"C:\Users\1\source\repos\Algorithm\Debug\Algorithm.exe" + " " + str(4) + " " + letters + " " + countOwn + " " + countSearch, stdout=sbp.PIPE)
    r=str(result.stdout)
    print(r)

def bigstringinput():
    ownWord, searchWord ="", ""
    countOwn, countSearch = 0, 0
    print("Введите часть исходного слова: ", end="")
    ownWord=input()
    print("Введите часть искомого слова: ", end="")
    searchWord=input()
    print("Введите количество повторений исходной строки: ", end="")
    countOwn=input()
    print("Введите количество повторений искомой строки: ", end="")
    countSearch = input()
    result =sbp.run(r"C:\Users\1\source\repos\Algorithm\Debug\Algorithm.exe" + " " + str(5) + " " + ownWord + " " + searchWord + " " + countOwn + " " + countSearch, stdout=sbp.PIPE)
    r=str(result.stdout)
    print(r)
    
def grafick(t_x,t1_y,t2_y,name):
    t1_y = savgol_filter(t1_y, 51, 3)
    t2_y=savgol_filter(t2_y, 51, 3)
    plt.figure(name[-1],figsize=(5,5))
    plt.title(name)
    plt.plot(t_x,t1_y, 'r', label='TrivialAlgorithm')
    plt.plot(t_x,(t2_y),'b', label="KMPAlgorithm")
    plt.legend()
    plt.show()

   
def test1():
    own, search = 'ab', 'ab'
    t1_x,t1_y,t2_y=[],[],[]
    for i in range(1,1011,10):
        result =sbp.run(r"C:\Users\1\source\repos\Algorithm\Debug\Algorithm.exe" + " " + str(1) + " " + own + " " + search + " " + str(i), stdout=sbp.PIPE)
        r=str(result.stdout)
        print(r)
        t1_x.append(i)
        t1_y.append(float(r[2:r.find(' ')]))
        t2_y.append(float(r[r.find(' ')+1:len(r)-1]))
    grafick(t_x=t1_x,t1_y=t1_y,t2_y=t2_y,name="Test 1")
  
def test2():
    own,search ="ab","a"
    t1_x,t1_y,t2_y=[],[],[]
    for i in range(1,1010001,10000):
        result =sbp.run(r"C:\Users\1\source\repos\Algorithm\Debug\Algorithm.exe" + " " + str(2) + " " + own + " " + search + " " + str(i), stdout=sbp.PIPE)
        r=str(result.stdout)
        print(r)
        t1_x.append(i)
        t1_y.append(float(r[2:r.find(' ')]))
        t2_y.append(float(r[r.find(' ')+1:len(r)-1]))
    grafick(t_x=t1_x,t1_y=t1_y,t2_y=t2_y,name="Test 2")

def test3():
    own,search ="aaaaab","aaaaa"
    t1_x,t1_y,t2_y=[],[],[]
    for i in range(1,1000000+1,10000):
        result =sbp.run(r"C:\Users\1\source\repos\Algorithm\Debug\Algorithm.exe" + " " + str(3) + " " + own + " " + search + " " + str(i), stdout=sbp.PIPE)
        r=str(result.stdout)
        print(r)
        t1_x.append(i)
        t1_y.append(float(r[2:r.find(' ')]))
        t2_y.append(float(r[r.find(' ')+1:len(r)-1]))
    grafick(t_x=t1_x,t1_y=t1_y,t2_y=t2_y,name="Test 3") 
    
test1()
test2()
test3()