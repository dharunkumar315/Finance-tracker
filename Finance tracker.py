import csv
from datetime import datetime

# File to store transactions
FILE_NAME = "finance_data.csv"

# Load existing data or initialize a new file
def load_transactions():
    transactions = []
    try:
        with open(FILE_NAME, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                transactions.append(row)
    except FileNotFoundError:
        with open(FILE_NAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Type", "Category", "Amount", "Note"])
    return transactions

# Save a new transaction
def save_transaction(transaction):
    with open(FILE_NAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(transaction)

# Add a transaction
def add_transaction():
    t_type = input("Enter type (income/expense): ").lower()
    category = input("Enter category (e.g. food, salary): ")
    amount = float(input("Enter amount: "))
    note = input("Enter a note (optional): ")
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    transaction = [date, t_type, category, amount, note]
    save_transaction(transaction)
    print("Transaction added successfully!")

# Show all transactions
def view_transactions(transactions):
    if not transactions:
        print("No transactions found.")
        return
    print(f"\n{'Date':<20} {'Type':<10} {'Category':<15} {'Amount':<10} {'Note'}")
    for t in transactions:
        print(f"{t['Date']:<20} {t['Type']:<10} {t['Category']:<15} {t['Amount']:<10} {t['Note']}")

# Show balance summary
def show_summary(transactions):
    income = sum(float(t["Amount"]) for t in transactions if t["Type"] == "income")
    expense = sum(float(t["Amount"]) for t in transactions if t["Type"] == "expense")
    print(f"\nTotal Income: ₹{income:.2f}")
    print(f"Total Expense: ₹{expense:.2f}")
    print(f"Net Balance: ₹{income - expense:.2f}")

# Main menu
def main():
    while True:
        print("\n=== Finance Tracker ===")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Show Summary")
        print("4. Exit")
        choice = input("Choose an option: ")

        transactions = load_transactions()

        if choice == '1':
            add_transaction()
        elif choice == '2':
            view_transactions(transactions)
        elif choice == '3':
            show_summary(transactions)
        elif choice == '4':
            print("Exiting Finance Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
