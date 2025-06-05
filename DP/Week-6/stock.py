def buy_and_sell(arr,pre_idx,curr_idx):
    max1 = -1e9
    while curr_idx < len(arr):
        if arr[curr_idx]-arr[pre_idx] < 0:
            pre_idx = curr_idx
        else:
            max1 = max(max1,arr[curr_idx]-arr[pre_idx])
            curr_idx += 1
    return max1
arr = [7,1,5,3,6,4]
print(buy_and_sell(arr,0,0))