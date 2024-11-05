class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self._model = model #Protected
        self.__year = year #Private
    
    def get_year(self):
       return self.__year 
    
    def get_brand(self):
        print(f"band: {self.brand}")
        
    def set_year(self, year):
        self.__year = year   

car  = Car("Marcedes", "G wargon", 2020)

car.brand = "BMW"
car._model = "M70"
car.set_year(2022)

print(f"brand: {car.brand}")
print(f"model: {car._model}")
print(f"year: {car.set__year}")
      