# static variables and methods

class Atm:
    __counter = 0  # static variable whose value will remain same for all objects

    def __init__(self):  # constructor: special method
        Atm.__counter += 1 
        self.s_no = Atm.__counter 

    
    @staticmethod
    def get_counter():   # no need for self because it does not deal with any instance variable
        return Atm.__counter


    @staticmethod
    def set_counter(new_counter):
        if type(new_counter) == int:
            Atm.__counter = new_counter
        else:
            print("Invalid type!")

hbl = Atm()
ubl = Atm()
meezan = Atm()

print(f"hbl: {hbl.s_no}")  # every object has the right serial number through static variable
print(f"ubl: {ubl.s_no}")
print(f"meezan: {meezan.s_no}")

counter = Atm.get_counter()
print(f"counter: {counter}")

Atm.set_counter(5)

counter = Atm.get_counter()
print(f"counter: {counter}")