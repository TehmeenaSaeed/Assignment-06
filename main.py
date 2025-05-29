# 1. using self
# assignment a class student with attributes name and marks. use the self
# keyword to initialize these values via a constructor. () that prints student details.

class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def display(self):
        return(f'Name: {self.name}, Mark: {self.marks}') 

student1:Student = Student("Tehmeena Malik",95)
student2:Student = Student("Ali Malik",85)
print("Student 1 Details:",student1.display())
print(student1.name,student1.marks)
print("Student 2 Details:",student2.display())

# 2. Using cls

# Assignment:
# Create a class Counter that keeps track of how many objects have been created. Use a class variable and a class method with cls to manage and display the count.

class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def  display_count(cls):
         return f'Total objects created: {cls.count}'
    
obj1 : Counter = Counter()
obj2 : Counter = Counter()
obj3 : Counter = Counter()
print(Counter.display_count())

# 3. Public Variables and Methods

# Assignment:
# Create a class Car with a public variable brand and a public method start(). Instantiate the class and access both from outside the class.


class Car:
    def __init__(self,brand):
        self.brand = brand
        
    def start(self):
        return f'{self.brand} is starting.'

car:Car = Car("Toyota")
print(car.brand)
print(car.start())     

# 4. Class Variables and Class Methods

# Assignment:
# Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name) that allows changing the bank name. Show that it affects all instances.


class Bank:
    bank_name = "ABC Bank"

    @classmethod
    def changed_bank_name(cls, name):
        cls.bank_name = name

b1:Bank = Bank()
print(b1.bank_name)
b2:Bank = Bank()
print(b2.bank_name)
Bank.changed_bank_name("XYZ Bank")
print(b1.bank_name)
print(b2.bank_name) 

# 5. Static Variables and Static Methods

# Assignment:
# Create a class MathUtils with a static method add(a, b) that returns the sum. No class or instance variables should be used.


class Mathutils:
    @staticmethod
    def add(a,b):
        return a + b
    
print(Mathutils.add(5,10))

# 6. Constructors and Destructors

# Assignment:
# Create a class Logger that prints a message when an object is created (constructor) and another message when it is destroyed (destructor).


class Logger:
    def __init__(self):
        print("Logger object created.")

    # def __del__(self):
    #    print("Logger object destroyed.")  

log:Logger = Logger()
del log  

# 7. Access Modifiers: Public, Private, and Protected

# Assignment:
# Create a class Employee with:

# a public variable name,

# a protected variable _salary, and

# a private variable __ssn.

# Try accessing all three variables from an object of the class and document what happens.
class  Employee:
    def __init__(self,name,salary,ssn):
        self.name = name
        self._salary = 5000
        self.__ssn = 132-45-6754

emp1 : Employee = Employee("Tehmeena Malik",5000,"132-45-8976")   
print(emp1.name)
print(emp1._salary)
#print(emp1.__ssn)     
print(emp1._Employee__ssn)

# 8. The super() Function

# Assignment:
# Create a class Person with a constructor that sets the name. Inherit a class Teacher from it, add a subject field, and use super() to call the base class constructor.     


class person:
    def __init__(self,name):
        self.name = name

class Teacher(person):
    def __init__(self,name,subject):
        super().__init__(name)
        self.subject = subject   

teacher: Teacher = Teacher("Tehmeena Malik","English")  
print(f'Name: {teacher.name}, Subject: {teacher.subject}') 

# 9. Abstract Classes and Methods

# Assignment:
# Use the abc module to create an abstract class Shape with an abstract method area(). Inherit a class Rectangle that implements area().


from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self,height,width):
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width
    
rect1 :Rectangle = Rectangle(5.8,10.6)
print(f'Aera of Rectangle: {rect1.area()}')

# 10. Instance Methods

# Assignment:
# Create a class Dog with instance variables name and breed. Add an instance method bark() that prints a message including the dog's name.


class Dog:
    def __init__(self,name,breed):
        self.name = name
        self.breed = breed
    def bark(self):
        return(f'{self.name} says wooofff!')  

dog :Dog = Dog("Tommy","Labrador")    
print(dog.bark())    

# 11. Class Methods

# Assignment:
# Create a class Book with a class variable total_books. Add a class method increment_book_count() to increase the count when a new book is added.

class Book:
    total_books = 0
    def __init__(self):
        Book.total_books += 1
    @classmethod
    def increament_book_count(cls):
        return f'The count of total_books are {cls.total_books}.'
        
book1:Book = Book()
book2 :Book = Book()
book3: Book = Book()
book4: Book = Book()
book5: Book = Book()
book6: Book = Book()
book7: Book = Book()
book8: Book = Book()
book9: Book = Book()
book10: Book = Book()
print(Book.increament_book_count())

#12. Static Methods

# Assignment:
# Create a class TemperatureConverter with a static method celsius_to_fahrenheit(c) that returns the Fahrenheit value.

