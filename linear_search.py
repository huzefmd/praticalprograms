import matplotlib.pyplot as plt
import time

def linear_search(arr,key,n):
    for i in range(n):
        if arr[i]==key:
            return i
    return -1

def run_linear():
    results=[]
    runs=int(input("enter the number of runs:"))
    for j in range(runs):
        n=int(input("enter the number of elements:"))
        arr=list(map(int,input("enter the array elements:").split()))
        key=int(input("enter the element to be searches:"))
        
        repeat=10000
        start_time=time.time()
        for _ in range(repeat):
            result=linear_search(arr,key,n)
        end_time=time.time()
    
        
        time_taken=(end_time-start_time)*1000/repeat
        
        if result != -1:
            print(f'key-->{key} found at index--->{result}')
        else:
            print(f'key---->{key}: not found')
            
        results.append((n,time_taken))   
        
    return results

def plot_result(results):
    n_values=[result[0]for result in results]
    times=[result[1]for result in results]
    plt.figure()
    plt.plot(n_values,times,'o-')
    plt.xlabel('number of elllemts(n)')
    plt.ylabel("time taken(milliseconds)")
    plt.title("linear search time complexity")
    plt.grid(True)
    plt.show()
    
    
a=run_linear()
plot_result(a)

    