def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                print(arr)


arr = [65, 34, 25, 12, 22, 77, 90]
bubble_sort(arr)
print("排序后的数组:", arr)
