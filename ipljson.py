sample_output = """[
    {
        "Team": "Chennai Super Kings",
        "Matches Played": 2,
        "Total Points": 4,
        "Won": 1,
        "Tied": 1,
        "Lost": 0
    },
    {
        "Team": "Mumbai Indians",
        "Matches Played": 2,
        "Total Points": 4,
        "Won": 1,
        "Tied": 1,
        "Lost": 0
    },
    {
        "Team": "Delhi Capitals",
        "Matches Played": 3,
        "Total Points": 3,
        "Won": 0,
        "Tied": 3,
        "Lost": 0
    },
    {
        "Team": "Rajasthan Royals",
        "Matches Played": 2,
        "Total Points": 3,
        "Won": 1,
        "Tied": 0,
        "Lost": 1
    },
    {
        "Team": "Rajasthan Royal",
        "Matches Played": 1,
        "Total Points": 1,
        "Won": 0,
        "Tied": 1,
        "Lost": 0
    },
    {
        "Team": "Kolkata Knight Riders",
        "Matches Played": 1,
        "Total Points": 0,
        "Won": 0,
        "Tied": 0,
        "Lost": 1
    },
    {
        "Team": "Sunrisers Hyderabad",
        "Matches Played": 1,
        "Total Points": 0,
        "Won": 0,
        "Tied": 0,
        "Lost": 1
    }
]
"""
import json
n=int(input())
d={}
for i in range(n):
    t1,t2,r=input().split(';')
    if t1 not in d:
        d[t1]=[r]
    else:
        d[t1].append(r)
    if t2 not in d:
        if r == 'win':
            d[t2]=['loss']
        elif r=='loss':
            d[t2]=['win']
        elif r=='draw':
            d[t2]=['draw']
    else:
        if r == 'win':
            d[t2].append('loss')
        elif r=='loss':
            d[t2].append('win')
        elif r=='draw':
            d[t2].append('draw')
list1 = []
dict1 = {}
for t,mp in d.items():
    up_dict = {}
    up_dict["Team"] = t
    up_dict["Matches Played"] = len(mp)
    points = 0
    for res in mp:
        if res == 'win':
            points +=3
        elif res == 'draw':
            points +=1
    up_dict["Total Points"] = points
    dict1[t] = points
    up_dict["Won"] = mp.count('win')
    up_dict["Tied"] = mp.count('draw')
    up_dict["Lost"] = mp.count('loss')
    list1.append(up_dict)
dict1 = dict(sorted(dict1.items()))
dict1= dict(sorted(dict1.items(),key = lambda x : -x[1]))
f_list = []
for i,j in dict1.items():
    for k in list1:
        if k["Team"] == i:
            f_list.append(k)
            break
json_op = json.dumps(f_list,indent=4)
print(json_op)
