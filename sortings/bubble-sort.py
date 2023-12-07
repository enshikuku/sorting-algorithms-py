def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def main():
    user_list = list(map(int, input("Enter numbers separated by spaces: ").split()))
    bubble_sort(user_list)
    print("Sorted array:", user_list)

if __name__ == "__main__":
    main()
