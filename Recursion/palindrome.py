name = "MoMd"
start = 0
end = len(name)-1

def pali(name1,start,end):
    if name1[start] != name1[end]:
        return False
    if start>=end:
        return True
    pali(name1,start+1,end-1)

if pali(name,start,end):
    print(f"{name} is a palidrome string")
else:
    print(f"{name} is not a palidrome string")
