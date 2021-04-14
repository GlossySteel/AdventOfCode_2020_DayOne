# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 18:34:10 2021

@author: Joseph Kharzo
"""

import pandas as pd

df = pd.read_csv("Numbers.csv")

numbers = df['Numbers']

firstNumber = 0
secondNumber= 0

i = 0
j = 1

while i < numbers.size:
    j = i+1
    while j < numbers.size:
        
        if numbers[i] + numbers[j] == 2020:
            firstNumber = numbers[i]
            secondNumber = numbers[j]
        j += 1
    i += 1

print(str(firstNumber) + " " + str(secondNumber))

   