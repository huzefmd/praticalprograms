import sys

def minKey(key,mstSet,n):
    min_value=sys.maxsize
    for v in range(n):
        if mstSet[v]==False and key[v]<min_value:
            min_value=key[v]
            min_index=v
    return min_index

def print_mst(parent,c,n):
    totalweight=0
    print("Edge  Weight")
    for i in range(1,n):
        print(str(parent[i]+1)+ " - " + str(i+1) + "     " + str(c[i][parent[i]]) )
        totalweight+=c[i][parent[i]]
    return totalweight

def primMst(c,n):
    parent=[None]*n
    key=[sys.maxsize]*n
    key[0]=0
    mstSet=[False]*n
    parent[0]=-1
    for count in range(n):
        u=minKey(key,mstSet,n)
        mstSet[u]=True
        for v in range(n):
            if c[u][v]>0 and mstSet[v] ==False and c[u][v]< key[v]:
                parent[v]=u
                key[v]=c[u][v]
                
                
    totalWeight=print_mst(parent,c,n)
    print("Total cost of the minimum spaning tree is "+ str(totalWeight))
n=int(input(" enter the number of vertices:::"))
c=[]
print (" enter the cost adjacaceny matrix:")
for i in range(n):
    c.append(list(map(int,input().split())))
primMst(c,n)
        
        
        