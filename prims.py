import heapq

def prims(graph,start):
    visited = set()
    min_heap = [(0,start,None)]
    edges = []
    total_cost = 0
    
    while min_heap:
        cost , node , prev = heapq.heappop((min_heap))
        
        if node in visited:
            continue
        visited.add(node)
        
        if prev is not None:
            edges.append((prev,node,cost))
            total_cost +=cost
        
        for i , j in graph.get(node,[]):
            if i not in visited:
                heapq.heappush(min_heap,(j,i,node))
    
    print("minimum spannig tree edges")
    for i , j , w in edges:
        print(f"{i}-{j} = {w}")
    
    print(f"total mst ; {total_cost}")    



graph = {}

for _ in range(int(input("enter the no of edges : "))):
    v1,v2,cost = input("enter the v1 v2 cost : ").split()
    cost = int(cost)
    graph.setdefault(v1,[]).append((v2,cost))
    graph.setdefault(v2,[]).append((v1,cost))
    
start = input("enter start node ; ")    
prims(graph,start)    
    
