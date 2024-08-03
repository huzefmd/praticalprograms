def find_subsets(arr, target, index, current_subset, all_subsets):
    if target == 0:
        all_subsets.append(current_subset.copy())
        return
    
    if target < 0 or index >= len(arr):
        return
    
    current_subset.append(arr[index])
    find_subsets(arr, target - arr[index], index + 1, current_subset, all_subsets)
    current_subset.pop()
    find_subsets(arr, target, index + 1, current_subset, all_subsets)

def main():
    arr = list(map(int, input("Enter the set elements separated by space: ").split()))
    target = int(input("Enter the target sum: "))
    
    all_subsets = []
    find_subsets(arr, target, 0, [], all_subsets)
    
    if not all_subsets:
        print("No subset found with the given target sum.")
    else:
        print("Subsets with the given target sum are:")
        for subset in all_subsets:
            print(subset)

if __name__ == "__main__":
    main()
