
file = open('input.txt', 'r')

lines = file.readlines()

numbers1 = []
numbers2 = []
sum=0

for line in lines:
    numbers1.append(int(line))

for x in range(len(numbers1)-2):
    int1 = numbers1[x]
    int2 = numbers1[x+1]
    int3 = numbers1[x+2]

    numbers2.append(int1 + int2 + int3)


for x in range(len(numbers2)-1):
    if (numbers2[x] < numbers2[x+1]):
        sum = sum+1

print(sum)
