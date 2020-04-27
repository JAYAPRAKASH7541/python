class Pokemon:
	sound_by_animal=""
	def __init__(self,name,level):
		self._master=None
		if name=="":
			raise ValueError("name cannot be empty")
		else:
			self._name=name
		if level <=0:
			raise ValueError("level should be > 0")
		else:
			self._level=level
	@property
	def master(self):
		if self._master==None:
			print("No Master")
		else:
			return self._master
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

class Island:
	
	total_islands=[]
	def __init__(self,name, max_no_of_pokemon, total_food_available_in_kgs):
		
		
		self._pokemon_left_to_catch=0
		self._name=name
		self._max_no_of_pokemon=max_no_of_pokemon
		self._total_food_available_in_kgs = total_food_available_in_kgs
		self.total_islands.append(self)
		
	@property
	def name(self):
		return self._name
	
	@property
	def pokemon_left_to_catch(self):
		return self._pokemon_left_to_catch
		
	@property
	def max_no_of_pokemon(self):
		return self._max_no_of_pokemon
	
	@property
	def total_food_available_in_kgs(self):
		return self._total_food_available_in_kgs
		
	def __str__(self):
		return ("{} - {} pokemon - {} food".format(self._name,
		self._pokemon_left_to_catch,self._total_food_available_in_kgs))
		
	def add_pokemon(self,pokemon):
		if self._pokemon_left_to_catch>=self._max_no_of_pokemon:
			print("Island at its max pokemon capacity")
		else:
			self._pokemon_left_to_catch+=1
	
	@classmethod
	def get_all_islands(cls):
		return cls.total_islands
	
		
class Trainer:
	def __init__(self,name):
		
		self._food_in_bag=0
		self._experience=100
		self._name=name
		self._current_island=None  #taking an attribute of none type
		self._max_food_in_bag=10*(self._experience)
		self.pokemon_list=[]
		
		
	@property
	def name(self):
		return self._name
		
	@property
	def food_in_bag(self):
		return self._food_in_bag
	
	@property
	def experience(self):
		return self._experience
	
	@property
	def max_food_in_bag(self):
		return self._max_food_in_bag
	
	@property
	def current_island(self):
		if(self._current_island==None):            #giving safe accesss
			print("You are not on any island")
		else:
			return self._current_island
			
	def move_to_island(self,island):
		self._current_island = island
	
	def collect_food(self):
		if self._current_island==None:
			print("Move to an island to collect food")
		else:
			if self._current_island._total_food_available_in_kgs>self._max_food_in_bag:
				if self._food_in_bag<self._max_food_in_bag:
					self._current_island._total_food_available_in_kgs-=self._max_food_in_bag
					self._food_in_bag+=self._max_food_in_bag
				else:
					self._food_in_bag=self._max_food_in_bag
			else:
				self._food_in_bag=self._current_island._total_food_available_in_kgs
				self._current_island._total_food_available_in_kgs=0
                
	def catch(self,pokemon):
		pokemon._master=self
		if  self._experience>=100*pokemon.level:
			print("You caught {}".format(pokemon.name))
			self._experience+=20
			self.pokemon_list.append(pokemon)
		else:
			print("You need more experience to catch {}".format(pokemon.name))
			
			
	def get_my_pokemon(self):
		return self.pokemon_list
		

