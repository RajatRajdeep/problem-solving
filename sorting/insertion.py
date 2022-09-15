def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i-1
        key = arr[i]
        while j >= 0 and arr[j] > key:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            j -= 1
    return arr


print(insertion_sort([2, 5, 1, 3, 4, 8, 7, 6, 0, 10, 9, 6, 3]))
