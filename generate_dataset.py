import pandas as pd
import random
from datetime import datetime, timedelta

random.seed(42)

transactions = []

start_date = datetime(2026, 8, 1)

for i in range(1, 121):

    transaction_id = f"TXN{i:05d}"
    order_id = f"ORD{i:05d}"
    customer_id = f"CUST{random.randint(1001, 1100)}"

    amount = random.choice([
        199, 299, 499, 799, 999,
        1499, 1999, 2499, 2999, 4999
    ])

    transaction_date = start_date + timedelta(
        days=random.randint(0, 27)
    )

    payment_method = random.choice([
        "UPI",
        "CARD",
        "NETBANKING",
        "WALLET"
    ])

    status = random.choice([
        "SUCCESS",
        "SUCCESS",
        "SUCCESS",
        "FAILED",
        "REFUNDED"
    ])

    if status == "FAILED":

        settlement_status = "NOT_SETTLED"
        settlement_amount = 0

    elif status == "REFUNDED":

        settlement_status = "SETTLED"
        settlement_amount = amount

    else:

        settlement_status = random.choice([
            "SETTLED",
            "SETTLED",
            "PENDING"
        ])

        if settlement_status == "SETTLED":
            settlement_amount = amount
        else:
            settlement_amount = 0

    transactions.append({
        "transaction_id": transaction_id,
        "order_id": order_id,
        "transaction_date": transaction_date.strftime("%Y-%m-%d"),
        "customer_id": customer_id,
        "amount": amount,
        "currency": "INR",
        "payment_method": payment_method,
        "transaction_status": status,
        "settlement_status": settlement_status,
        "settlement_amount": settlement_amount
    })


df = pd.DataFrame(transactions)


# Create intentional problems for our AI to detect

# Amount mismatch
df.loc[7, "settlement_amount"] += 100

# Another amount mismatch
df.loc[18, "settlement_amount"] += 250

# Pending settlement
df.loc[34, "settlement_status"] = "PENDING"
df.loc[34, "settlement_amount"] = 0


# Save the dataset
df.to_csv("synthetic_transactions.csv", index=False)

print("Dataset created successfully!")
print("Total transactions:", len(df))
print("File: synthetic_transactions.csv")