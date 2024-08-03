import matplotlib.pyplot as plt
import time

def binary_search(arr,low,high,key):
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==key:
            return mid
        elif arr[mid]<key:
            low=mid+1
        else:
            high=mid-1
    return -1

def linear_search(arr,n,key):
    for i in range(n):
        if arr[i]==key:
            return i
    return -1

def  run_binary_search():
    results=[]
    runs=int(input("enter the number of runs->>>>"))
    
    for j in range(runs):
        
        
        n=int(input("enter the number of elements"))
        arr=list(map(int,input("enter the array ellements").split()))
        key=int(input('enter the key element to be searchedd'))
        
        
        repeat=10000
        start_time=time.time()
        for k in range(repeat):
            result=linear_search(arr,n,key)
        end_time=time.time()
        time_taken=(end_time-start_time)*1000/repeat
        
        
        
        if result!=-1:
            print(f"the key->{key} element found at index {result}")
        else:
            print(f'the key {key} eleemnet not found in the array -> {arr}')
            
        
            
        results.append((n,time_taken))
    return results


def plot_binary_search(results):
    n_values=[result[0]for result in results]
    times=[result[1]for result in results]
    
    plt.figure()
    plt.plot(n_values,times,'o-')
    plt.xlabel('number of ellements')
    plt.ylabel('time taken in millis seconds')
    plt.title("binary search time complexity")
    plt.grid(True)
    plt.show()
    
    
a=run_binary_search()
plot_binary_search(a)



        