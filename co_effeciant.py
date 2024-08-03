# def fact(n):
#     fact=1
#     for i in range(2,n+1):
#         fact*=i
#     return fact
    
def fact(n):
    if n<=1:
        return 1
    else:
        return (n*fact(n-1))
    
    
def b_c_bf(n,k):
    return fact(n)//(fact(k)*fact(n-k))


def b_c_dp(n,k):
    c=[[0 for j in range(k+1)]for i in range(n+1)]
    for i in range(n+1):
        for j in range(min(i,k)+1):
            if j==0 or j==i:
                c[i][j]=1
            else:
                c[i][j]=c[i-1][j-1]+c[i-1][j]
    return c[n][k]

n=int(input("enter the value of n"))
k=int(input("enter the value of k"))

bf_result=b_c_bf(n,k)
dp_result=b_c_dp(n,k)

print(f" binomeal coeffeicent result of brute force is{bf_result}")
print(f" binomeal coeffeicent result of dynamic programing is{dp_result}")