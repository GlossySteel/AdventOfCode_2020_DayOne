# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 18:43:37 2021

@author: Joseph Kharzo
"""

import pandas as pd

df = pd.read_csv("Numbers.csv")

numbers = df['Numbers']

firstNumber = 0
secondNumber= 0
thirdNumber = 0

i = 0
j = 1
k = 2

while i < numbers.size:
    j = i+1
    while j < numbers.size:
        k=i+2
        while k < numbers.size:
            if(numbers[i] + numbers[j] + numbers[k] == 2020):
                firstNumber = numbers[i]
                secondNumber = numbers[j]
                thirdNumber = numbers[k]
            k +=1
        
        j += 1
    i += 1

print(str(firstNumber) + " " + str(secondNumber) + " " + str(thirdNumber))