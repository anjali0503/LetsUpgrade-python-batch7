# -*- coding: utf-8 -*-
"""Day-6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13tqkl8noFNqVJGy52AtWh5kMqD1N680H

Day-6 (Assignment-1)
"""

class bank():
    ownername=""
    balance=0

    def deposit(self,amount):
        self.balance=self.balance+amount
        print("balance is ",self.balance)
    
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance=self.balance-amount
            print("balance is ",self.balance)
        else:
            print("insufficient funds!")

deposits=bank()

deposits.deposit(1000)

deposits.withdraw(1001)

deposits.withdraw(100)

"""Day-6 (Assignment-2)"""

import math

class Cone:
    radius=0
    height=0
    def __init__(self,radius,height):
        self.radius=radius
        self.height=height
        print("initiated class object")
    def volume(self):
        volume=3.14*self.radius*self.radius*(self.height//3)
        print("volume is ",volume)
    def surfacearea(self):
        area=(3.14*self.radius)*(self.radius+(math.sqrt(self.height*self.height+self.radius*self.radius)))
        print("surface area is ",area)

cone=Cone(3,4)

cone.volume()

cone.surfacearea()