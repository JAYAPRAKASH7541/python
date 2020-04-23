class Animal:
    sound_by_animal=""
    make_breathe=""
    feed_grow=0
    def __init__(self,age_in_months,required_food_in_kgs,breed):
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
    def age_in_months(self):
        return self._age_in_months
    @property
    def breed(self):
        return self._breed
    
    @property
    def required_food_in_kgs(self):
        return self._required_food_in_kgs
    
    
    @classmethod
    def breathe(cls):
        print(cls.make_breathe)
    
    @classmethod
    def make_sound(cls):
        print(cls.sound_by_animal)
        
    def grow(self):
        self._age_in_months += 1
        self._required_food_in_kgs += self.feed_grow    
        
class Deer(Animal):
    sound_by_animal="Buck Buck"
    make_breathe="Breathe in air"
    feed_grow=2
    
class Lion(Animal):
    sound_by_animal="Roar Roar"
    make_breathe="Breathe in air"
    feed_grow=4
    
    
class Shark(Animal):
    sound_by_animal="Shark Sound"
    make_breathe="Breathe oxygen from water"
    feed_grow=8
    
class GoldFish(Animal):
    sound_by_animal="Hum Hum"
    make_breathe="Breathe oxygen from water"
    feed_grow=0.2
    

class Snake(Animal):
    sound_by_animal="Hiss Hiss"
    make_breathe="Breathe in air"
    feed_grow=0.5


class Zoo:
    pass


