def remove_duplicates(arr):
    i = 0
    j = 1
    n = len(arr)
    while j < n:
        if arr[i] == arr[j]:
            j += 1
        else:
            i += 1
            arr[i] = arr[j]
    return i+1

arr = [1,2,2,3,3,4,5]
print(remove_duplicates(arr))




