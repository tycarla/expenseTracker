"""
Expense Entry Form: Date, Categoy, Amount, Description

Functionality:
[INPUT]
--User can add entry forms

[PROCESS]
--User interaction
--Expense calculation
--Error handling
--Data handling (csv or sql)

[OUTPUT]
--Can view the expense by category, date, amount
--Can view summary report (e.g total monthly spending)

"""
  
date = input("Enter today's date: ")
category = input("Enter the Category: ")
amount = input("Enter the amount: ")
description = input("Enter your description: ")

with open("frutis.txt", "r") as f:
    input_data = f.read()

def applyDiscount(price=900, percent=0.05):
    discount = price * percent
    newPrice = discount - price
    return newPrice


newPrice = applyDiscount(900, percent=0.05)

applyDiscount(abs(newPrice))

print(f"the date is {date}")
print(input_data)
print(abs(newPrice))