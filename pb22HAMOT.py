
def solve():   
    fichier=open('p022_names.txt','r')
    L2=fichier.read()
    L1=L2.split('","')
    alpha='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    L=[]
    L1[0]='MARY'
    L1[-1]='ALONSO'
    compte=0
    for i in alpha:
        L.append(i)
    L1.sort()
    long=len(L1)
    for k in range(long):
        b=0
        for y in L1[k]:
            b+=alpha.index(y)+1
        compte+= b*(k+1)
    return(compte)

assert(solve())==871198282