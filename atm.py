class Atm:
    def __init__(self):  # constructor: special method
        self.pin = "1234"  # data/properties
        self.balance = 0

        self.menu()  # behavior/method


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
        self.pin = input("Enter PIN: ")
        print("\n PIN created successfully!\n")
    

    def deposit(self):
        entered_pin = input("Please enter your PIN: ")

        if entered_pin == self.pin:
            deposit_amount = int(input("Enter amount to deposit: "))
            self.balance += deposit_amount
            print(f"Deposited {deposit_amount} successfully! \n Your current balance is {self.balance}.")
        else:
            print("Invalid PIN!")


    def withdraw(self):
        entered_pin = input("Enter your PIN: ")
        
        if entered_pin == self.pin:
            withdrawal_amount = int(input("Enter amount to withdraw: "))

            if withdrawal_amount <= self.balance:
                self.balance -= withdrawal_amount
                print(f"Withdrew {withdrawal_amount} successfully! \n Your current balance is {self.balance}.")
            
            else: 
                print("Insufficient balance!")

        else:
            print("Invalid PIN")


    def check_balance(self):
        entered_pin = input("Enter your PIN: ")
        
        if entered_pin == self.pin:
            print(self.balance)
        else:
            print("Invalid PIN")

obj = Atm()

