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


print(merge_sort([2, 5, 1, 3, 4, 8, 7, 6, 0, 10, 9, 6, 3]))