class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32
    
print(f'The temperature in Fahrenheit is {TemperatureConverter.celsius_to_fahrenheit(25)}')  

#12. Static Methods

# Assignment:
# Create a class TemperatureConverter with a static method celsius_to_fahrenheit(c) that returns the Fahrenheit value.

class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32
    
print(f'The temperature in Fahrenheit is {TemperatureConverter.celsius_to_fahrenheit(25)}')   

#13. Composition

# Assignment:
# Create a class Engine and a class Car. Use composition by passing an Engine object to the Car class during initialization. Access a method of the Engine class via the Car class.

class Engine:
    def start_engine(self):
        return "Engine started"
    
class Car:
    def __init__(self,engine):
        self.engine = engine
        
    def start_car(self):
        return self.engine.start_engine()
    
car_engine:Engine = Engine()
my_car:Car = Car(car_engine)
print(my_car.start_car())

# 14. Aggregation

# Assignment:
# Create a class Department and a class Employee. Use aggregation by having a Department object store a reference to an Employee object that exists independently of it.       

class Department:
    def __init__(self,department_name):
        self.department_name = department_name
        
    def get_department_name(self):
        return self.department_name

class Employee:
    def __init__(self,employee_name,department):
        self.employee_name = employee_name
        self.department = department    
        
        
department:Department = Department("HR")
employee1:Employee = Employee("Tehmeena",department)
print(f"Employee {employee1.employee_name} works in {employee1.department.get_department_name()} department.")

# 15. Method Resolution Order (MRO) and Diamond Inheritance
# Assignment:
# Create four classes:
# A with a method show(),
# B and C that inherit from A and override show(),
# D that inherits from both B and C.
# Create an object of D and call show() to observe MRO.

class A:
    def show(self):
        return('Class A show() method')
        
class B(A):
    def show(self):
        return('Class B show() method')

class C(A):
    def show(self):
        return('Class C show() method')
        
class D(B,C):
    def show(self):
        return('Class D show() method')
    
obj1:D = D()
print(obj1.show())

# 16. Function Decorators

# Assignment:
# Write a decorator function log_function_call that prints "Function is being called" before a function executes. Apply it to a function say_hello().

def log_function_call(func):
    def wrapper(*args, **kwargs):
        print("Function is being called")
        return func(*args, **kwargs)
    return wrapper

@log_function_call
def say_hello():
    return "Hello, World!"

print(say_hello())

#17. Class Decorators

# Assignment:
# Create a class decorator add_greeting that modifies a class to add a greet() method returning "Hello from Decorator!". Apply it to a class Person.

def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"
    cls.greet = greet
    return cls

@add_greeting
class Person:
    def __init__(self,name):
        self.name = name
    

    
person:Person = Person("Tehmeena")
print(person.name)
print(person.greet())

# 18. Property Decorators: @property, @setter, and @deleter

# Assignment:
# Create a class Product with a private attribute _price. Use @property to get the price, @price.setter to update it, and @price.deleter to delete it.  
        
class Product:
    def __init__(self,price):   
        self.__price = price
     
    @property   
    def price(self):
        return self.__price 
        
    @price.setter
    def price(self,value):
        self.__price = value
        return self.__price
    @price.deleter
    def price(self):
        del self.__price
     
        
product1 : Product = Product(1000)
print(product1.price)
product1.price = 1500
print(product1.price)
del product1.price
print('Product1 price deleted Successfully!') 

# 19. callable() and __call__()

# Assignment:
# Create a class Multiplier with an __init__() to set a factor. Define a __call__() method that multiplies an input by the factor. Test it with callable() and by calling the object like a function.

class Multiplier:
    def __init__(self,factor):
        self.factor = factor
    def __call__(self,x):
        return x * self.factor
    
factor1:Multiplier = Multiplier(5)
print(factor1(10))  
print(callable(factor1))

#20. Creating a Custom Exception

# Assignment:
# Create a custom exception InvalidAgeError. Write a function check_age(age) that raises this exception if age < 18. Handle it with try...except.

class InvalidAgeError(Exception):
                    pass
def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be 18 or older")
    else:
        return "Age is valid"
try:
    result = check_age(15)
    print(result)
except InvalidAgeError as e:
    print(f"InvalidAgeError: {e}")

try:
    result = check_age(19)
    print(result)
except InvalidAgeError as e:
    print(f"InvalidAgeError: {e}")

# 21. Make a Custom Class Iterable

# Assignment:
# Create a class Countdown that takes a start number. Implement __iter__() and __next__() to make the object iterable in a for-loop, counting down to 0.

class Countdown:
    def __init__(self,start):
        self.current = start
    def __iter__(self):
        return self
    def __next__(self):
        if self.current < 0:
            raise StopIteration
        else:
            current = self.current
            self.current -= 1
            return current
        
        
countdown :Countdown = Countdown(5)
print("Countdown:")
for number in countdown:
    print(number)
    