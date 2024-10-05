import json
from datetime import datetime

EXPENSE_FILE = 'expenses.txt'


def load_expenses():
    try:
        with open(EXPENSE_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_expenses(expenses):
    with open(EXPENSE_FILE, 'w') as file:
        json.dump(expenses, file)


def add_expense(expenses):
    date = input("Enter Date (DD/MM/YYYY): ")
    category = input("Enter Category (Food/Transport/Entertainment): ")
    description = input("Enter Description: ")
    amount = float(input("Enter Amount: "))

    expense = {
        'date': date,
        'category': category,
        'description': description,
        'amount': amount
    }

    expenses.append(expense)
    print("Expense added successfully!")


def view_summary_by_date(expenses):
    date = input("Enter Date (DD/MM/YYYY): ")
    total = 0
    print(f"Expenses on {date}:")
    for expense in expenses:
        if expense['date'] == date:
            print(f"{expense['category']} - {expense['description']} - ${expense['amount']:.2f}")
            total += expense['amount']
    print(f"Total Expenses on {date}: ${total:.2f}")


def view_summary_by_category(expenses):
    category = input("Enter Category (Food/Transport/Entertainment): ")
    total = 0
    print(f"Total Expenses for {category}:")
    for expense in expenses:
        if expense['category'].lower() == category.lower():
            print(f"{expense['date']} - {expense['description']} - ${expense['amount']:.2f}")
            total += expense['amount']
    print(f"Total {category} Expenses: ${total:.2f}")


def main():
    expenses = load_expenses()

    while True:
        print("\nWelcome to the Expense Tracker")
        print("1. Add a New Expense")
        print("2. View Summary by Date")
        print("3. View Summary by Category")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            view_summary_by_date(expenses)
        elif choice == '3':
            view_summary_by_category(expenses)
        elif choice == '4':
            save_expenses(expenses)
            print("Your expenses have been saved. Goodbye!")
            break
        else:
            print("Invalid option, please try again.")


if __name__ == '__main__':
    main()
