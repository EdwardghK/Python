import json
import os

def add_expense(expenses, description, amount, budget):
    if get_total_expenses(expenses) + amount > budget:
        print(f"Cannot add expense: {description}. This would exceed the budget.")
    else:
        expenses.append({"description": description, "amount": amount})
        print(f"Added expense: {description}, Amount: {amount}")

def get_total_expenses(expenses):
    total = 0
    for expense in expenses:
        total += expense["amount"]
    return total

def get_balance(budget, expenses):
    return budget - get_total_expenses(expenses)

def show_budget_details(budget, expenses):
    print(f"Total budget: {budget}")
    print("Expenses:")
    for expense in expenses:
        print(f"- {expense['description']}: {expense['amount']}")
    print(f"Total spent: {get_total_expenses(expenses)}")
    print(f"Remaining budget: {get_balance(budget, expenses)}")

def load_budget_data(filepath):
    if not os.path.exists(filepath):
        with open(filepath, 'w') as file:
            json.dump({"initial_budget": 0, "expenses": []}, file)
        return 0, []
    
    try:
        with open(filepath, 'r') as file:
            data = json.load(file)
            return data["initial_budget"], data["expenses"]
    except json.JSONDecodeError:
        return 0, []

def save_budget_details(filepath, initial_budget, expenses):
    data = {
        'initial_budget': initial_budget,
        'expenses': expenses
    }
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)

def main():
    print("Welcome to the Budget Tracker")
    filepath = './budget_data.json'
    initial_budget, expenses = load_budget_data(filepath)
    if initial_budget == 0:
        initial_budget = float(input("Please enter your initial budget: "))
    budget = initial_budget

    while True:
        print("\nWhat would you like to do?")
        print("1. Add expense")
        print("2. Show budget details")
        print("3. Exit")
        choice = input("Enter choice (1, 2, or 3): ")

        if choice == '1':
            description = input("Enter expense description: ")
            amount = float(input("Enter the amount: "))
            add_expense(expenses, description, amount, budget)
        elif choice == '2':
            print(" ")
            print("-----------------------------")
            show_budget_details(budget, expenses)
            print("-----------------------------")
        elif choice == '3':
            save_budget_details(filepath, initial_budget, expenses)
            print("Now exiting")
            break
        else:
            print("Invalid input, please enter a choice again.")

if __name__ == "__main__":
    main()
