
Q1="select count(id) from movie where year <2000;"

Q2="select avg(rank) from movie where year==1991;"

Q3="select min(rank) from movie where year=1991;"

Q4 = '''select fname,lname from actor  Inner join cast  
on id = pid where mid = 27;'''

Q5 = '''select count(mid) from cast  Inner Join actor  on pid = id
where fname = 'Jon' and lname = 'Dough';'''

Q6='''select name from movie  where name like 'young latin girls%' 
and year between 2003 and 2006;'''
