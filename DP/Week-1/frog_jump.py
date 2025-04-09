#APPROACH - 1 (RECURSION)
# def minimum_energy(n,curr_sum,final_energy,arr):
#     if n == 0:
#         final_energy = min(final_energy,curr_sum)
#         return final_energy
#     step_one = float('inf')
#     step_two = float('inf')
#     if n >= 1:
#         step_one = minimum_energy(n-1,curr_sum+abs(arr[n] - arr[n-1]),final_energy,arr)
#     if n >= 2:
#         step_two = minimum_energy(n-2,curr_sum+abs(arr[n] - arr[n-2]),final_energy,arr)
#     return min(step_one,step_two)
# n = 3
# final_energy = float('inf')
# curr_sum = 0
# arr = [10,30,20]
# print(minimum_energy(n-1,curr_sum,final_energy,arr))

#APPROACH - 2(MEMOIZATION)

# def minimum_energy(n,curr_sum,final_energy,arr,dp):
#     if n == 0:
#         final_energy = min(final_energy,curr_sum)
#         return final_energy
#     if dp[n] != -1:
#         return dp[n]
#     step_one = float('inf')
#     step_two = float('inf')
#     if n >= 1:
#         step_one = minimum_energy(n-1,curr_sum+abs(arr[n] - arr[n-1]),final_energy,arr,dp)
#     if n >= 2:
#         step_two = minimum_energy(n-2,curr_sum+abs(arr[n] - arr[n-2]),final_energy,arr,dp)
#     dp[n] = min(step_one,step_two)
#     return dp[n]
# n = 4
# final_energy = float('inf')
# curr_sum = 0
# arr = [10,30,20,40]
# dp = [-1]*(n)
# print(minimum_energy(n-1,curr_sum,final_energy,arr,dp))

#APPROACH - 3(TABULATION)
# def minimum_energy(n,dp,arr):
#     dp[0] = 0
#     dp[1] = abs(arr[0]-arr[1])
#     for i in range(2,n):
#         step_one = dp[i-1] + abs(arr[i-1]-arr[i])
#         step_two = dp[i-2] + abs(arr[i-2]-arr[i])
#         dp[i] = min(step_one,step_two)
#     return dp[n-1]
# n = 2
# arr = [10,20]
# dp = [float('inf')]*(n)
# print(minimum_energy(n,dp,arr))


#APPROACH - 4 (SPACE OPTIMIZATION)
def minimum_energy(n,arr):
    prev2 = 0
    prev = abs(arr[0]-arr[1])
    for i in range(2,n):
        one_jump = prev + abs(arr[i-1]-arr[i])
        two_jumps = prev2 + abs(arr[i-2]-arr[i])
        curr = min(one_jump,two_jumps)
        prev2 = prev
        prev = curr
    return prev
n = 6
arr = [30,10,60,10,60,50]
print(minimum_energy(n,arr))


