import os as os

os.chdir('c:\\Users\\Alon\\Documents\\לימודים\\AdventOfCode2021\\Day2')

file = open('input.txt', 'r')
lines = file.readlines()


    

arr_inst = []
arr_size = []
for line in lines:
    a, b = line.split()

    arr_inst.append(a)
    arr_size.append(b)

depth = 0
horizontal = 0
aim = 0

for i in range(0,len(arr_inst)):

        if arr_inst[i] == "forward":
            horizontal = horizontal + int(arr_size[i])
            depth = aim * int(arr_size[i])

        if arr_inst[i] == "down":
            aim = aim + int(arr_size[i])

        if arr_inst[i] == "up":
            aim = aim - int(arr_size[i])


      
print("depth: " ,depth, "horizontal", horizontal)
print("depth * horizontal= ", depth * horizontal)
