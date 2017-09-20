"""
我下面寫的def , 

定義func , 把第一個字寫成大寫,

用dir() 去看, 會把大寫的func, 歸類成class
"""
class Queue(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []
    
    def enqueue(self,item):
        self.items.insert(0,item) 
    
    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