'''
An island in the game is described by

its name
the maximum number of pokemon it can hold
total food available on the island
number of pokemon left to catch on the island
On creating a new island pokemon_left_to_catch should be 0
>>> island = Island(name="Island1", max_no_of_pokemon=5, total_food_available_in_kgs=10000)
>>> island.name
Island1
>>> island.max_no_of_pokemon
5
>>> island.total_food_available_in_kgs
10000
>>> island.pokemon_left_to_catch
0
>>> print(island)
Island1 - 0 pokemon - 10000 food 
You can add pokemon to an Island.
>>> island.pokemon_left_to_catch
0
>>> island.add_pokemon(pokemon)
>>> island.pokemon_left_to_catch
1
You can add only a maximum of max_no_of_pokemon pokemon to the Island.
>>> island.pokemon_left_to_catch
5
>>> island.max_no_of_pokemon
5
>>> island.add_pokemon(pokemon)  # Print
Island at its max pokemon capacity
>>> island.pokemon_left_to_catch
5
---------------------------------------------
# Task3
# Trainer
A Pokemon trainer is described by his/her

name: any string with which a trainer is referred, just like a name for humans.
experience: represents the experience of the trainer. experience is 100 for a newly created trainer. Every time a trainer catches a pokemon, his/her experience is increased (details are mentioned at catch method below)
max_food_in_bag: represents the max amount of food a trainer can carry along with him/her. max_food_in_bag increases with the trainers experience. i.e max_food_in_bag is equal to 10 x experience.
food_in_bag: represents the current amount of food a trainer has.
>>> trainer = Trainer(name="Bot") 
>>> trainer.name
Bot
>>> trainer.experience
100
>>> print(trainer)
Bot
>>> trainer.max_food_in_bag
1000
>>> trainer.food_in_bag
0
-----------------------------------------------------
# Task4
Trainers travel from one island to another to catch pokemon and gather food. Trainers should be shown all the available islands.

>>> Island.get_all_islands()
Island1 - 100 pokemon - 10000 food
Island2 - 24 pokemon - 12300 food
Island3 - 82 pokemon - 11830 food
Island4 - 192 pokemon - 101238 food
----------------------------------------------------
# Task5
Trainer can move from one island to another.
>>> trainer.move_to_island(island1)
>>> trainer.current_island == island1
True
>>> trainer.current_island  
Island1 - 0 pokemon - 10000 - food
If trainer is not on any island current_island should return the message mentioned below.
>>> trainer.current_island  # Print
You are not on any island
------------------------------------------------------
# Task6
Trainers can collect food from the island and store it in their bag.
>>> trainer.move_to_island(island)
>>> island.total_food_available_in_kgs
10000
>>> trainer.food_in_bag
0
>>> trainer.collect_food()
>>> island.total_food_available_in_kgs
9900
>>> trainer.food_in_bag
100
Trainer fills his/her bag with food just by calling the collect_food method once.
>>> island.total_food_available_in_kgs
9900
>>> trainer.food_in_bag
1000
>>> trainer.max_food_in_bag
1000
>>> trainer.collect_food()
>>> trainer.food_in_bag
1000
>>> island.total_food_available_in_kgs
9900
When a trainer collects food from an island, food in the island is decreased by the same amount.

If the trainer bag is full i.e., food_in_bag is equal to max_food_in_bag then collect_food doesn't decrease food on the island and also doesn't increase the food_in_bag.

If trainer is not on any island collect_food should behave as mentioned below.

>>> trainer.current_island  # Print
You are not on any island

>>> trainer.collect_food()  # Print
Move to an island to collect food
If the food on the island is less than the food required by the trainer, then your code should behave as below.
>>> island.total_food_available_in_kgs
90
>>> trainer.food_in_bag
0
>>> trainer.experience
100
>>> trainer.max_food_in_bag
1000
>>> trainer.collect_food()
>>> trainer.food_in_bag
90
>>> island.total_food_available_in_kgs
0
---------------------------------------------
# Task7
A trainer can catch a pokemon.
>>> pokemon.name
Pigetto
>>> pokemon.level 
1
>>> trainer.experience
100
>>> trainer.catch(pokemon)  # Print
You caught Pigetto
Every time a trainer catches a pokemon, their experience increases by the pokemon level x 20 points.
>>> pokemon.name
Pigetto
>>> pokemon.level 
1
>>> trainer.experience
100
>>> trainer.catch(pokemon)  # Print
You caught Pigetto
>>> trainer.experience
120
A trainer can catch a pokemon only if his/her experience >= 100 x pokemon.level
>>> pokemon.name
Pigetto
>>> pokemon.level 
2
>>> trainer.experience
100
>>> trainer.catch(pokemon)  # Print
You need more experience to catch Pigetto
-----------------------------------------------------
# Task8
A trainer can see the list of all pokemon he/she has caught.
>>> trainer.get_my_pokemon()
[Pigetto - Level 1]
get_my_pokemon should return a list of pokemon objects the trainer has caught.
--------------------------------------------------------------
# Task9
A pokemon remembers its trainer.

>>> pokemon.name
Pigetto
>>> pokemon.level 
1
>>> pokemon.master  # Print
No Master
>>> trainer.catch(pokemon)
>>> pokemon.master == trainer 
True
------------------------------
'''
