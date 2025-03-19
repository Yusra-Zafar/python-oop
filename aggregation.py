class Customer:
    def __init__(self, name, gender, address):
        self.name = name
        self.gender = gender
        self.address = address

    def edit_profile(self, new_name, new_city, new_pincode, new_state):
        self.name = new_name
        self.address.change_address(new_city, new_pincode, new_state)  # calls address class's method to change address. This is aggregation


        
class Address:
    def __init__(self, city, pincode, state):
        self.city =  city
        self.pincode = pincode
        self.state = state

    def change_address(self, new_city, new_pincode, new_state):
        self.city =  new_city
        self.pincode = new_pincode
        self.state = new_state



address = Address("pwr", 25000, "kpk")
customer = Customer("Yusra", "F", address)  # we can pass an object as an argument in another object. it will behave the same as an ordianry object

# after editing
customer.edit_profile("shanza", "isl", 23000, "capital")


# print(customer.address)  # prints address object
print(customer.address.state)  # prints address attribute state