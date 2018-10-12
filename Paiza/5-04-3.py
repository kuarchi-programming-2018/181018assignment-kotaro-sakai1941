# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 23:19:31 2018

@author: sakai kotaro
"""

# ループで合計を計算しよう

points = {"国語" : 70, "算数" : 35, "英語" : 52}
sum = 0
# この下で、辞書の値の合計をループで計算してみよう
for a in points:
    sum += points[a]
print(int(sum))
