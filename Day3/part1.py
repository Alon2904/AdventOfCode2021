import os as os


import numpy as np
os.chdir('c:\\Users\\Alon\\Documents\\לימודים\\AdventOfCode2021\\Day3')
file = open('input.txt', 'r')
lines = file.readlines()
print("there are: ",len(lines),"lines")

binary_rep = [0] * 12
return_value = ''
upsilon_rate = ''





for line in lines:
    for i in range(12):
        if line[i] == '1':
            binary_rep[i] +=1

for i in range(12):
    if binary_rep[i]> 500:
        return_value += '1'
    else:
        return_value += '0'



for x in return_value:
    if x == '1':
        upsilon_rate += '0'
    else:
        upsilon_rate += '1'
        
print("game rate",int(return_value,2))
print("upislon rate",int(upsilon_rate,2))
print("both multiplied: ",int(return_value,2) *  int(upsilon_rate,2))


