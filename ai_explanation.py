import pandas as pd

# Load exception report
df = pd.read_csv("exceptions.csv")

ai_results = []

for index, row in df.iterrows():

    transaction_id = row["transaction_id"]
    amount = row["amount"]
    settlement_amount = row["settlement_amount"]
    issue = row["issue"]

    priority = "MEDIUM"
    explanation = ""
    action = ""

    # Amount mismatch
    if issue == "Amount mismatch":

        difference = settlement_amount - amount

        if difference > 0:
            explanation = (
                "Settlement amount is higher than the transaction amount."
            )
        else:
            explanation = (
                "Settlement amount is lower than the transaction amount."
            )

        action = "Verify the settlement record."
        priority = "HIGH"


    # Settlement pending
    elif issue == "Settlement pending":

        explanation = (
            "The payment was successful but the settlement "
            "has not completed yet."
        )

        action = "Monitor the settlement and check again later."
        priority = "MEDIUM"


    # Refund
    elif issue == "Refund requires review":

        explanation = (
            "The transaction was refunded and should be "
            "checked against the refund record."
        )

        action = "Verify the refund amount and refund status."
        priority = "MEDIUM"


    # Failed transaction with settlement
    elif issue == "Failed transaction has settlement":

        explanation = (
            "The transaction failed but a settlement amount "
            "was recorded."
        )

        action = "Investigate the settlement immediately."
        priority = "HIGH"


    ai_results.append({
        "transaction_id": transaction_id,
        "issue": issue,
        "amount": amount,
        "settlement_amount": settlement_amount,
        "priority": priority,
        "ai_explanation": explanation,
        "recommended_action": action
    })


# Create AI report
ai_report = pd.DataFrame(ai_results)

# Save report
ai_report.to_csv("ai_report.csv", index=False)

print("==========================================")
print("       AI ANALYSIS COMPLETED")
print("==========================================")

print("Total records analyzed:", len(ai_report))

print()
print("AI report saved successfully!")
print("File: ai_report.csv")