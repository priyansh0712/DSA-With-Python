# For Merge two sort array
def two_merge(left,right):
    result = []
    i,j = 0,0
    n,m = len(left),len(right)
    while i<n and j<m:
        if left[i]<=right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    if i<n:
        while i<n:
            result.append(left[i])
            i+=1
    if j<m:
        while j<m:
            result.append(right[j])
            j+=1
    return result

# for divide and final sort array
def sort_array(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left_part = arr[:mid]
    right_part = arr[mid:]
    left = sort_array(left_part)
    right = sort_array(right_part)
    
    return two_merge(left,right)

l = [3,5,2,6,8,3,7,3,1,4,2]
print(sort_array(l))
