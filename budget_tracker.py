print("=== Monthly Budget Tracker (PHP) ===")

# 1. Set your starting monthly budget
monthly_budget = 15000.00

# 2. Store expenses as a LIST of DICTIONARIES
expenses = [
    {"item": "Fiber Internet", "amount": 1500.00},
    {"item": "Electricity", "amount": 2200.00},
    {"item": "Groceries", "amount": 4500.00},
    {"item": "Mobile Data", "amount": 399.00}
]

# 2.5 Let the user add extra expenses interactively
while True:
    new_item = input("\nEnter an extra expense name (or type 'done' to finish): ")
    if new_item.lower() == "done":
        break
    new_amount = float(input(f"Enter amount for{new_item} PHP: "))
    expenses.append({"item": new_item, "amount": new_amount})

# 3. Loop through the list to calculate total expenses
total_spent = 0.0

print("\nExpense Breakdown:")
for expense in expenses:
    item_name = expense["item"]
    item_cost = expense["amount"]
    total_spent += item_cost
    print(f"- {item_name}: PHP {item_cost:.2f}")

# 4. Calculate and display the remaining balance
remaining_balance = monthly_budget - total_spent

print("\n--- Summary ---")
print(f"Starting Budget:   PHP {monthly_budget:.2f}")
print(f"Total Spent:       PHP {total_spent:.2f}")
print(f"Remaining Balance: PHP {remaining_balance:.2f}")