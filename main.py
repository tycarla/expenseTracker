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
name = input("Enter your name: ")
age = input("Enter your age: ")

with open("user_info.txt", "w") as f:
    f.write(name)
    f.write(age)