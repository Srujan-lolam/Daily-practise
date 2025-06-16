# Brute force could be taking a temporary array of same size ,iterate through the original array elements from
# index 1 and store them in temporary array in index-1 position . after the completition of loop , store first
# element original array in last index of temporary array

# for i in range(n):
#     tmp[i-1] = arr[i]
# tmp[n-1] = arr[0] - this would take extra O(n) time complexity

# optimized approach

def left_rotate_by_one(arr):
    x = arr[0]
    n = len(arr)
    for i in range(1,n):
        arr[i-1] = arr[i]
    arr[n-1] = x
    return arr
arr = [1,2,3,4,5,6]
print(left_rotate_by_one(arr))