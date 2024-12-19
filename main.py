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

THIS IS THE UI ----
Welcome to expense tracker!

(# User enters expenses)
Enter expense name:
Enter expense amount:
Select a category:
1. Food
2. Home
3. Work
4. Fun
5. Misc
Enter a category number:
You've added coffee ($) to your expenses.
You have 7 expenses totalling $739.00

(#Summarise expense tracker)
Expenses by category
Food: $
Home: $
Fun: $

Budget (#Show remaining budget)
You have $ left to spend this month.
That's roughly $ per day.

"""
#User entry expense

expense_name = input("Enter your expense name: ")
expense_amount = input("Enter expense amount: ")


#If statement for category
def expense_category():
    
    category = ["1. Food", "2. Home", "3. Work", "4. Fun", "5. Misc"]
    print(category)
    expense_category = input("Enter a category number: ")
    print(expense_category)
    
    if expense_category == 1:
        Food
    
    elif expense_category == 2:
        Home
    
    elif expense_category == 3:
        Work
    
    elif expense_category == 4:
        Fun
    
    elif expense_category == 5:
        Misc
    
    else:
        print("Select number category from 1 to 5 only!")
        
    
#Classes
class Food:
    
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount
    
    def summarize(self, totalAmount):
        totalAmount.amount += totalAmount

class Home:
    
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount
    
    def summarize(self, totalAmount):
        totalAmount.amount += totalAmount
        
class Work:
    
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount
    
    def summarize(self, totalAmount):
        totalAmount.amount += totalAmount
        
class Fun:
    
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount
    
    def summarize(self, totalAmount):
        totalAmount.amount += totalAmount
        
class Misc:
    
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount
    
    def summarize(self, totalAmount):
        totalAmount.amount += totalAmount
        



#Save expense to CSV file

with open("Food.txt", "w") as f:
    f.write()

with open("Home.txt", "w") as f:
    f.write()

with open("Work.txt", "w") as f:
    f.write()
    
with open("Fun.txt", "w") as f:
    f.write()
    
with open("Misc.txt", "w") as f:
    f.write()

#Summaries expense totals

#Show remaining budget

class Monster:
    
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack
    
    def fight(self, target):
        target.hp -= self.attack
        print(f"{self.name} attacked {target.name} for {self.attack} damage!")
        print(f"{target.name} has {target.hp} HP left")
        

#print?
Morgana = Monster("Morgana", 100, 25)
Lux = Monster("Lux", 50, 35)
Morgana.fight(Lux)
Lux.fight(Morgana)