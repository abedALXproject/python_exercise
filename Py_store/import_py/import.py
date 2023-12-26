#!/usr/bin/env python3
# _*_ conding: utf-8 _*_

#import random as me
"""
#from random import * #randint, uniform, random
#random.seed(1)
randInt = randint(0,10)
print(randInt)

randFloat = random()
print(randFloat)

randUniform = uniform(1,100)
print(randUniform)

randInt = randint(0,10)
print(randInt)

myList = [1,2,3,5,45,8,7,11]
pickElement = me.choice(myList)
print(pickElement)
print(myList)
me.shuffle(myList)
print(myList)
"""

#time library

#import time
"""
currentTime = time.clock()
print("Hello")
pastTime = time.clock()
print(pastTime - currentTime)

print("1")
time.sleep(4)
print("5")

for me in range(1,11):
    print(me)
    time.sleep(2)
"""

#math library
"""
import math

num = 3.14
sqrtNum = math.sqrt(num)
print(sqrtNum**2) #sqrtNum ^2

expNum = math.exp(num)
print(expNum)

factNum = math.factorial(math.floor(num)) #5! = 5*4*3*2*1
print(factNum)

sinNum = math.sin(num)
print(sinNum)

floorNum = math.floor(num)
print(floorNum)

ceilingNum = math.ceil(num)
print(ceilingNum)
"""

#Guessing game
"""
from random import randint
value = randint(0,100)

while(True):
    guessing = int(input("Enter guessing:"))
    if guessing == value:
        break
    elif guessing < value:
        print("low guessing")
    else:
        print("Too high guessing")
print("Correct guessing with:", guessing)

"""

from random import random
from time import perf_counter #clock

randValue = random()
#print(randValue)

higher = 1.0
lower = 0.0
#guess = 0.5 - > Too Low -  lower = 0.5
#guess = 0.9 -> Too High -> Higher = 0.9

#guess = 0.5

startTime = perf_counter() # clock()
while(True):
    guess = (higher + lower)/2
    if guess == randValue:
        break
    elif guess < randValue:
        lower = guess
    else:
        higher = guess
    #guess = (higher + lower)/2
endTime = perf_counter() #clock()
its_take = endTime- startTime
print(guess)
print(f"it take me: {its_take} second")
