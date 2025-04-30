# easy level problem 

# approach - 1 :
#     sort the array and return  the second largest element from the ascending order or second element from the 
#     descending order - takes extra time complexity for sorting the array
#     fails if there are duplicates (missed this point)

# approach - 2 :
        # find the first largest element in one iteration by recursive comparision and in the second
        # iteration ,find the second largest by comparing it with first largest element

def second_largest(arr):
    first_largest = -1e9
    sec_largest = -1e9
    for i in arr:
        if i > first_largest :
            sec_largest = first_largest
            first_largest = i
        elif i == first_largest:
            continue
        else:
            if i > sec_largest:
                sec_largest = i
    return sec_largest

# (can be written in a single elif condition instead of elif and else  -- elif i > second_largest and i != first_larget)

arr = [1,2,4,7,7,5]
print(second_largest(arr))
