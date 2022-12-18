class Engine:
    power: int
    brand: str

    def __init__(self, power: int, brand: str):
        self.power = power
        self.brand = brand

    def __repr__(self):
        return f"{self.brand} engine with {self.power} horse power"

class Person:
    age: int
    full_name: str

    def __init__(self, age: int, name: str):
        self.age = age
        self.full_name = name

    def __repr__(self):
        return f"{self.full_name} is {self.age} years old"

class Driver(Person):
    experience: int

    def __init__(self, age: int, name: str, experience: int):
        super().__init__(age, name)
        self.experience = experience

    def __repr__(self):
        return f"Driver {self.full_name} is {self.age} years old with {self.experience} years of experience"

class Car:
    brand: str
    car_class: str
    weight: int
    engine: Engine
    driver: Driver

    def __init__(self, brand, car_class, weight, engine, driver):
        self.brand = brand
        self.car_class = car_class
        self.weight = weight
        self.engine = engine 
        self.driver = driver 

    def start(self):
        print("Поехали")

    def stop(self):
        print("Останавливаемся")

    def turnLeft(self):
        print("Поворот налево")

    def turnRight(self):
        print("Поворот направо")

    def __repr__(self):
        return f"{self.brand} {self.car_class} car weighs {self.weight} kgs with {self.engine}.\n{self.driver}."

class Lorry(Car):
    carrying: int

    def __init__(self, brand, car_class, weight, engine, driver, carrying: int):
        super().__init__(brand, car_class, weight, engine, driver)
        self.carrying = carrying

    def __repr__(self):
        return f"{self.brand} {self.car_class} lorry weighs {self.weight} kgs with {self.engine} that can carry {self.carrying} kgs.\n{self.driver}."

class SportCar(Car):
    speed: float

    def __init__(self, brand, car_class, weight, engine, driver, speed: float):
        super().__init__(brand, car_class, weight, engine, driver)
        self.speed = speed

    def __repr__(self):
        return f"{self.brand} {self.car_class} sport car weighs {self.weight} kgs with {self.engine} and speed of {self.speed} km/h.\n{self.driver}."

engine = Engine(300, "Force Motors")
driver = Driver(19, "Adi Yeltay", 3)
myCar = Car("BMW", "high", "2000", engine, driver)
mySportCar = SportCar("Ferari", "sport", "1800", engine, driver, 300.0)
myLorry = Lorry("Toyota", "middle", "3500", engine, driver, 1000)

print(myCar)
print(mySportCar)
print(myLorry)