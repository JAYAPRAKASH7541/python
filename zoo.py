class Animal:
	
	feed_grow=0
	sound_by_animal=""
	
	def __init__(self,age_in_months,breed,required_food_in_kgs):
		if age_in_months !=1:
			raise ValueError("Invalid value for field age_in_months: {}".format(age_in_months))
		else:
			self._age_in_months=age_in_months
		if required_food_in_kgs <=0:
			raise ValueError("Invalid value for field required_food_in_kgs: {}".format(required_food_in_kgs))
		else:
			self._required_food_in_kgs=required_food_in_kgs
		self._breed=breed
	
	
	@property
	def required_food_in_kgs(self):
		return self._required_food_in_kgs
		
	@property
	def age_in_months(self):
		return self._age_in_months
		
	@property
	def breed(self):
		return self._breed
		
	def grow(self):
		self._age_in_months+=1
		self._required_food_in_kgs+=self.feed_grow
		
	@classmethod
	def make_sound(cls):
		print(cls.sound_by_animal)

class Land_animal:
	
	make_breathe="Breathe in air"
	
	@classmethod
	def breathe(cls):
		print(cls.make_breathe)
		
class Water_animal:
	
	make_breathe="Breathe oxygen from water"
	
	@classmethod
	def breathe(cls):
		print(cls.make_breathe)

class Hunting_animal:
	
	animal="Deer"
	hunted_animal="deers"
	
	def hunt(self,zoo):
		if self.animal in zoo.total_animals:
				zoo.total_animals.remove(self.animal)
				zoo.count_animals()
		else:
				print("No {} to hunt".format(self.hunted_animal))
			
class Deer(Animal,Land_animal):
	
	sound_by_animal = "Buck Buck"
	feed_grow = 2
	name="Deer"

class Lion(Animal,Land_animal,Hunting_animal):
	
	sound_by_animal = "Roar Roar"
	feed_grow = 4
	name="Lion"

class Shark(Animal,Water_animal,Hunting_animal):
	
	sound_by_animal = "Shark Sound"
	feed_grow = 8
	animal="GoldFish"
	hunted_animal ="GoldFish"
	name="Shark"
	
	
	
	
class GoldFish(Animal,Water_animal):
	
	sound_by_animal = "Hum Hum"
	feed_grow = 0.2
	name="GoldFish"


class Snake(Animal,Land_animal,Hunting_animal):
	
	sound_by_animal = "Hiss Hiss"
	feed_grow = 0.5
	name="Snake"
	
class Zoo:
	
	total_zoo_animals=[]
	def __init__(self):
		self._reserved_food_in_kgs=0
		self.total_animals=[]
	
	@property
	def reserved_food_in_kgs(self):
		return self._reserved_food_in_kgs
		
	def count_animals(self):
		return len(self.total_animals)
	
	def add_food_to_reserve(self,food_amount):
		self._reserved_food_in_kgs+=food_amount
		
	def add_animal(self,animal):
		self.total_animals.append(animal.name)
		self.total_zoo_animals.append(animal.name)
		
	def feed(self,animal):
		feed_required = animal._required_food_in_kgs
		if self._reserved_food_in_kgs > feed_required:
			self._reserved_food_in_kgs -=feed_required
			animal.grow()
			
	@classmethod
	def count_animals_in_all_zoos(cls):
		return len(cls.total_zoo_animals)
	
	@staticmethod
	def count_animals_in_given_zoos(zoo):
		count=0
		for zoo_park in zoo:
			count+=zoo_park.count_animals()
		return count	
		
