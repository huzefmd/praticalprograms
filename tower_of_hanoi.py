def toh(n,s,d,t):
    if n==1:
        print(f"move disk {n} from {s} to {d}")
        return 1
    count=0
    count += toh(n-1,s,t,d)
    print(f"move disk {n} from {s} to {d}")
    count+=1
    count += toh(n-1,t,d,s)
    return count

n=2
result=toh(n,"A","B","C")
print(f"the total number of moves are {result}")