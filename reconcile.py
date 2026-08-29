import pandas as pd

# Load dataset
df = pd.read_csv("synthetic_transactions.csv")

matched = 0
pending = 0
mismatch = 0
refunds = 0

exceptions = []

print("========== TRANSACTION RECONCILIATION ==========\n")


for index, row in df.iterrows():

    transaction_id = row["transaction_id"]
    amount = row["amount"]
    settlement_amount = row["settlement_amount"]
    transaction_status = row["transaction_status"]
    settlement_status = row["settlement_status"]

    # Failed transaction
    if transaction_status == "FAILED":

        if settlement_amount != 0:

            print(transaction_id, "EXCEPTION: Failed transaction has settlement")

            mismatch += 1

            exceptions.append({
                "transaction_id": transaction_id,
                "order_id": row["order_id"],
                "amount": amount,
                "settlement_amount": settlement_amount,
                "issue": "Failed transaction has settlement"
            })

        else:

            print(transaction_id, "MATCHED")
            matched += 1


    # Successful transaction
    elif transaction_status == "SUCCESS":

        if settlement_status == "SETTLED":

            if amount == settlement_amount:

                print(transaction_id, "MATCHED")
                matched += 1

            else:

                print(transaction_id, "EXCEPTION: Amount mismatch")

                mismatch += 1

                exceptions.append({
                    "transaction_id": transaction_id,
                    "order_id": row["order_id"],
                    "amount": amount,
                    "settlement_amount": settlement_amount,
                    "issue": "Amount mismatch"
                })


        elif settlement_status == "PENDING":

            print(transaction_id, "EXCEPTION: Settlement pending")

            pending += 1

            exceptions.append({
                "transaction_id": transaction_id,
                "order_id": row["order_id"],
                "amount": amount,
                "settlement_amount": settlement_amount,
                "issue": "Settlement pending"
            })


    # Refunded transaction
    elif transaction_status == "REFUNDED":

        print(transaction_id, "REFUND - REVIEW")

        refunds += 1

        exceptions.append({
            "transaction_id": transaction_id,
            "order_id": row["order_id"],
            "amount": amount,
            "settlement_amount": settlement_amount,
            "issue": "Refund requires review"
        })


# Create exception DataFrame
exception_df = pd.DataFrame(exceptions)

# Save exception report
exception_df.to_csv("exceptions.csv", index=False)


# Calculate totals
total = len(df)

total_exceptions = pending + mismatch

match_rate = (matched / total) * 100
exception_rate = (total_exceptions / total) * 100


# Summary
print("\n==============================================")
print("           RECONCILIATION SUMMARY")
print("==============================================")

print("Total Transactions :", total)
print("Matched            :", matched)
print("Exceptions         :", total_exceptions)
print("Refunds            :", refunds)
print("Pending            :", pending)
print("Amount Mismatches  :", mismatch)

print("----------------------------------------------")

print("Match Rate         :", round(match_rate, 2), "%")
print("Exception Rate     :", round(exception_rate, 2), "%")

print("----------------------------------------------")

print("Exception report saved as: exceptions.csv")

print("==============================================")