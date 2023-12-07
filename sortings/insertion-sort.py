def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Get user input and perform insertion sort
user_array = list(map(int, input("Enter elements of the array separated by spaces: ").split()))
insertion_sort(user_array)

# Display the sorted array
print("Final Sorted array:", user_array)
