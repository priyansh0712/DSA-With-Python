l = [1,5,3,8,4,8]
left = 0
right = len(l)-1

def revrse(l,left,right):
    if left>=right:
        return l
    l[left],l[right] = l[right],l[left]
    revrse(l,left+1,right-1)

def r(l,left,right):
    revrse(l,left,right)
    return l

print(r(l,left,right))