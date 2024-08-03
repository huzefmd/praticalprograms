import random
import timeit
import matplotlib.pyplot as plt


#function to create random input to array
def random_input(array,n):
    for i in range(n):
        ele=random.randrange(1,100)
        array.append(ele)
        
        
def quick_sort(array,low,high):
    if low<high:
        pi=partion(array,low,high)
        quick_sort(array,low,pi-1)
        quick_sort(array,pi+1,high)
        
   
   
#parttion function to divided     
def partion(array, low,high):
    pivot=array[low]
    i=low+1
    j=high
    
    while True:
        while(i<=j and array[i]<=pivot):
            i+=1
            
        while(i<=j and array[j]>=pivot):
            j-=1
            
        if i<=j:
            array[i],array[j]=array[j],array[i]
        else:
            break
    array[low],array[j]=array[j],array[low]
    return j
            
#main function to run the quick sort program  
n_values=[]
cpu=[]

runs=int(input("enter the number of runs:"))
for r in range(0,runs):
    array=[]
    print(f"trail no:->>>>>{r+1}")
    n=int(input("enter the number of ellements"))
    random_input(array,n)
    start=timeit.default_timer()
    quick_sort(array,0,n-1)
    times=timeit.default_timer()-start
    print(f"sorted array is{array}")
    n_values.append(n)
    cpu.append(round(float(times)*100000,2))
    
    
#taking time and values to display in graph
print("N_values  cpu")
for r in range(0,runs):
    print(n_values[r],cpu[r])
    
#ploting the graph    
plt.plot(n_values,cpu,color="red",marker="*")
plt.xlabel("array size")
plt.ylabel("cpu proceesing timee")
plt.title("quick sort time ccomplexity")
plt.show()
    
        
    
        
    
    
    
        
