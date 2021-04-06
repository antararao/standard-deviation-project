import csv 
import math 

with open('data.csv', newline='') as f:

    reader = csv.reader(f)
    data = list(reader)

file = data[0]

def mean(file):
    n = len(file)
    total = 0
    for x in file: 
        total += int(x)

    mean = total / n

    return(mean) 

square = []
for number in file:
    a = int(number) - mean(file)
    a = a**2
    square.append(a)

sum = 0
for i in square: 
    sum += i

result = sum/(len(file)- 1)

dev = math.sqrt(result)

print(dev)
