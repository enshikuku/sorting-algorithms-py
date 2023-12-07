def bucket_sort(arr):
    buckets = []
    for i in range(len(arr)):
        buckets.append([])

    for num in arr:
        index = int(num * 10)
        buckets[index].append(num)

    for bucket in buckets:
        bucket.sort()

    sorted_array = []
    for bucket in buckets:
        sorted_array.extend(bucket)

    return sorted_array

# Get user input and perform bucket sort
user_array = list(map(float, input("Enter elements of the array separated by spaces: ").split()))
sorted_array = bucket_sort(user_array)

# Display the sorted array
print("Final Sorted array:", sorted_array)
