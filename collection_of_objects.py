class Customer():
    def __init__(self, name):
        self.name = name


cust1 = Customer("Shanza")
cust2 = Customer("Yusra")
cust3 = Customer("Ali")

customer_list = [cust1, cust2, cust3]  # we can make a collection of objects like list, tuple, dictionary (not set because that needs immutable data types)

for i in customer_list:  # we can loop through our list of objects
    print(i.name)