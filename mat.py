import re
s = input().rstrip().split()
n = int(s[0])
m = int(s[1])
matrix = []
for _ in range(n):
    item = input()
    matrix.append(item)
dec = ""
for c in range(m):
    for r in range(n):
        dec += matrix[r][c]        
print(re.sub(r"(?<=\w)([^\w]+)(?=\w)", " ", dec))
