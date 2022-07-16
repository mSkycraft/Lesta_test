class StructQueue:
    def __init__(self):
        self.data = None
        self.next = None
        self.back = None
    
    def AddToEnd(self,value):
        if self.data == None:
            self.data = value
            return
        EndData = self
        while(EndData.next!=None):
            EndData = EndData.next
        EndData.next = StructQueue()
        EndData.next.back = EndData
        EndData = EndData.next
        EndData.data = value
    
    def BackToStart(self):
        start = self
        while(start.back):
            start = start.back
        return start

    def ExtractFirst(self):
        start = self.BackToStart()
        next = start.next
        next.back = None
        return start.data,next

    def PrintQueue(self):
        id = 1
        start = self.BackToStart()
        while(start!=None):
            print(f'ID: {id} Data: {start.data}')
            start = start.next
            id += 1




isStQueue = StructQueue()

isStQueue.AddToEnd("Data1")
isStQueue.AddToEnd("Data2")
isStQueue.AddToEnd("Data3")
isStQueue.AddToEnd("Data4")

isStQueue = isStQueue.BackToStart()

isStQueue.PrintQueue()

data, isStQueue = isStQueue.ExtractFirst()

print(f'Извлеченные данные: {data}')
isStQueue.PrintQueue()
