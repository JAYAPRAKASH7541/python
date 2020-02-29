# python
python notes
from collections import *
d=defaultdict(lambda:defaultdict(int))
for i in range(int(input())):
    a,b,c=input().split(";")
    d[a]['MP']+=0
    d[b]['MP']+=0
    d[a]['W']+=0
    d[b]['W']+=0
    d[a]['D']+=0
    d[b]['D']+=0
    d[a]['L']+=0
    d[b]['L']+=0
    d[a]['P']+=0
    d[b]['P']+=0
    
    d[a]['MP']+=1
    d[b]['MP']+=1
    if c=='win':
     d[a]['W']+=1
     d[a]['P']+=3
     d[b]['L']+=1
    if c=='loss': 
     d[a]['L']+=1
     d[b]['W']+=1
     d[b]['P']+=3
    if c=='draw':
        d[a]['D']+=1
        d[b]['D']+=1
        d[a]['P']+=1
        d[b]['P']+=1
        
print("{:<24}| {:>2} | {:>2} | {:>2} | {:>2} | {:>2} |".format('Team','MP','W','D','L','P'))
d=dict(sorted(d.items()))

for j in sorted(d,key=lambda x:d[x]['P'],reverse=True):
   print("{:<24}| {:>2} | {:>2} | {:>2} | {:>2} | {:>2} |".format(j,d[j]['MP'],d[j]['W'],d[j]['D'],d[j]['L'],d[j]['P']))
