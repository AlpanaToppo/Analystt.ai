import json
from datetime import datetime

def load_expenses():
    try:
        with open("expenses.json", "r") as file:
            expenses = json.load(file)
    except FileNotFoundError:
        expenses = []
    return expenses

def save_expenses(expenses):
    with open("expenses.json", "w") as file:
        json.dump(expenses, file)

def add_expense(category, amount):
    expenses = load_expenses()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    expense = {"timestamp": timestamp, "category": category, "amount": amount}
    expenses.append(expense)
    save_expenses(expenses)
    print("Expense added successfully.")

def view_expenses():
    expenses = load_expenses()
    if not expenses:
        print("\nNo expenses recorded.")
    else:
        print("Expenses:")
        for expense in expenses:
            print(f"{expense['timestamp']} - Category: {expense['category']}, Amount: Rs.{expense['amount']}")

if __name__ == "__main__":
    while True:
        print("\n1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            category = input("Enter expense category: ")
            amount = float(input("Enter expense amount: "))
            add_expense(category, amount)
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            print("Exiting the expense tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")
