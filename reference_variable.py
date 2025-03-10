class Customer:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

def greet(customer):
    if customer.gender == "M":
        print(f"Hello {customer.name} Sir!")
    else:
        print(f"Hello {customer.name} Mam!")

    cust2 = Customer("Yusra", "F")
    return cust2


cust = Customer("mutahar", "M")
new_cust = greet(cust)  # passing our our object into function as argument, similar to any object in python. receiving the returned object from function
print(new_cust.name)   # our object will behave exactly same as any other object in Python.