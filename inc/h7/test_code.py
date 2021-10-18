# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 09:25:12 2020

@author: Nadine
"""

"""
- tracking elasped time
- timeit module
"""
import time

def func_one(n):
    return [str(num) for num in range (n)]

def func_two(n):
    return list(map(str,range(n)))

n=100000

start_time = time.time()
a=func_one(n)
end_time = time.time()
elapsed_time = end_time-start_time
print(elapsed_time)

start_time = time.time()
b=func_two(n)
end_time = time.time()
elapsed_time = end_time-start_time
print(elapsed_time)


# grab time
# run code
# grab time
# diff is 

#%% alternative

import timeit

stmt_one = '''
func_one(n)
'''
setup_one = '''
n=100
def func_one(n):
    return [str(num) for num in range (n)]
''' 
stmt_two = '''
func_two(n)
'''
setup_two = '''
n=100
def func_two(n):
    return list(map(str,range(n)))
''' 

func_one_time = timeit.timeit(stmt_one,setup_one,number=100000)
func_two_time = timeit.timeit(stmt_two,setup_two,number=100000)

print(func_one_time)
print(func_two_time)

#%% optimizing algorithms and data structures

N=3

total = 0
for x in range(1, N+1):
    total += x
print(total)

print(N*(1+N)/2)


#%% count number of elements in list
my_list = [0,1,2,3,4]

how_many = 0
for element in my_list:
    how_many += 1
print(how_many)

print(len(my_list))

#%% select only even numbers
my_list = [0,1,2,3,4]

output = []
for element in my_list:
    if element % 2 == 0:
        output.append(element)

list(filter(lambda x: x % 2, my_list))      # actually slower than loops; wrong use-case

[item for item in my_list if item % 2]

#%% 1000 operations and 1 function
def square(number):
    return number**2
squares = [square(i) for i in range(1000)]

def compute_squares():
    return [i**2 for i in range(1000)]

#%% check if True/False

if variable == True: #35.8ns
if variable is True: #28.7ns
if variable:         #20.6ns

if variable == False: #35.1ns
if variable is False: #26.9ns
if not variable:      #19.8ns

#%% do not:
q=1
w=2
e=3
r=4

q,w,e,r = 1,2,3,4 # faster but your future self will hate you

#%% Oefenopgave even getallen sneller maken:
# vind alle even getallen uit een random lijst op twee manieren
import numpy as np
import time

# gebruik een random seed om telkens dezelfde random getallen te gebruiken
#np.random.seed(2020)

n=1000000   # aantal random getallen
random_nrs = np.random.randint(100,size=n) # n random int tussen 0 en 99
#random_nrs = list(random_nrs)       

start_tijd1 = time.time() # start de tijd voor methode 1
even_nrs1 = [] # maak lege lijst voor even getallen                 
for element in random_nrs: # loop door de hele lijst
    if element % 2 == 0: # als een getal even is (% 2 = 0)
        even_nrs1.append(element) # voeg het getal toe aan de lijst even_nrs1
eind_tijd1 = time.time() # stop de tijd voor methode 1
verstreken_tijd1 = eind_tijd1-start_tijd1 # bereken de verstreken tijd
print('methode 1 duurt: %.4f sec' % verstreken_tijd1)


start_tijd1 = time.time() # start de tijd voor methode 2
#random_nrs = np.array(random_nrs) # maak een np.array van de lijst
masker_even_getallen = random_nrs % 2 == 0 # maak een masker voor even getallen
even_nrs2 = random_nrs[masker_even_getallen] # gebruik het masker voor de array random getallen
# even_nrs2 = list(even_nrs2) # zet de array om in een lijst
eind_tijd1 = time.time() # stop de tijd voor methode 2
verstreken_tijd1 = eind_tijd1-start_tijd1 # bereken de verstreken tijd
print('methode 1 duurt: %.4f sec' % verstreken_tijd1)


#%%
a=input('?')