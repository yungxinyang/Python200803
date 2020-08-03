# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 14:21:36 2020

@author: user
"""

score=input('score')
score=int(score)
if score>=0 and score<=100:
    print('score')
    if score>=90:
        print('A')
    elif score>=80:
        print('B')
    elif score>=70:
        print('C')
    elif score>=60:
        print('D')
    else:
        print("E")
else:
    print('error')
