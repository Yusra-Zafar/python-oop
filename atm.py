class Atm:
    def __init__(self):  # constructor: special method
        self.__pin = "1234"  # data/properties
        self.__balance = 0   # private data members

        self.menu()  # behavior/method
        self.get_pin()


    def get_pin(self):    # getter method to get private data member
        print (self.__pin)


    def set_pin(self, new_pin):    # setter method to set private data member according to my logic
        if type(new_pin) == str:
            self.__pin == new_pin
        else:
            print("Please enter string type")


    def menu(self):  # method
        user_input = input(
            """
            1. Enter 1 to create pin
            2. Enter 2 to deposit
            3. Enter 3 to withdraw
            4. Enter 4 to check balance
            5. Enter 5 to exit
            """)
        
        if user_input == "1":
            self.create_pin()
            
        elif user_input == "2":
            self.deposit()
            
        elif user_input == "3":
            self.withdraw()
            
        elif user_input == "4":
            self.check_balance()
            
        elif user_input == "5": 
            print("exit")

        else:
            print("Invalid entry!")


    def create_pin(self):
        self.__pin = input("Enter PIN: ")
        print("\n PIN created successfully!\n")
        self.menu()
    

    def deposit(self):
        entered_pin = input("Please enter your PIN: ")

        if entered_pin == self.__pin:
            deposit_amount = int(input("Enter amount to deposit: "))
            self.__balance += deposit_amount
            print(f"Deposited {deposit_amount} successfully! \n Your current balance is {self.__balance}.")
        else:
            print("Invalid PIN!")
        self.menu()


    def withdraw(self):
        entered_pin = input("Enter your PIN: ")
        
        if entered_pin == self.__pin:
            withdrawal_amount = int(input("Enter amount to withdraw: "))

            if withdrawal_amount <= self.__balance:
                self.__balance -= withdrawal_amount
                print(f"Withdrew {withdrawal_amount} successfully! \n Your current balance is {self.__balance}.")
            
            else: 
                print("Insufficient balance!")

        else:
            print("Invalid PIN")
        self.menu()


    def check_balance(self):
        entered_pin = input("Enter your PIN: ")
        
        if entered_pin == self.__pin:
            print(self.__balance)
        else:
            print("Invalid PIN")
        self.menu()

obj = Atm()
obj.get_pin()

