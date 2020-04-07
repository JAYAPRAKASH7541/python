class Car:
	def __init__(self,color,acceleration):
		self.color=color
		self.acceleration=acceleration
		self.speed=0
	def accelerate(self):
		print("speed  up bruh!!!")
		self.speed+=self.acceleration
	
	def apply_brakes(self):
		print("brake bro reduce the speed bruh!!!! ")
		self.speed-=10


car1=Car("green",60)

print(car1.speed)
print(car1.color)
car1.accelerate()
print(car1.speed)
car1.apply_brakes()
print(car1.speed)
#-------------
car2=Car("black",40)
print(car2.color)
print(car2.speed)
car2.accelerate()
print(car2.speed)
car2.apply_brakes()
print(car2.speed)


		
		
	
