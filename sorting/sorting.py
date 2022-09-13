import random

def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[min_index], arr[i] = arr[i], arr[min_index]
    return arr


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


def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i-1
        key = arr[i]
        while j >= 0 and arr[j] > key:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            j -= 1
    return arr


def merge(arr, low, mid, high):
    i, j, k = low, mid + 1, low
    copy_arr = arr[:]
    while i <= mid and j <= high:
        if copy_arr[i] > copy_arr[j]:
            arr[k] = copy_arr[j]
            j += 1
        else:
            arr[k] = copy_arr[i]
            i += 1
        k += 1

    while i <= mid:
        arr[k] = copy_arr[i]
        i += 1
        k += 1

    while j <= high:
        arr[k] = copy_arr[j]
        j += 1
        k += 1

    return arr


def merge_sort(arr, low=None, high=None):
    if low is None or high is None:
        low, high = 0, len(arr) - 1
    if low >= high:
        return arr

    mid = low + (high - low)//2
    merge_sort(arr, low, mid)
    merge_sort(arr, mid+1, high)
    merge(arr, low, mid, high)
    return arr


def choose_pivot(low, high):
    return random.randrange(low, high+1)


def partition(arr, low, high):
    pivot_index = choose_pivot(low, high)
    arr[high], arr[pivot_index] = arr[pivot_index], arr[high]

    pivot_index = low
    for i in range(low, high):
        if arr[i] <= arr[high]:
            arr[pivot_index], arr[i] = arr[i], arr[pivot_index]
            pivot_index += 1
    arr[high], arr[pivot_index] = arr[pivot_index], arr[high]
    return pivot_index


def quick_sort(arr, low=None, high=None):
    if low is None or high is None:
        low, high = 0, len(arr) - 1
    if low >= high:
        return arr

    pivot_index = partition(arr, low, high)
    quick_sort(arr, low, pivot_index-1)
    quick_sort(arr, pivot_index+1, high)
    return arr


print(selection_sort([2, 5, 1, 3, 4, 8, 7, 6, 0, 10, 9, 6, 3]))
print(bubble_sort([2, 5, 1, 3, 4, 8, 7, 6, 0, 10, 9, 6, 3]))
print(insertion_sort([2, 5, 1, 3, 4, 8, 7, 6, 0, 10, 9, 6, 3]))
print(merge_sort([2, 5, 1, 3, 4, 8, 7, 6, 0, 10, 9, 6, 3]))
print(quick_sort([2, 5, 1, 3, 4, 8, 7, 6, 0, 10, 9, 6, 3]))
