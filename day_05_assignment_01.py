# -*- coding: utf-8 -*-
"""Day.05 Assignment.01.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bIZ4JPAjbpZifZ1nlDnG-pucI8o8r--b
"""

# WAP to indentify sub list [1,1,5] is there  in the given list in the same order , if yes print "its match" if no then print "its gone" in function.
lst=[1,4,3,5,7,1,6,5,6]
sublst=[1,1,5]

for i in range(len(lst)):
  if lst[i]==sublst[0]:
    for j in range(i+1,len(lst)):
      if lst[j]==sublst[1]:
        for k in range(j+1,len(lst)):
          if lst[k]==sublst[2]:
            print("its match")
            break
        break
    break
  else:
      print("its gone")