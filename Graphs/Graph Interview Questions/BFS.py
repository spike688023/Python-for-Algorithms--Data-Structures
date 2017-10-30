# -*- coding: utf-8 -*-
graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

print graph 
"""
實作DFS, BFS:

最大的差別在,  使用的儲存結構,

BFS因為要從相鄰的往外延申, 所以要用queue,

DFS則是用stack, 

喔, 它媽的想到了, 

DFS, BFS只是對圖的search的方式不同而己, 

function的呼叫,也是可以給個目地.
"""
def BFS(graph, start):
    result, queue = [start], [start]
    visited = set(start)

    # 這裡 for loop要用set 
    while queue:
        vertex = queue.pop(0) 
        for i in graph[vertex] - visited:
            queue.append(i)   
            visited.add(i)
            result.append(i)
             
    return result

print "BFS : " + str( BFS(graph, 'A') )


"""
DFS , 會用到 yield
DFS停的點在那裡?  找到 goal的時侯，

即便我的寫法是錯的，yield也要有回傳一些路徑才對丫。

喔，它媽的，我知道，

首先，我沒有用while去判斷stack內是否有東西，

整個func內，只有一個for loop，所以這個loop，

沒有跑到，我們要的end， 所以沒有東西return，

即便我code裡面有寫要return的行。

所以，我改成要到b ，就 會有東西了
"""
graph2 = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

def DFS(graph2, start, end):
    path, stack = [start], [start]
    visited = set(start)
    print path
    vertex = stack.pop() 
    for i in graph2[vertex] - visited:
        if i == end: 
            yield path + [i]
        else:
            stack.append(i)   
            visited.add(i)
            path.append(i)

print list(  DFS(graph2, 'A', 'B')  )
