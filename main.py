import csv
from utils.validator import validate_date, validate_amount, normalize_category

from analytics.summary import (
    total_expense,
    category_summary,
    monthly_summary,
    spending_insight,
    budget_alerts
)



DATA_PATH = "data/expenses.csv"

def show_menu():
    print("\n" + "=" * 40)
    print("💰 Personal Finance Intelligence System")
    print("=" * 40)
    print("1️⃣  Add Expense")
    print("2️⃣  View Total Expense")
    print("3️⃣  Category-wise Summary")
    print("4️⃣  Monthly Summary")
    print("5️⃣  Spending Insight")
    print("6️⃣  Budget Alerts")
    print("0️⃣  Exit")
    print("=" * 40)


def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    if not validate_date(date):
        print("❌ Invalid date format. Use YYYY-MM-DD.")
        return

    amount = input("Enter amount: ")
    if not validate_amount(amount):
        print("❌ Amount must be a positive number.")
        return

    category = input("Enter category: ")
    category = normalize_category(category)

    note = input("Enter note: ")

    with open(DATA_PATH, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, float(amount), category, note])

    print("✅ Expense added successfully!")
1


def view_total_expense():
    total = total_expense()
    print(f"Total expense: ₹{total}")


def view_category_summary():
    summary = category_summary()
    print("\nCategory-wise Expense:")
    print(summary)

def view_monthly_summary():
    summary = monthly_summary()
    print("\nMonthly Expense Summary:")
    print(summary)


def view_spending_insight():
    insight = spending_insight()
    print("\nSpending Insight:")
    print(insight)

def view_budget_alerts():
    alerts = budget_alerts()
    print("\nBudget Alerts:")
    for alert in alerts:
        print(alert)



while True:
    show_menu()
    choice = input("Choose an option: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_total_expense()

    elif choice == "3":
        view_category_summary()

    elif choice == "4":
        view_monthly_summary()

    elif choice == "5":
        view_spending_insight()

    elif choice == "6":
        view_budget_alerts()

    elif choice == "0":
        print("👋 Exiting. Take control of your finances!")
        break

    else:
        print("❌ Invalid option. Please choose again.")

    input("\nPress Enter to continue...")
