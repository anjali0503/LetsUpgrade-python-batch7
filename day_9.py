# -*- coding: utf-8 -*-
"""day:9.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Nr4yHJStRgbYNWtRMu6fO0Wx-5kd4nIE

#Assignment.no:1  Day:9
"""

# Commented out IPython magic to ensure Python compatibility.
# %%writefile prime_number
# '''
# its a function to check prime number
# '''
# def prime(num_n):
#   '''
#   this is a prime function
#   '''
#     if num_n == 1 :
#         return False
#     for i in range(2, num_n) :
#         if num_n%i == 0 :
#             return False
#     return True

! pip install pylint

! pylint "prime_number"

"""#Assignment 2 Day:9"""

print(" enter 'q' to quit,")
print("enter the intervals(starting and ending number):")
start=input();
if start=='x':
  exit();
else:
  end=input();
  lower=int(start);
  upper=int(end);
  for num in range(lower, upper+1):
    tot=0;
    temp=num;
    while temp!=0:
      dig=temp%10;
      tot+=dig**3;
      temp//=10;
    if num==tot:
      print(num);