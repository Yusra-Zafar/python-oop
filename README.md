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
**So, in Python, we can say that data type is a class and the variable is an object of that class.**

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

d. **Constructor**: Magic/Special method that gets called/executed when an object of that class is created. Its control is not given to the user. All the configuration related tasks that should be done automatically when the software opens, should be written inside the constructor.





### 3. 