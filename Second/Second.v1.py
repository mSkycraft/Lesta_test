
class Queue:
    def __init__(self):
        self.queue = list()
    
    def add(self,value):
        if value not in self.queue:
            self.queue.insert(0,value)
            return True
        return False
    
    def delete(self):
        if(len(self.queue)>0):
            return self.queue.pop()
        return 'Очередь пуста'
    
    def size(self):
        return len(self.queue)
    
    def getData(self):
        if(len(self.queue)>0):
            ret = self.queue[len(self.queue)-1]
            self.delete()
            return ret
        return 'Очередь пуста'



isQueue = Queue()

isQueue.add("Данные1")
isQueue.add("Данные2")
isQueue.add("Данные3")
isQueue.add("Данные4")

print(isQueue.queue)
print(isQueue.getData())
print(isQueue.getData())
print(isQueue.queue)
