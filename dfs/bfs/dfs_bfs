
def edges(graph,v1,v2):
    graph.setdefault(v1,[]).append(v2)
    graph.setdefault(v2,[]).append(v1)
    
    
def dfs(graph , vertex , visited):
    visited.add(vertex)
    print(vertex , end=" ")
    
    for i in graph.get(vertex , []):
        if i not in visited:
            dfs(graph , i , visited)
    
def bfs(graph , vertex):
    
    visited = {vertex}
    queue = [vertex]
    
    while queue:
        vertex = queue.pop(0)
        print(vertex , end=" ")
        
        for i in graph.get(vertex,[]):
            if i not in visited:
                visited.add(i)
                queue.append(i)
    
    
def main():
    graph = {}
    for _ in range(int(input("enter no. of edges : "))):
        v1,v2 = map(int,input("enter vertex sepreted by space : ").split())
        edges(graph,v1,v2)
        
    vertex = int(input("start vertex"))
    print("dfs")
    dfs(graph,vertex,set())
    print("/n dfs")
    bfs(graph,vertex)
    

if __name__ == "__main__":
    main()
