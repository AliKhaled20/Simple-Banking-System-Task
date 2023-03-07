class Users:

    def __init__(self, Name, Initial_Balance, Account_Number):
        self.Name = Name
        self.Initial_Balance = Initial_Balance
        self.Account_Number = Account_Number
        print("Initialize a user with ID:",Account_Number," is done")

    def toString(U):
        return "The name is:", U.Name, " The Balance: ", U.Initial_Balance, " The account number is: ", U.Account_Number

    def Tranfare(self,Another,Valu):
        if self.Initial_Balance >= Valu:
            Another.Initial_Balance = Another.Initial_Balance + Valu
            self.Initial_Balance = self.Initial_Balance - Valu
            print("The user ",self.Name," Transfer ",Valu," To ",Another.Name ,".")
        else:
            print(self.Name," does not have this valu '",Valu,"'")

    def deposit(self,Valu):
        self.Initial_Balance = self.Initial_Balance + Valu
        print("The user ",self.Name,"depostit '", Valu,"'")

    def withdrawal(self,Valu):
        self.Initial_Balance = self.Initial_Balance - Valu
        print("The user ", self.Name, "withdrawal '", Valu,"'")