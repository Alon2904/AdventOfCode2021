import os as os


import numpy as np
os.chdir('c:\\Users\\Alon\\Documents\\לימודים\\AdventOfCode2021\\Day3')
file = open('input.txt', 'r')
lines = file.readlines()

first_argument = []
second_argument = []
arr_ones = []
arr_zeros = []


def Sort(arr1,i ):
  

    for x in arr1:
      
      if x[i] == '1':
          arr_ones.append(x)
      else:
          arr_zeros.append(x)

    if int(len(arr_ones) > int(len(arr_zeros))):
        value = arr_ones.copy()
        return value
    else:
        value = arr_zeros.copy()
        return value

x = Sort(lines,0)
print(x)
arr_ones.clear()
arr_zeros.clear()


for i in range(1,11):
    x = Sort(x,i)
    arr_ones.clear()
    arr_zeros.clear()

print(x)











