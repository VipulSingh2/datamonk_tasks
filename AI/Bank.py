class Bank_v1:
    
    bank_name = "vipul"
    rate_of_interest = "6.5%"
    branch_name = " Main Branch"
    def __init__(self,name : str, age : int, account_no : int, balance: int = 0):
        self.customer_name = name 
        self.customer_age = age
        self.account_no = account_no
        self.balance = balance
    
    # class method
    @classmethod
    def bank_det(cls):
        print("Bank Name     :", cls.bank_name)
        print("Branch Name   :", cls.branch_name)
        print("Interest Rate :", cls.rate_of_interest)
        
    # static method
    @staticmethod
    def get_int_value(msg):
        return int(input(msg))
    # def get_int_value(int:int):
    #     print(f"Given interger is {int}")
        
        
    # instance method
    def customer_det(self):
        """
        Docstring for customer_det: This function will print the details of the customer.
        
        :param self: Description
        """
        
        print("Customer Name :", self.customer_name)
        print("Customer Age  :", self.customer_age)
        print("Account No    :", self.account_no)
        print("Balance       :", self.balance)

    # instance method 
    def deposit(self):
        """
        Docstring for deposit: This function is build for the deposit of the money
        
        :param self: Description
        :param money: Description
        :type money: float
        
        """
        # money = float(input("Enter the money you want to depposit."))
        money = self.get_int_value("Enter amount to deposit")
        self.balance += money
        print("Current balance is:",self.balance)
        
    # instance method
    def withdraw(self):
        """
        Docstring for withdraw: This function is build to withdraw amount from the account 
        before entering amount make sure that the entered amount should be less than the account amount.
        
        :param self: Description
        
        """
        money = self.get_int_value("Enter amount to withdraw")
        if money <= self.balance:
            self.balance -= money
            print(f"{money} has been withdrawn and the remaining amount is {self.balance}")
        else:
            raise ValueError("Amount is Too High")
        
    
    
class Bank_v2(Bank_v1):
    branch_name = "City Branch"
    mobile_no = "1800-222-xxx"
    def __init__(self, name, age, account_no, pin : int ,balance = 0):
        super().__init__(name, age, account_no, balance)
        self.pin = pin
        
    # Method overriding
    def customer_det(self):
        super().customer_det()
        print("Customer Pin  :", self.pin)
        
    # Mehod overriding
    @classmethod
    def bank_det(cls):
        super().bank_det()
        print("Bank Mobile   :",cls.mobile_no)
    
    # method overriding with PIN validation
    def withdraw(self):
        entered_pin = Bank_v1.get_int_value("Enter Pin:")
        if entered_pin == self.pin:
            super().withdraw()
        else:
            raise ValueError("Incorrect PIN")
        
        
# user = Bank_v1("vipul",22,123456,1000)
# # user.deposit(500)
# # user.customer_det()
# # user.withdraw()
# user.bank_det()
# user.get_int_value(12)


# user = Bank_v2("Vipul", 22, 123456, 1234, 1000)

# user.customer_det()
# user.bank_det()
# user.withdraw()


# ---------------- TEST CODE ----------------

# user = Bank_v2(
#     name="Vipul",
#     age=22,
#     account_no=123456,
#     pin=1234,
#     balance=30000
# )

# # customer details
# user.customer_det()

# print("\n--- Bank Details ---")
# user.bank_det()

# print("\n--- Withdraw Test ---")
# user.withdraw()

# print("\n--- Deposit Test ---")
# user.deposit()
