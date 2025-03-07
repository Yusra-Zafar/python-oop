# What is OOP?
- Different style of writing code, more efficient, readable, maintainable, modular. 
- Used practically
```
list = [1,2,3,4,5]
list.upper()

AttributeError: 'list' object has no attribute 'upper'

```
- Everything is an object in Python
  
# What problem does it solve?
- Helps in planning the code, writing efficient code
- Generality to specificity
- Programmer can make his own data types
# Core concepts in OOP
![Core concepts in OOP](OOP_concepts.png)

### 1. Class
- Blueprint of how an object will behave and what it will do
- If everthing in python is an object, so an object must belong to a class
```
list=[1,2,3,4]   # this object belongs to class list
print(type(list))
<class 'list'>

a = 2   # this object belongs to class int
print(type(a))
<class 'int'>
```
> **So, in Python, we can say that data type is a class and the variable is an object of that class.**

Class has 2 things: Data/Property (noun/description of object) & Method/Function (verb/what object can do)

```
class CarClass:
    model_name = "Corolla"   # data/property
    year = 2023   # data/property

    def calc_avg_speed(parameters): # method/function
        pass
```


### 2. Object
- Instance of a class
```
object = ClassName()
car1 = CarClass()   # car1 is an object of class CarClass
```

**IMPORTANT CONCEPTS:** 

a. **Function**: is any function, can be accessed by anyone  

b. **Method**: is a function that belongs to a class, can be accessed by the object of that class.

c. **Magic/special method**: Starts and ends with double underscores. An object doesn't call these methods. They get called on a given specific criteria automatically. 

    class Fraction():
        def __init__(self, numerator, denominator):
            self.numerator = numerator
            self.denominator = denominator

    fraction = Fraction(2, 3)
    print(fraction)
    
    OUTPUT:
    <__main__.Fraction object at 0x0000018160B4B200>

Python doesn't know how does a fraction look like!

Here comes magic methods:

1. **\__str__ method**

        class Fraction():
            def __init__(self, numerator, denominator):
                self.numerator = numerator
                self.denominator = denominator


            def __str__(self):  # gets executed when you put object inside print
                return "{}/{}".format(self.numerator, self.denominator)

            fraction = Fraction(2, 3)
            print(fraction)

        OUTPUT:
        2/3

2. **\__add__ method**

        def __add__(self, other):  # binary (takes two objects as arguments) gets triggered when we add two objects
            new_numerator = (self.numerator * other.denominator) + (other.numerator * self.denominator)
            new_denominator = self.denominator * other.denominator

            return "{}/{}".format(new_numerator, new_denominator)  # print new fraction


        x = Fraction(2, 3)
        y = Fraction(2, 3)
        print(x+y) 

        OUTPUT: 
        12/9

d. **Constructor**: Magic/Special method that gets called/executed when an object of that class is created. Its control is not given to the user. All the configuration related tasks that should be done automatically when the software opens, should be written inside the constructor.

e. **self**: It is the object with which you are working right now. Jis bhi object k saath aap abhi kaam kr rhe ho, wahi self he. 

    
    class Animal():
    def __init__(self):
        print(id(self))

    cat = Animal()
    print(id(cat))

    2125115978144   # id of self
    2125115978144   # id of cat

> *Only the object can access it's class's data and methods. Even one mehtod cannot access another method or data in it's own class. So, we pass self into the method to receive the object parameter. Also, we use self.method to call the method. In python, obj.class() means the obj is getting passed as the parameter in class() by default.* 
    





### 3. 