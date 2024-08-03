import matplotlib.pyplot as plt
import random
import timeit


# function to create random array ellements


def random_array(array, n):
    for i in range(n):
        ele = random.randrange(1, 100)
        array.append(ele)


# selection sort function


def selection_sort(array, size):
    for a in range(size):
        min_idx = a
        for b in range(a + 1, size):
            if array[b] < array[a]:
                min_idx = b
        array[a], array[min_idx] = array[min_idx], array[a]

# def run_selection():
n_values = []
cpu = []
runs = int(input("enter the number of runs"))
for r in range(0, runs):
    array = []
    print(f"------->trail no {r+1}<------")
    n = int(input("enter the number of elements"))
    random_array(array, n)
    start = timeit.default_timer()
    result = selection_sort(array, n)
    times=timeit.default_timer()-start
    print(f"sorted Array is {result}")
    n_values.append(n)
    cpu.append(round(float(times)*1000000,2))
    
    
print(n_values,cpu)
for r in range(0,runs):
    print(n_values[r],cpu[r])
    
    
plt.plot(n_values,cpu,color="red",marker='*',markersize=10)
plt.xlabel("array size,n_values")
plt.ylabel("cpu processing time")
plt.title("selection sort time complexity")
plt.show()
