def get_valid_amount(prompt):
    """Safely ask the user for a positive number using try/except."""
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Amount cannot be negative. Please try again.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a numeric amount (e.g., 500 or 1250.50).")

def add_extra_expenses(expenses):
    """Loop to let the user add new expenses safely."""
    while True:
        new_item = input("\nEnter an extra expense name (or type 'done' to finish): ").strip()
        if new_item.lower() == "done":
            break
        if not new_item:
            print("Expense name cannot be empty.")
            continue

        new_amount = get_valid_amount(f"Enter amount for {new_item} (PHP): ")
        expenses.append({"item": new_item, "amount": new_amount})

def display_summary(monthly_budget, expenses):
    """Calculate totals and print a clean budget breakdown."""
    print("\n--- Expense Breakdown ---")
    total_spent = 0.0
    for expense in expenses:
        print(f"- {expense['item']}: PHP {expense['amount']:,.2f}")
        total_spent += expense["amount"]

    remaining = monthly_budget - total_spent
    print("\n--- Summary ---")
    print(f"Monthly Budget:     PHP {monthly_budget:,.2f}")
    print(f"Total Spent:        PHP {total_spent:,.2f}")
    print(f"Remaining Balance:  PHP {remaining:,.2f}")

    if remaining < 0:
        print("Warning: You are over budget!")

def main():
    print("=== Monthly Budget Tracker (PHP) ===")
    monthly_budget = get_valid_amount("Enter your starting monthly budget (PHP): ")

    expenses = [
        {"item": "Fiber Internet", "amount": 1500.00},
        {"item": "Electricity", "amount": 2200.00},
        {"item": "Groceries", "amount": 4500.00},
        {"item": "Mobile Data", "amount": 399.00},
    ]

    add_extra_expenses(expenses)
    display_summary(monthly_budget, expenses)

if __name__ == "__main__":
    main()