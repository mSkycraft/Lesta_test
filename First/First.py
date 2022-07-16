#Вариант 1
def isEven(value):return value%2==0


#Вариант 2
def Parity(value):
    if(value>0):
        return Parity(value-2)
    if(value==0):
        return True
    else:
        return False


for i in range(1,10):
    print(f'{i} - {Parity(i)}')


