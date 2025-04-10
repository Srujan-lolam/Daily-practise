# APPROACH - 1 (RECURSION)
def minimum_energy(n,curr_sum,final_energy,arr):
    if n == 0:
        final_energy = min(final_energy,curr_sum)
        return final_energy
    step_one = float('inf')
    step_two = float('inf')
    if n >= 1:
        step_one = minimum_energy(n-1,curr_sum+abs(arr[n] - arr[n-1]),final_energy,arr)
    if n >= 2:
        step_two = minimum_energy(n-2,curr_sum+abs(arr[n] - arr[n-2]),final_energy,arr)
    return min(step_one,step_two)
n = 3
final_energy = float('inf')
curr_sum = 0
arr = [10,30,20]
print(minimum_energy(n-1,curr_sum,final_energy,arr))