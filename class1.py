#---------------------object instantiation-----------------
'''class Person:
	pass
jai=Person()#INSTANTIATION
print(type(jai))
s=type(jai) == Person
print(s)'''
#-------------self description---------------------------
'''class Person:
	def say_hello(self):
		print("Hello")
		print(self)
		print(jai)
jai=Person()
#jai.say_hello()

jai.say_hello()

#methods are ment to be objects'''
#----------------------keyword arguments and positional arguments------------------------------
'''class Person:
	def greet(self,name="ajay"):
		return "Hello {}".format(name)

jai=Person()
greets=jai.greet("prakash")
print(greets)
s=jai.greet()
print(s)'''
#---------------special method init-method(no return value)----------------------------------
'''class Person:
	def __init__(self):
		print("hello")

jai=Person()'''
#-------------------------------------------------
'''class Person:
	def __init__(self,name):
		print("hello, Im {}!".format(name))

Person("jaiip")
p=Person("jaaa")
print(p)
#print(type(p))'''
#--------attributes of object-------------------------------------
'''class Person:
      def __init__(self,full_name,last_name):
      	self.name=full_name
      	self.name1=last_name
p=Person("jaip","matam")
s=p.name
h=p.name1
print(s,h)'''
#----------------------any method we can access using self-------------------------
'''class Person:
	def __init__(self,full_name):
		self.name=full_name
	def say_hello(self):
	  	print("hello im {}!".format(self.name))
	  	
p=Person("jaip")
p.say_hello()'''
#---------------------------------------------

		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		


























