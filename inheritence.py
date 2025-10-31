#1
class person:
    def __init__(self,name):
        self.name = name
    def intro(self):
        print("Hello, I am a person.")  
        
class man(person):
    def __init__(self,name):
        super().__init__(name)
        self.name = name + "and I am a man"



obj = man("akram")
obj.intro()

#2
class Vehicle:
    def __init__(self,move):
        self.move = move
    def move_vehicle(self):
        print("Vehicle is moving", self.move)

class Car(Vehicle):
    def __init__(self, move,honk):
        super().__init__(move)
        self.honk = honk

    def honk_horn(self):
        print("Car is honking", self.honk)


car = Car("fast", "peeeeeeeeeee!")
car.move_vehicle()
car.honk_horn()
        
#3
class Account:
    def __init__(self,balance):
        self.balance = balance
    
        
    def make_deposit(self):
        self.deposit = self.balance
        print("Deposit made:", self.deposit)
        print("Current balance:", self.balance)
    
class SavingsAccount(Account):
    def __init__(self, deposit, interest):
        super().__init__(deposit)
        self.interest= interest

    def add_interest(self):
        print("Interest added:", self.interest)
        self.deposit += self.interest
        print("New balance:", self.deposit)

savings = SavingsAccount(100000, 500)
savings.make_deposit()
savings.add_interest()


#4
class Shape:
    def __init__(self,area):
        self.area = area

    def calculate_area(self):
        print("Area of the shape is:", self.area)

class Rectangle(Shape):
    def __init__(self, area):
        super().__init__(area)

