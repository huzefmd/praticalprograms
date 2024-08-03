inf=99999
def print_floyd(v,d):
    print("the folowing matrix showa the shortest distnace betweeen eyery pair of vertices")
    for i in range(v):
        for j in range(v):
            if d[i][j]==inf:
                print(f"{'inf':7}",end="")
            else:
                print(f"{d[i][j]:7}",end="")
        print()
    
    
def floyd_warshal(v,cost_matrix):
    d=[[0]*v for _ in range(v)]
    for i in range(v):
        for j in range(v):
            d[i][j]=cost_matrix[i][j]
        
    for k in range(v):
        for i in range(v):
            for j in range(v):
                if d[i][j]>d[i][k]+d[k][j]:
                    d[i][j]=d[i][k]+d[k][j]
                    
    print_floyd(v,d)
    
    
v = int(input("Enter the number of vertices: "))

# Initialize the cost matrix
cost_matrix = [[0] * v for _ in range(v)]

print("Enter the cost matrix row by row, separated by spaces:")
print("Enter 0 for cost[i][i] and 99999 for no direct path")

# Input the cost matrix
for i in range(v):
    cost_matrix[i] = list(map(int, input().split()))

# Run the Floyd-Warshall algorithm
floyd_warshal(v, cost_matrix)
    