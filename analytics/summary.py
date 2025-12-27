from utils.budgets import BUDGETS

import pandas as pd

DATA_PATH = "data/expenses.csv"


def load_data():
    df = pd.read_csv(DATA_PATH)
    df["amount"] = pd.to_numeric(df["amount"])
    df["date"] = pd.to_datetime(df["date"])
    return df


def total_expense():
    df = load_data()
    return df["amount"].sum()


def category_summary():
    df = load_data()
    return df.groupby("category")["amount"].sum()


def monthly_summary():
    df = load_data()
    monthly = df.groupby(df["date"].dt.to_period("M"))["amount"].sum()
    return monthly


def spending_insight():
    monthly = monthly_summary()

    if len(monthly) < 2:
        return "Not enough data for monthly comparison."

    last = monthly.iloc[-1]
    prev = monthly.iloc[-2]

    change = ((last - prev) / prev) * 100

    if change > 0:
        return f"📈 Spending increased by {change:.1f}% compared to last month."
    else:
        return f"📉 Spending decreased by {abs(change):.1f}% compared to last month."
    

def budget_alerts():
    df = load_data()

    # current month only
    current_month = df["date"].dt.to_period("M").iloc[-1]
    month_df = df[df["date"].dt.to_period("M") == current_month]

    alerts = []

    for category, limit in BUDGETS.items():
        spent = month_df[month_df["category"].str.lower() == category]["amount"].sum()

        if spent == 0:
            continue

        if spent > limit:
            alerts.append(
                f"⚠️ {category.capitalize()} budget exceeded by ₹{spent - limit}"
            )
        else:
            alerts.append(
                f"✅ {category.capitalize()} is within budget (₹{limit - spent} left)"
            )

    if not alerts:
        return ["No budget data available."]

    return alerts

