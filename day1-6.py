# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 15:22:10 2020

@author: user
"""

m=int(input('m'))
e=int(input('e'))
if m>=90 and e>=90:
    print('有獎品')
elif m<60 or e<60:
    print('再加油')
elif m<60 and e<60:
    print('要補考')
