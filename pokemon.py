class Pokemon:
	sound_by_animal=""
	def __init__(self,name,level):
		if name=="":
			raise ValueError("name cannot be empty")
		else:
			self._name=name
		if level <=0:
			raise ValueError("level should be > 0")
		else:
			self._level=level
	
	@property
	def level(self):
		return self._level
	
	@property
	def name(self):
		return self._name
		
	def __str__(self):
		return ("{} - Level {}".format(self.name,self.level))
		
		
	@classmethod
	def make_sound(cls):
		print(cls.sound_by_animal)
		
		
'''class Attack_animal(Pokemon):
	
	type_attack=""
	
	@classmethod
	def attack(cls):
		print("{} with {} damage".format(cls.attack,cls.level))'''
	
class Running_animal:
	
	run_animal=""
	
	@classmethod
	def run(cls):
		print("{} running...".format(cls.run_animal))
		

class Swimming_animal:
	
	swim_animal=""
	
	@classmethod
	def swim(cls):
		print("{} swimming...".format(cls.swim_animal))
		
class Flying_animal:
	
	fly_animal=""
	
	@classmethod
	def fly(cls):
		print("{} flying...".format(cls.fly_animal))

class Pikachu(Pokemon,Running_animal):
	
	sound_by_animal="Pika Pika"
	run_animal="Pikachu"

	def attack(self):
		self.type_attack="Electric attack"
		print("{} with {} damage".format(self.type_attack,(self.level*10)))
		

class Squirtle(Pokemon,Running_animal,Swimming_animal):
	
	sound_by_animal="Squirtle...Squirtle"
	run_animal="Squirtle"
	swim_animal="Squirtle"
	
	def attack(self):
		self.type_attack="Water attack"
		print("{} with {} damage".format(self.type_attack,(self.level*9)))
	
class Pidgey(Pokemon,Flying_animal):
	
	sound_by_animal="Pidgey...Pidgey"
	fly_animal="Pidgey"
	
	def attack(self):
		self.type_attack="Air attack"
		print("{} with {} damage".format(self.type_attack,(self.level*5)))
	
class Swanna(Pokemon,Flying_animal,Swimming_animal):
	
	sound_by_animal="Swanna...Swanna"
	fly_animal="Swanna"
	swim_animal="Swanna"
	
	def attack(self):
		self.type_attack="Water attack"
		self.types_attack="Air attack"
		print("{} with {} damage".format(self.type_attack,(self.level*9)))
		print("{} with {} damage".format(self.types_attack,(self.level*5)))

class Zapdos(Pokemon,Flying_animal):
	
	sound_by_animal="Zap...Zap"
	fly_animal="Zapdos"
	
	def attack(self):
		self.type_attack="Electric attack"
		self.types_attack="Air attack"
		print("{} with {} damage".format(self.type_attack,(self.level*10)))
		print("{} with {} damage".format(self.types_attack,(self.level*5)))

		
	
	#task1
