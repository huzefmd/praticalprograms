MAX=100

c=[[0]* MAX for _ in range(MAX)]
visited=[0]*MAX
queue=[0]*MAX

def bfs(v):
    front=0
    rear=-1
    
    visited[v]=1
    queue[rear+1]=v
    rear+=1
    
    while front<=rear:
        v=queue[front]
        front+=1
        print(f"{v} ",end="")
        for i in range(i,n+1):
            if c[v][i]==1 and visited==0:
                queue[rear+1]=i
                rear+=1
                visited[i]=1
                
                
if __name__=="__main__":
    print("enter the number of vertices in the graph:")
    n=int(input())
    
    print('enter the cost matrix of the graph->')
    for i in range(1,n+1):
        c[i]=[0] +list(map(int,input().split()))
        
        
        for i in range(1,n+1):
            visited[i]=0
        print("enter the startting vertix:->")
        v=int(input())
        print("bfs traversal of the graph is ->",end="")
        bfs(v)
                     