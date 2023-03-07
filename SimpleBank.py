# The project is to build a program that simulates a simple banking system.
# The program should allow users to create accounts, make deposits and withdrawals,
# check their balances, and transfer funds between accounts.

# Operations that are to be allowed:
#
# create account: create a new account
# deposit: enter an amount into an account
# withdrawal: pull some amount from an account
# check balance: check all account details
# transfer: move amounts between accounts

# An account should have the following:
#
# Name
# Initial Balance
# Account Number
# Your code should handle user errors appropraitely.

# You are allowed to use any desing you want. Check the best data types that you think fit for this project.
#     Make sure to document your code well and prepare for a code review.

import Users
from Users import Users

# [Ali - ToDo : comment the next line when the import is done ]
# Ahmad = Users("Ahmad",100,50)

# [Ali - ToDo : Uncomment the below lines :D ]
Ahmad = Users("Ahmad",100,56)
Moath = Users("Moath",100,7)
Sami = Users("Sami", 0, 11)

print(Ahmad.toString())
print(Moath.toString())

Ahmad.Tranfare(Moath,50)
print(Ahmad.toString())
print(Moath.toString())

Sami.Tranfare(Moath,50)

Sami.deposit(80)
print(Sami.toString())
Sami.Tranfare(Moath,50)
print(Sami.toString())
print(Moath.toString())
Moath.withdrawal(100)
print(Moath.toString())
