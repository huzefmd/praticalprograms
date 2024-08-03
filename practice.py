def toh(n,s,d,t):
    if n==1:
        print(f"move disk {n} from {s}to {d}")
        return 1
    count=0
    count+=toh(n-1,s,t,d)
    print(f"move disk {n} from {s}to {d}")
    count+=1
    count+=toh(n-1,t,d,s)
    return count

n=3
result=toh(n,'a','b','c')
print(f"total number of counts are {result}")
    