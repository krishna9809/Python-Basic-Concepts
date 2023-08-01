# object oriented programming 

# Class : Class is a template/blue-print for real-world entities

# ==> Class is a user-defined data-type

# Objects ==> Objects are specific instances of a class

#Creating the 'Phone' Class
class Phone:
    def make_call(self):
        print("Making Call")
    def play_game(self):
        print("Playing Game")

#Instantiating the'p1' object
p1 = Phone()

#Invoking methods through object
p1.make_call()
# ==> output = Making Call
# p1.play_game()
# ==> output = Playing Game

# Adding parameters to the class

class Phone:
    def set_color(self,color):
        self.color = color
    def set_cost(self,cost):
        self.cost = cost
    def show_color(self):
        return self.color
    def show_cost(self):
        return self.cost
    def make_call(self):
        print("Making Call")
    def Play_game(self):
        print("Playng Game")

p2 = Phone()
p2.set_color("blue")
p2.set_cost(5000)

print(p2.show_color())
print(p2.show_cost())


class Employee:
    def __init__(self,name,age,salary,gender):
        self.name = name
        self.age = age
        self.salary = salary
        self.gender = gender
    def employee_detail(self):
        print("Employee name is ",self.name)
        print("Employee age is ",self.age)
        print("Employee salary is ",self.salary)
        print("Employee gender is ",self.gender)

e2 = Employee('sam',35,95000,'male')

e2.employee_detail()

#Inheritance in python

# ==> With inheritance one class can derive the properties of another class

class Vehical:
    def __init__(self,milenge,cost):
        self.milenge = milenge
        self.cost = cost
    def show_detail(self):
        print("I am  Vehical")
        print("Milenge is ",self.milenge)
        print("my cost is",self.cost)

v1 = Vehical(400,500)

v1.show_detail()

class Car(Vehical):
    def show_car(self):
        print("I am car")

c1 = Car(200,300)

c1.show_detail()

c1.show_car()

# over-ride init 

class Jeep(Vehical):
    def __init__(self, milenge, cost,tyre,rent):
        super().__init__(milenge,cost)
        self.tyre = tyre
        self = rent
    def show_jeep(self):
        print("in this tyres are",self.tyre)
        print("Rent of this Jeep is ",self.rent)

j1 = Jeep(6000,1400,6,666666)

j1.show_detail()


# types of inheritance

#==> multiple inheritance

class Parent1:
    def assing_str1(self,str1):
        self.str1 = str1
    def show_str1(self):
        return self.str1

class Parent2:
    def assing_str2(self,str2):
        self.str2 = str2
    def show_str2(self):
        return self.str2

class derived(Parent1,Parent2):
    def assing_str3(self,str3):
        self.str3 = str3
    def show_str3(self):
        return self.str3

s1 = derived()

s1.assing_str1('cdscds')
s1.assing_str2('dadsd')
s1.assing_str3('cccc')
print(s1.show_str1())

# multi-level inheritance

class Parent:
    def assing_name(self,name):
        self.name = name
    def show_name(self):
        return self.name
    
class Child(Parent):
    def assing_age(self,age):
        self.age = age
    def show_age(self):
        return self.age
    
class GrandChild(Child):
    def assing_gender(self,gender):
        self.gender = gender
    def show_gender(self):
        return self.gender

g1 = GrandChild()

g1.assing_name('krishna')
g1.assing_age(15)
g1.assing_gender('male')

print(g1.show_name())
print(g1.show_age())
print(g1.show_gender())