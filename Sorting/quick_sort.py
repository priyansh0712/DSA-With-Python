def partition(n, low, high):
    pivot = n[low]
    i = low + 1
    j = high
    while True:
        while i <= high and n[i] <= pivot:
            i += 1
        while j >= low + 1 and n[j] > pivot:
            j -= 1
        if i <= j:
            n[i], n[j] = n[j], n[i]
        else:
            break
    n[low], n[j] = n[j], n[low]
    return j
            
def quick_sort(n,low,high):
    if low<high:
        part_index = partition(n,low,high)
        quick_sort(n,low,part_index-1)
        quick_sort(n,part_index+1,high)
        
# Calling 
num = [4,1,7,6,3,2,8]
quick_sort(num,0,len(num)-1)
print("Sorted num : ",num)