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
DFS停的點在那裡?
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

    vertex = stack.pop() 
    for i in graph2[vertex] - visited:
        if i is end: 
            path.append(i)
            yield path
        else:
            stack.append(i)   
            visited.add(i)
            path.append(i)

print "DFS : " + str(  DFS(graph2, 'A', 'F')  )
