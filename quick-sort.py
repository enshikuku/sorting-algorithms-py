def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less_than_pivot = [x for x in arr[1:] if x <= pivot]
        greater_than_pivot = [x for x in arr[1:] if x > pivot]
        return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)

# Get user input and perform quick sort
user_array = list(map(int, input("Enter elements of the array separated by spaces: ").split()))
user_array = quick_sort(user_array)

# Display the sorted array
print("Final Sorted array:", user_array)
