Liste1=liste(

def solve(n):
    c=str(n)
    b=0
    for k in c:
        b+=int(k)
    return(b)

assert(solve(2**15))==26
print(solve(2**1000))