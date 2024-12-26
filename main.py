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
from expense import Expense

def main():
    print("Running Expense Tracker!")
    expense_file_path = "expense.csv"

    #User entry expense
    expense = get_user_expense()
    print(expense)

    #Write their expense to a file
    save_expense_to_file(expense, expense_file_path)

    #Summaries expense totals
    summarize_expense(expense_file_path)

    #Show remaining budget

def get_user_expense():
    print("Getting User Expense")
    expense_name = input("Enter expense name: ")
    expense_amount = float(input("Enter expense amount: "))
    print(f"You've entered {expense_name}, {expense_amount} pesos")
    
    expense_category = [
        "Food", 
        "Home", 
        "Work", 
        "Fun", 
        "Misc",
        ]
    
    while True:
        print("Select a category: ")
        for i, category_name in enumerate(expense_category):
            print(f"    {i + 1}. {category_name}")
            
        value_range = f"[1 - {len(expense_category)}]"
        
        selected_index = int(input("Enter a category number {value_range}: ")) - 1
        
        if selected_index in range(len(expense_category)):
            selected_category = expense_category[selected_index]
            new_expense = Expense(
                name=expense_name, category=selected_category, amount=expense_amount
                )
            return
        else:
            print("invalid category. Please try again!")
        
        break
    
    
def save_expense_to_file(expense: Expense, expense_file_path):
    print("Saving User Expense: {expense} to {expense_file_path}")
    with open(expense_file_path, "a") as f:
        f.write(f"{expense.name}, {expense.amount}, {expense.category}\n")

def summarize_expense():
    print("Summarizing User Expense")
    

if __name__ == "__main__":
    main()