#  Bubble Sort
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left, right = arr[:mid], arr[mid:]
        merge_sort(left)
        merge_sort(right)
        arr[:] = sorted(left + right)

# Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less_than_pivot = [x for x in arr[1:] if x <= pivot]
        greater_than_pivot = [x for x in arr[1:] if x > pivot]
        return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)

# Heap Sort
def heapify(arr, n, i):
    largest = i
    left_child = 2 * i + 1
    right_child = 2 * i + 2

    if left_child < n and arr[i] < arr[left_child]:
        largest = left_child

    if right_child < n and arr[largest] < arr[right_child]:
        largest = right_child

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

# heap_sort
def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

# counting_sort
def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]

# Radix Sort
def radix_sort(arr):
    max_num = max(arr)

    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

# Bucket Sort
def bucket_sort(arr):
    max_val = max(arr)
    min_val = min(arr)
    num_buckets = len(arr)
    buckets = [[] for _ in range(num_buckets)]

    for num in arr:
        index = int((num - min_val) / (max_val - min_val) * (num_buckets - 1))
        buckets[index].append(num)

    for bucket in buckets:
        bucket.sort()

    sorted_array = []
    for bucket in buckets:
        sorted_array.extend(bucket)

    return sorted_array

# Shell Sort
def shell_sort(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2

if __name__ == "__main__":
    user_array = list(map(int, input("Enter elements of the array separated by spaces: ").split()))

    bubble_sorted = user_array.copy()
    bubble_sort(bubble_sorted)
    print("Bubble Sort:", bubble_sorted)

    insertion_sorted = user_array.copy()
    insertion_sort(insertion_sorted)
    print("Insertion Sort:", insertion_sorted)

    merge_sorted = user_array.copy()
    merge_sort(merge_sorted)
    print("Merge Sort:", merge_sorted)

    quick_sorted = user_array.copy()
    quick_sorted = quick_sort(quick_sorted)
    print("Quick Sort:", quick_sorted)

    heap_sorted = user_array.copy()
    heap_sort(heap_sorted)
    print("Heap Sort:", heap_sorted)

    counting_sorted = user_array.copy()
    radix_sort(counting_sorted)
    print("Radix Sort:", counting_sorted)

    bucket_sorted = user_array.copy()
    bucket_sorted = bucket_sort(bucket_sorted)
    print("Bucket Sort:", bucket_sorted)

    shell_sorted = user_array.copy()
    shell_sort(shell_sorted)
    print("Shell Sort:", shell_sorted)
