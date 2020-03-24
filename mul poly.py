Input:
4
0 5
1 0
2 10
3 6
3
0 1
1 2
2 4

Output:
24x^5 + 52x^4 + 26x^3 + 30x^2 + 10x^1 + 5

--------
from  itertools import product
x = int(input())
ap = []
ac = []
for i in range(x):
    n,m = input().split(" ")
    ap.append(int(n))
    ac.append(int(m))
y = int(input())
bp = []
bc = []
for i in range(y):
    n,m = input().split(" ")
    bp.append(int(n))
    bc.append(int(m))
pl = list(product(ap,bp))
cl = list(product(ac,bc))
d = {}
for i in range(len(pl)):
    g = pl[i][0] + pl[i][1]
    h = cl[i][0] * cl[i][1]
    if g not in d:
        d[g] = h
    else:
        d[g]+=h
d1={}
for i in d:
    if d[i]!=0:
        d1.update({i:d[i]})
d1 =  (sorted(d1.items(),key = lambda x: x[0],reverse=True))
if len(d1)==0:
    print("0")
else:
    a=[]
    b=[]
    for k,v in d1:
        a.append("{}x^{}".format(v,k))
        b=(" + ").join(a)
        b=b.replace('x^0','')
        b=b.replace(' + -',' - ')
print(b,end="")
