from car import Car
class Truck(Car):
	def __init__(self,color,max_speed,acceleration,tyre_friction,max_cargo_weight):
		super().__init__(color,max_speed,acceleration,tyre_friction)
		self._max_cargo_weight=max_cargo_weight
		self._loads=0
	@property
	def max_cargo_weight(self):
		return self._max_cargo_weight
	@property
	def loads(self):
		return self._loads

	def load(self,cargo_weight):
		if cargo_weight <0:
			raise ValueError("Invalid value for cargo_weight")
		#if self._is_engine_started:
		if self._current_speed == 0:
			if self._loads+cargo_weight >= self._max_cargo_weight:
				print("Cannot load cargo more than max limit: {}".format(self.max_cargo_weight))
			else:
				self._loads+=cargo_weight
		else:
			print("Cannot load cargo during motion")

				    
	def unload(self,cargo_weight):
		if cargo_weight <0:
			raise ValueError("Invalid value for cargo_weight")
		#if self._is_engine_started:
		if self._current_speed == 0:
			self._loads-=cargo_weight
		else:
			print("Cannot unload cargo during motion")
				    
					
	def sound_horn(self):
		if self.is_engine_started:
			print("Honk Honk")
		else:
			print("Start the engine to sound_horn")
				   
		
		
