def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left, right = arr[:mid], arr[mid:]
        merge_sort(left)
        merge_sort(right)
        arr[:] = sorted(left + right)

# Get user input and perform merge sort
user_array = list(map(int, input("Enter elements of the array separated by spaces: ").split()))
merge_sort(user_array)

# Display the sorted array
print("Final Sorted array:", user_array)
