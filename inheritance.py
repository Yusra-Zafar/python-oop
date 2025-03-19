# class User:
#     def login(self):
#         print('login')

#     def register(self):
#         print('register')


# class Student(User):  # student is inheriting from user
#     def enroll(self):
#         print("enroll")
    
#     def watch(self):
#         print("watch")

# student = Student()
# student.enroll()
# student.register()

############# example1 ############
# class User:
#     def __init__(self, __name, age):
#         self.__name = __name
#         self.age = age

#     def login(self):
#         print('login')

# class Student(User):  # if child has no constructor, parent's will be called
#     pass

# stud = Student('abc', 23)
# print(stud.age)

############# example2 ############
class User:
    def __init__(self, name, age):
        self.__name = name
        self.age = age

    def login(self):
        print('login')

class Student(User):  
    pass

stud1 = Student('xyz', 24)
print(stud1.__name)   # can't access private data member




