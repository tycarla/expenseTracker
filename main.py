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

def applyDiscount(price=900, percent=0.05):
    discount = price * percent
    newPrice = discount - price
    return newPrice


newPrice = applyDiscount(900, percent=0.05)

applyDiscount(abs(newPrice))
print(abs(newPrice))