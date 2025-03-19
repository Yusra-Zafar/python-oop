######## using super() to invoke parent's method ########

class Phone:

    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def buy(self):
        print("Buy Phone")


class SmartPhone(Phone):
    
    def buy(self):
        print("Buy a SmartPhone")
        super().buy()  # invokes parent's buy()
        
phone = SmartPhone('samsung', 123)
phone.buy()



######## using super() to invoke parent's constructor ########
class Phone:
    def __init__(self, brand, price, screen_size, battery):
        print("2. inside Phone constructor")
        self.brand = brand
        self.price = price
        self.screen_size = screen_size
        self.battery =battery


class SmartPhone(Phone):
    def __init__(self, brand, price, screen_size, battery, os, ram):
        print("1. inside SmartPhone constructor before super()")

        super().__init__(brand, price, screen_size, battery)   # for common data, invoking parent's constructor because it already has it
        
        self.os = os  # for specific SmartPhone data, initializing in my own class        
        self.ram = ram
        print("3. inside SmartPhone constructor after super()")
    

phone = SmartPhone('samsumg', 1200, 12, 5000, 'android', 8)
print(phone.battery)