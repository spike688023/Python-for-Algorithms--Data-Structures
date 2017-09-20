"""
真的要去下載 python 的source code來看, 

它list怎麼實作的, 不然, 我實作其它東西, 

大多都是用list 的func.
"""
class Deque(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []
    
    def addfront(self,item):
        self.items.append(item) 
    
    def addrear(self,item):
        self.items.insert(0,item) 

    def removefront(self):
        return self.items.pop()

    def removerear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

