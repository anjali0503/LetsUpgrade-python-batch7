# -*- coding: utf-8 -*-
"""ASSIGNMENT:01 DAY :4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15lEh6Qa7-o-CAGy-XKzNhhbXc_7dsuoM
"""

#Print the first ARMSTRONG NUMBER in range of 1042000 to 702648265 and exit the loop as soon you encounter the first armstrong number

lower=1042000
upper=702648265
for n in range(lower,upper+1):
        order=len(str(n))
        sum=0
        temp=n
        while temp>0:
            digit=temp%10
            sum+=digit**order
            temp//=10
            break
        if n==sum:
            print(n)