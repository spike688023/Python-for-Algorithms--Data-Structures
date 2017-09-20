"""
目前的想法, 是用list中的,

reverse的func, 

二個list, 一個用來放push的,

一個用來放remove,

當執行完, push or remove 的指令後, 

就做個reverse 動作 copy到另一個list中.

"""

class Queue2Stacks(object):
    
    def __init__(self):
        
        # Two Stacks
        self.stack1 = []
        self.stack2 = []
     
    def enqueue(self,element):
        self.stack1.append(element)
        # list是call by reference, 所以不能這樣用.
        #self.stack2 = self.stack1

        # 為什麼, 它會說沒有 copy func
        #stack2 = stack1.copy()
        # 案 python3.2 就真的沒有 copy func
        #self.stack2 = [ i for i in self.stack1 ]
        self.stack2 = self.stack1.copy()
        self.stack2.reverse()
        
    
    def dequeue(self):
        value = self.stack2.pop()
        #self.stack1 = self.stack2
        #self.stack1 = [ i for i in self.stack2 ]
        self.stack1 = self.stack2.copy()
        self.stack1.reverse()
        return value
        
    def isEmpty(self):
        return self.stack1 == [] and self.stack2 == []

    def size(self):
        return len(self.stack1)

q = Queue2Stacks()

for i in range(5):
    q.enqueue(i)
    
for i in range(5):
    print( q.dequeue() )
