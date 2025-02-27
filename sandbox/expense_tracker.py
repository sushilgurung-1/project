from expense import Expense
import calendar
import datetime

def get_user_expense():
    print(f"---------🎯Getting user Expenses-----------")

    while True:
        try:
            expense_name = input("Enter expense name: ")
            expense_amount = float(input("Enter expense amount: ")) # here we can apply exception
            break
        except ValueError:
            print("Invalid amount. Please enter a number.")

    expense_category = ["Food", "Home", "Work", "Fun", "Music"]

    while True:
        print("Select a category: ")
        for i, category_name in enumerate(expense_category):
            print(i+1,".",category_name)
        
        value_range = f"[1-{len(expense_category)}]"
        while True:
            try:
                selected_index = int(input(f"Enter a category number {value_range}: ")) - 1 # Need exception handling(str)
                if selected_index in range(len(expense_category)):
                    selected_category = expense_category[selected_index]
                    new_expense = Expense(
                        name=expense_name,category=selected_category,amount=expense_amount
                        )
                    return new_expense
                else:
                    print("Invalid category. Please try again!")
                break
            except ValueError:
                print(f"Provide a number from {value_range}. Please try again!")
       
def save_expense_to_file(expense: Expense,expense_file_path):
    print(f"-------🎯succesfull to save user Expenses {expense} to {expense_file_path}--------")
    with open(expense_file_path,'a') as f:
        f.write(f"{expense.name},{expense.amount},{expense.category}\n")


def summarize_expense(expense_file_path,budget):
    print(f"----------🎯Summarizing user Expenses-----------")
    expenses = []
    total_exp = 0

    # while True:
    while True:
        try:
            with open(expense_file_path, 'r') as f:
                lines = f.readlines() #list , read line by line
                for line in lines:
                    stripped_line = line.strip() # it's remove space, and line too.
                    expense_name, expense_amount, expense_category = stripped_line.split(",") # split word by word and store in list
                    line_expense = Expense(
                        name=expense_name,category=expense_category,amount=float(expense_amount)
                        )
                    expenses.append(line_expense)
                # print(expenses)
                
                amt_by_category = {}
                for expense in expenses:
                    key = expense.category
                    
                    if key in amt_by_category:
                        amt_by_category[key] += expense.amount
                    else:
                        amt_by_category[key] = expense.amount
                print("Expenses by category:")
                

                for keys, values in amt_by_category.items():
                    print(f"{keys}: {values:.2f}")
                    total_exp += values

            remaining_budget = budget - total_exp
            print(f"You have spent {total_exp} out of {budget}")
            print(f'Remaining balance : {remaining_budget}')

            now = datetime.datetime.now() # current time
            # print(now)
            days_in_month = calendar.monthrange(now.year, now.month)[1]
            print(days_in_month)
            print(now.day)
            print(now.year)
            remaining_days = days_in_month - now.day
            print(f"Remaining days in month: {remaining_days}")

            daily_budget = remaining_budget/remaining_days
            print(red(f"You can {daily_budget} per days for remaining the {remaining_days} days"))
            break
        except FileNotFoundError:
            print("File not found. Please check the file path and try again.")
            
def red(text):
    return f"\033[91m{text}\033[0m"

def main():
    expense_file_path = "sandbox\expenses.csv"
    budget = 30000

    # Get user input for expense.
    expense = get_user_expense()
    print()
    # Write their expense to a file.
    save_expense_to_file(expense,expense_file_path)
    print()
    # Read file and summarize expenses.

    summarize_expense(expense_file_path,budget)
    print()
    
if __name__ == "__main__":
    main()