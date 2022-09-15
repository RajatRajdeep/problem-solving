import random


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


print(quick_sort([2, 5, 1, 3, 4, 8, 7, 6, 0, 10, 9, 6, 3]))
