def house_robber(arr,idx,n):
    prev2 = arr[idx]
    prev = max(arr[idx],arr[idx+1])
    for i in range(idx+2,n):
        curr = max(arr[i]+prev2,prev)
        prev2 = prev
        prev = curr
    return prev
arr = [49]
n = len(arr)
if n == 1:
    print(arr[0])
elif n == 2:
    print(max(arr[0],arr[1]))
else:
    print(max(house_robber(arr,0,n-1),house_robber(arr,1,n)))

