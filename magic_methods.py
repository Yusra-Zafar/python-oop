# creating our own datatype for fraction operations. Since python does not support fracion operations by default, we are creating a class that will take fraction(s) and help you do fraction addition, subtration, multiplication, division etc.

class Fraction():
    def __init__(self):
        self.numerator = int(input("Numerator: "))   # instance variable that is different for each object
        self.denominator = int(input("Denominator: "))


    def __str__(self):  # gets executed when you put object inside print
        return "{}/{}".format(self.numerator, self.denominator)
    

    def __add__(self, other):  # binary (takes two objects as arguments) gets triggered when two objects +
        new_numerator = (self.numerator * other.denominator) + (other.numerator * self.denominator)
        new_denominator = self.denominator * other.denominator

        return "{}/{}".format(new_numerator, new_denominator)  # print new fraction

   
    def __sub__(self, other):   # gets triggered when two objects -
        new_numerator = (self.numerator * other.denominator) - (other.numerator * self.denominator)
        new_denominator = self.denominator * other.denominator

        return "{}/{}".format(new_numerator, new_denominator)


    def __mul__(self, other):  # gets triggered when two objects *
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator

        return "{}/{}".format(new_numerator, new_denominator)


    def __truediv__(self, other):  # gets triggered when two objects /
        new_numerator = self.numerator * other.denominator
        new_denominator = other.numerator * self.denominator

        return "{}/{}".format(new_numerator, new_denominator)


x=Fraction()
y=Fraction()

user_choice = input(
    """ 
        Select 1 for addition
        Select 2 for subtraction
        Select 3 for multiplication
        Select 4 for division
    """
    )

if user_choice == "1":
    print(x+y)

elif user_choice == "2":
    print(x-y)

elif user_choice == "3":
    print(x*y)

elif user_choice == "4":
    print(x/y)

else: 
    print("invalid choice")
