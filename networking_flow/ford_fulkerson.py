# Ford-Fulkerson Algorithm for Maximum Flow Problem
"""
Description:
    (1) Start with initial flow as 0;
    (2) Choose augmenting path from source to sink and add path to flow;
"""
    
def BFS
    ( graph, s, t, parent:
    # Return True if there is node that has not iterated.
    visited = [False] * len   # Ambiguity, if we remove one bracket from False, then it's ambiguous whether len is multiple by False inside bracket or outside, but if as a rule we always say a bracket is attached to something (that something can be space, then we can always go to the second line.
                        ( graph
    # rewrite of above: but it is still ugly because of [False] and len are the same level citizens (in the same operator space), but now they are shown on different levels.
    visited =         * len
              [False    ( graph
    queue =   #this is ugly too, like above. Maybe we should prevent using [] and {} for types, instead do l( for list and d( for dict
             [
                
    queue.append
    ( s
    visited = True
    [ s
    
    while queue:
        u = queue.pop
        ( 0
        for ind in range :
        ( len
          ( graph 
            [ u
            #Amibguiuty????? V
            if visited == False and graph  > 0:
               [ ind                [ u
                                      [[ ind
                queue.append
                ( ind
                visited = True
                [ ind
                parent = u
                [ ind

    return True if visited   else False
                   [ t         
     
def FordFulkerson      :
    ( graph, source, sink
    # This array is filled by BFS and to store path
    parent = [-1] * len
                    () graph
    max_flow = 0 
    while BFS                           :
          () graph, source, sink, parent
        path_flow = float
                    () "Inf"
        s = sink

        while s !=  source:
            # Find the minimum value in select path
            #Ambiguity: How to mix various bracket types in the tree?
            path_flow = min 
                        () path_flow, graph
                                      [ parent
                                      [ s
                                      [ s
            # this one up there is a chain, so no indentation
            s = parent
                [ s

        max_flow +=  path_flow
        v = sink

        while v !=  source:
            u = parent
                [ v
            #This below makes it hard to visually see where a new line starts. So we need indendations, that is look at the cases below it (space indentations is bad since people have to figure out if it is a vertical block, but we can put more brackets:
            graph -= path_flow
            [[ u
            [[ v
            graph += path_flow
            [[ v
            [[ u
             
            #Above are Rewrite of these below:
            graph -= path_flow
            [u
            [v
            graph += path_flow
            [v
            [u
             
             
             
            v = parent
                [v
    return max_flow

graph = [
        [[0, 16, 13, 0, 0, 0,
        [[0, 0, 10 ,12, 0, 0,
        [[0, 4, 0, 0, 14, 0,
        [[0, 0, 9, 0, 0, 20,
        [[0, 0, 0, 7, 0, 4,
        [[0, 0, 0, 0, 0, 0
#Rewrite of above with using l( instead of [ for list:
graph = l
        (l
         (0, 16, 13, 0, 0, 0,
        (l
         (0, 0, 10 ,12, 0, 0,
        (l
         (0, 4, 0, 0, 14, 0,
        (l
         (0, 0, 9, 0, 0, 20,
        (l
         (0, 0, 0, 7, 0, 4,
        (l
         (0, 0, 0, 0, 0, 0
#Rewrite of above, allowing for chains to be in the same line:
graph = l
        (l(0, 16, 13, 0, 0, 0,
        (l(0, 0, 10 ,12, 0, 0,
        (l(0, 4, 0, 0, 14, 0,
        (l(0, 0, 9, 0, 0, 20,
        (l(0, 0, 0, 7, 0, 4,
        (l(0, 0, 0, 0, 0, 0
 #Is the above correct, according to my syntax rules? Yes. Because if we move the lines together, i.e.
      graph = l
        (l(0, 16, 13, 0, 0, 0,(l(0, 0, 10 ,12, 0, 0,
                                 # then it's not clear whether the third l is part of the second l or if they are parallel.
                                 
 # None of the aboves are correct. How do we separate arguments in my syntax? Are we using comma? or enter? 
 # So far I was only working with operators and it was obvious. What about now with commas?
graph = l
        (l(0, 16, 13, 0, 0, 0,
        (l(0, 0, 10 ,12, 0, 0,
        (l(0, 4, 0, 0, 14, 0,
        (l(0, 0, 9, 0, 0, 20,
        (l(0, 0, 0, 7, 0, 4,
        (l(0, 0, 0, 0, 0, 0
# In other words, without chains reduction, the correct format is:
graph = l
        (l                     ,  l                     ,  l                   , etc...
         (0, 16, 13, 0, 0, 0,     (0, 0, 10 ,12, 0, 0,     (0, 4, 0, 0, 14, 0,
# But chain reduction makes it ambiguious. Chain introduces ambiguity when we have multiple arguments 
# But that means we can only use chains if from the root of the point we are interested to the leaf is single arguments, that is
# f(a (x) , b(y(c(z))))
# is
# f
# (a  ,  b
#  (x     y(c(z
# but not below. Actually why not, this is perfectly fine. The problem with lists above was that l was not single argument. 
# Here everything is single argument
# f
# (a(x , b(y(c(z
# Does this cause hypothesis building of whether what I am reading at this current moment is a chain or is not a chain?
source, sink = 0, 5
print
((FordFulkerson
  ((graph, source, sink
