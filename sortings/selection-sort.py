def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Get user input and perform selection sort
user_array = list(map(int, input("Enter elements of the array separated by spaces: ").split()))
selection_sort(user_array)

# Display the sorted array
print("Final Sorted array:", user_array)
