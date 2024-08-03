#essentially multiplying a by itself n times. 
def brute_force(a,n):
    result=1
    for i in range(n):
        result*=a
    return result

def divide_and_conquer(a,n):
    if n==0:
        return 1
    elif n%2==0:
        return divide_and_conquer(a*a,n//2)
    else:
        return a* divide_and_conquer(a*a,n//2)
    
    
    
a,n=map(int,input('enter the value of a and n :').split())

bruteforce_result=brute_force(a,n)
dandc_result=divide_and_conquer(a,n)

print(f"result using brute force---------->{bruteforce_result}")
print(f"result using divide and conquer---------->{dandc_result}")