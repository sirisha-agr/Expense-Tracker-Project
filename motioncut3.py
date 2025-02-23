from datetime import datetime

EXPENSE_FILE = "expenses.txt"

def add_expense():
    amount = input("Enter amount spent: ")
    category = input("Enter category (Food, Transport, Entertainment, etc.): ").capitalize()
    description = input("Enter a short description: ")
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(EXPENSE_FILE, "a") as file:
        file.write(f"{date},{amount},{category},{description}\n")

    print("Expense added successfully!")


def view_expenses():
    try:
        with open(EXPENSE_FILE, "r") as file:
            expenses = file.readlines()

        if not expenses:
            print("No expenses recorded.")
            return
        
        print("\n--- Expense List ---")
        for idx, exp in enumerate(expenses, start=1):
            date, amount, category, description = exp.strip().split(",")
            print(f"{idx}. {date} | ₹{amount} | {category} | {description}")

    except FileNotFoundError:
        print("No expenses recorded yet.")

def expense_summary():
    summary = {}

    try:
        with open(EXPENSE_FILE, "r") as file:
            expenses = file.readlines()

        if not expenses:
            print("No expenses recorded.")
            return

        for exp in expenses:
            _, amount, category, _ = exp.strip().split(",")
            summary[category] = summary.get(category, 0) + float(amount)

        print("\n--- Expense Summary ---")
        for category, total in summary.items():
            print(f"{category}: ₹{total:.2f}")

    except FileNotFoundError:
        print("No expenses recorded yet.")


def main():
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Summary")
        print("4. Exit")
        
        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            expense_summary()
        elif choice == "4":
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
