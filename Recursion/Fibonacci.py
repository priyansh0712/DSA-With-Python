n = 10
a = 0
b = 1

def fibo(n,a,b):
    if n<=0:
        return
    print(a,end=" ")
    fibo(n-1,b,a+b)
fibo(n,a,b)