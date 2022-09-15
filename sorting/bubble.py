def bubble_sort(arr):
    for i in range(len(arr)):
        swap = False
        for j in range(1, len(arr)-i):
            if arr[j-1] > arr[j]:
                swap = True
                arr[j-1], arr[j] = arr[j], arr[j-1]
        if not swap:
            break
    return arr


print(bubble_sort([2, 5, 1, 3, 4, 8, 7, 6, 0, 10, 9, 6, 3]))
