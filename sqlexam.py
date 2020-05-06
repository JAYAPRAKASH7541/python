
Q1="select count(id) from movie where year <2000;"

Q2="select avg(rank) from movie where year==1991;"

Q3="select min(rank) from movie where year=1991;"

Q4 = '''select fname,lname from actor  Inner join cast  
on id = pid where mid = 27;'''

Q5 = '''select count(mid) from cast  Inner Join actor  on pid = id
where fname = 'Jon' and lname = 'Dough';'''

Q6='''select name from movie  where name like 'young latin girls%' 
and year between 2003 and 2006;'''

#Q7 ='''select distinct fname,lname from Director as d, MovieDirector as md, 
#Movie AS m where d.id = md.did AND md.mid = m.id AND group by m.id having count(m.id)>=1
#AND name LIKE 'Star Trek%';'''


Q7 ='''select distinct fname,lname from Director as d INNER JOIN MovieDirector as md
ON d.id = md.did INNER JOIN movie as m ON md.mid = m.id where name LIKE 'Star Trek%'
group by (d.id) having count(md.mid)>=1;'''

Q8='''select name from  Movie AS m ,MovieDirector AS md,Cast AS c ,
Director AS d,Actor AS a where m.id = md.mid AND md.mid = c.mid 
AND d.id = md.did AND a.id = c.pid AND a.fname = 'Jackie (I)' 
AND d.fname = 'Jackie (I)' AND a.lname = 'Chan' AND d.lname = 'Chan'
ORDER BY name ASC;'''

Q9 = '''select fname,lname FROM Director AS d,MovieDirector AS md, Movie AS m
where md.did = d.id and md.mid = m.id and m.year = 2001 GROUP BY d.id
Having COUNT(m.id) >=4 ORDER BY fname ASC,lname DESC;'''

Q10='''select gender,count(*) from actor group by gender order by gender asc;'''

Q11= '''SELECT m1.name,m2.name,m1.rank,m1.year FROM Movie as m1 INNER JOIN
Movie as m2 ON m1.rank = m2.rank AND m1.year = m2.year WHERE m1.id > m2.id
ORDER BY m1.name LIMIT 100;'''


Q12='''select a.fname,m.year,avg(rank) as rank from movie as m Inner Join cast as c 
on m.id = c.mid Inner join actor as a on a.id = c.pid group by year,a.id
order by a.fname asc,m.year desc limit 100;'''


Q13='''SELECT a.fname,d.fname,AVG(rank) as score FROM MovieDirector as md
INNER JOIN Cast as c ON c.mid = md.mid INNER JOIN Movie as m ON m.id = md.mid
INNER JOIN Actor as a ON a.id = c.pid INNER JOIN Director as d ON d.id = md.did
GROUP BY d.id,a.id HAVING COUNT(*) >=5 ORDER BY score DESC,d.fname ASC,
a.fname DESC LIMIT 100;'''

