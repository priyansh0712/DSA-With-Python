# Asceding order

def ascending(arr):
    n = len(arr)
    for i in range(0,n):
        min_index = i
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index = j
        arr[min_index],arr[i] = arr[i],arr[min_index]
        

# Descending Order
        
def descending(arr):
    n = len(arr)
    for i in range(0,n):
        max_index = i
        for j in range(i+1,n):
            if arr[j]>arr[max_index]:
                max_index = j
        arr[max_index],arr[i]=arr[i],arr[max_index]
        
# Printing
    
l = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
ascending(l)
print("Ascending order",l)
descending(l)
print("Descending order",l)