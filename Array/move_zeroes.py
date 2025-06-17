def move_zeroes_to_end(arr):
    n = len(arr)
    i = 0
    j = 1
    while j < n:
        if (arr[i] != 0 and arr[j] == 0) or (arr[i] != 0 and arr[j] != 0 ):
            i += 1
            j += 1
        elif arr[i] == 0 and arr[j] != 0:
            arr[i],arr[j] = arr[j],arr[i]
            i += 1
            j += 1
        else:
            j += 1
    return arr
arr = [1 ,0 ,2 ,3 ,0 ,4 ,0 ,1]
print(move_zeroes_to_end(arr))