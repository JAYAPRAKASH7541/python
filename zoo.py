class Animal:
    animal_sound = 'sound made by animal'
    breathe_what = 'what does an animal breathe'
    feed_grow = 0
    def __init__(self,age_in_months,breed,required_food_in_kgs):
        self.check_is_possitive(required_food_in_kgs,'required_food_in_kgs')
        # if required_food_in_kgs <= 0:
        #     raise ValueError(f'Invalid value for field required_food_in_kgs: {required_food_in_kgs}')
        if age_in_months != 1:
            raise ValueError(f'Invalid value for field age_in_months: {age_in_months}')
        self._age_in_months = age_in_months
        self._breed = breed
        self._required_food_in_kgs = required_food_in_kgs
        
    @property
    def age_in_months(self):
        return self._age_in_months
    @property
    def breed(self):
        return self._breed
    
    @property
    def required_food_in_kgs(self):
        return self._required_food_in_kgs
    
    @classmethod
    def make_sound(cls):
        print(cls.animal_sound)
        return
    
    @classmethod
    def breathe(cls):
        print(cls.breathe_what)
        return

    def grow(self):
        self._age_in_months += 1
        self._required_food_in_kgs += self.feed_grow    
       
    @staticmethod
    def check_is_possitive(val,name):
        if val <= 0:
            raise ValueError(f'Invalid value for field {name}: {val}')

class Deer(Animal):
    animal_sound = 'Buck Buck'
    breathe_what = 'Breathe in air'
    feed_grow = 2
    
class Lion(Animal):
    animal_sound = 'Roar Roar'
    breathe_what = 'Breathe in air'
    feed_grow = 4
    
    @staticmethod
    def hunt(zoo):
        no_deers = zoo._animals_in_zoo.count('Deer')
        if no_deers > 0:
            zoo._animals_in_zoo.remove('Deer')
        else:
            print('No deers to hunt')    

class Shark(Animal):
    animal_sound = 'Shark Sound'
    breathe_what = 'Breathe oxygen from water'
    feed_grow = 8
    
    @staticmethod
    def hunt(zoo):
        no_gold_fish = zoo._animals_in_zoo.count('GoldFish')
        if no_gold_fish > 0:
            zoo._animals_in_zoo.remove('GoldFish')
        else:
            print('No GoldFish to hunt')
    
class GoldFish(Animal):
    animal_sound = 'Hum Hum'
    breathe_what = 'Breathe oxygen from water'
    feed_grow = 0.2
    
class Snake(Animal):
    animal_sound = 'Hiss Hiss'
    breathe_what = 'Breathe in air'
    feed_grow = 0.5
    
    @staticmethod
    def hunt(zoo):
        no_deers = zoo._animals_in_zoo.count('Deer')
        if no_deers > 0:
            zoo._animals_in_zoo.remove('Deer')
        else:
            print('No deers to hunt')
    
class Zoo:
    all_the_zoos = []
    def __init__(self):
        self._reserved_food_in_kgs = 0
        self._animals_in_zoo = []
        type(self).all_the_zoos.append(self)
        
    @property
    def reserved_food_in_kgs(self):
        return self._reserved_food_in_kgs
        
    def add_food_to_reserve(self,food_amount):
        self._reserved_food_in_kgs += food_amount
        
    def add_animal(self,animal):
        self._animals_in_zoo.append(type(animal).__name__)
        
    def feed(self,animal):
        feed_required = animal._required_food_in_kgs
        if self._reserved_food_in_kgs >= feed_required:
            animal.grow()
            self._reserved_food_in_kgs -= feed_required
    
    def count_animals(self):
        return len(self._animals_in_zoo)
        
    @classmethod
    def count_animals_in_all_zoos(cls):
        total_no_animals_in_all_zoos = 0
        for zoo in cls.all_the_zoos:
            total_no_animals_in_all_zoos += zoo.count_animals()
        return total_no_animals_in_all_zoos
        
    @staticmethod
    def count_animals_in_given_zoos(zoos):
        toatl_no_animals_in_given_zoos = 0
        for zoo in zoos:
            toatl_no_animals_in_given_zoos += zoo.count_animals()
        return toatl_no_animals_in_given_zoos







