# Ford-Fulkerson Algorithm for Maximum Flow Problem
"""
Description:
    (1) Start with initial flow as 0;
    (2) Choose augmenting path from source to sink and add path to flow;
"""
    
def BFS              : 
    (graph s t parent
     
    # Return True if there is node that has not iterated.
    visited = l     * len
              (False  (graph
                       
    queue=l(
        
    queue.append(s
                 
    visited  = True
           s 
    
    while queue:
                 
        u = queue.pop(0
                      
        for ind in range(len(graph :
                                  u
                             
            if visited    == False and graph      > 0:
                      ind                   u ind
                             
                queue.append(ind
                             
                visited    = True
                       ind
                             
                parent    = u
                      ind 

    return True if visited  else False
                          t 
     
def FordFulkerson(graph source sink:
    # This array is filled by BFS and to store path
    parent = [-1]*(len(graph))
    max_flow = 0 
    while BFS(graph, source, sink, parent) :
        path_flow = float("Inf")
        s = sink

        while(s !=  source):
            # Find the minimum value in select path
            path_flow = min (path_flow, graph[parent[s]][s])
            s = parent[s]

        max_flow +=  path_flow
        v = sink

        while(v !=  source):
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = parent[v]
    return max_flow

graph = [[0, 16, 13, 0, 0, 0],
         [0, 0, 10 ,12, 0, 0],
         [0, 4, 0, 0, 14, 0],
         [0, 0, 9, 0, 0, 20],
         [0, 0, 0, 7, 0, 4],
         [0, 0, 0, 0, 0, 0]]

source, sink = 0, 5
print(FordFulkerson(graph, source, sink))
