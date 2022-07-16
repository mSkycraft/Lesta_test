import random
import time


def sorter(massive,flag = False):
    if flag == True:
        flagU = True
        flagD = True
        for i in range(len(massive)-1):
            if(massive[i]<massive[i+1]):
                flagD = False
            elif(massive[i]>massive[i+1]):
                flagU = False
            if(flagU and flagD):
                return massive
    if len(massive) <= 1:
        return massive
    else:
        less = []
        pivotList = []
        more = []
        pivot = massive[0]
        for i in massive:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                more.append(i)
            else:
                pivotList.append(i)
        less = sorter(less)
        more = sorter(more)
        return less + pivotList + more


N = 1000

Test = [None]*N
sum = 0
max = 0.0
min = 100000000
for i in range (N):
    
    mas = list()
    for i in range(100):
        mas.append(round(random.random()*100,2))
    start = time.perf_counter_ns()
    mas = sorter(mas,True)
    stop = time.perf_counter_ns()
    Test[i] = stop - start
    if i == 0:
        max = Test[i]
        min = Test[i]
    if max < Test[i]:
        max = Test[i]
    if min > Test[i]:
        min = Test[i]
    sum = sum + Test[i]
    #print(f'{i}:{Test[i]}')

print(f'Минимальное время работы, мкс = {round(min/1000,5)}')
print(f'Среднее время работы, мкс = {round(sum/N/1000,5)}')
print(f'Максимальное время работы, мкс = {round(max/1000,5)}')
