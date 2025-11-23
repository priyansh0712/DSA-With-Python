# Asceding order

def bubble_asceding(l):
    is_swap = False
    for i in range(len(l)-1,-1,-1):
        for j in range(0,i):
            if l[j]>l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]
                is_swap=True
        if is_swap==False:
            return

# Descending order

def bubble_desceding(l):
    is_swap = False
    for i in range(len(l)-1,-1,-1):
        for j in range(0,i):
            if l[j]<l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]
                is_swap=True
        if is_swap==False:
            return
        
        
arr = [1,3,6,2,9,5,10]
bubble_asceding(arr)
print(arr)
bubble_desceding(arr)
print(arr)