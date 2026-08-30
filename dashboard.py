import streamlit as st
import pandas as pd

# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="AI Finance Controller",
    page_icon="💳",
    layout="wide"
)

# ==========================================
# SIDEBAR
# ==========================================

with st.sidebar:

    st.title("💳 Finance AI")

    st.markdown(
        "### AI Finance Controller"
    )

    st.caption(
        "Transaction reconciliation & exception intelligence"
    )

    st.divider()

    st.markdown("### 📊 Dashboard")

    st.write("Transaction Analytics")
    st.write("Exception Monitoring")
    st.write("AI Investigation")

    st.divider()

    st.markdown("### ⚙️ System")

    st.write("Reconciliation Engine")
    st.write("AI Analysis Engine")



# ==========================================
# LOAD DATA
# ==========================================

transactions = pd.read_csv("synthetic_transactions.csv")
ai_report = pd.read_csv("ai_report.csv")
# ==========================================
# SIDEBAR FILTERS
# ==========================================

st.sidebar.title("🔎 Investigation Panel")

st.sidebar.write(
    "Use these filters to investigate transactions."
)

# Transaction status filter
status_options = ["All"] + sorted(
    transactions["transaction_status"].unique().tolist()
)

selected_status = st.sidebar.selectbox(
    "Transaction Status",
    status_options
)

# Settlement filter
settlement_options = ["All"] + sorted(
    transactions["settlement_status"].unique().tolist()
)

selected_settlement = st.sidebar.selectbox(
    "Settlement Status",
    settlement_options
)

# Apply transaction filters
filtered_data = transactions.copy()

if selected_status != "All":

    filtered_data = filtered_data[
        filtered_data["transaction_status"]
        == selected_status
    ]

if selected_settlement != "All":

    filtered_data = filtered_data[
        filtered_data["settlement_status"]
        == selected_settlement
    ]

st.sidebar.divider()

st.sidebar.metric(
    "Transactions Found",
    len(filtered_data)
)


# ==========================================
# TITLE
# ==========================================

st.title("💳 AI Finance Controller")

st.markdown(
    "### Transaction Reconciliation & Exception Intelligence"
)

st.caption(
    "Monitor payments, settlements, refunds and financial exceptions in one place."
)

st.divider()


# ==========================================
# CALCULATE STATISTICS
# ==========================================

total_transactions = len(transactions)

matched = 0
pending = 0
mismatch = 0
refunds = 0

for _, row in transactions.iterrows():

    status = row["transaction_status"]
    settlement_status = row["settlement_status"]

    if status == "REFUNDED":

        refunds += 1

    elif status == "SUCCESS" and settlement_status == "PENDING":

        pending += 1

    elif (
        status == "SUCCESS"
        and settlement_status == "SETTLED"
        and row["amount"] == row["settlement_amount"]
    ):

        matched += 1

    elif (
        status == "FAILED"
        and row["settlement_amount"] == 0
    ):

        matched += 1

    else:

        mismatch += 1


exceptions = pending + mismatch

match_rate = (
    matched / total_transactions
) * 100


# ==========================================
# MAIN METRICS
# ==========================================

st.subheader("📊 Financial Overview")
st.caption(
    "Real-time overview of transaction reconciliation performance."
)
col1, col2, col3, col4 = st.columns(4)

with col1:

    st.metric(
        "Total Transactions",
        total_transactions
    )

with col2:

    st.metric(
        "Matched",
        matched
    )

with col3:

    st.metric(
        "Exceptions",
        exceptions
    )

with col4:

    st.metric(
        "Match Rate",
        f"{match_rate:.1f}%"
    )


# ==========================================
# SECOND METRIC ROW
# ==========================================

col5, col6, col7 = st.columns(3)

with col5:

    st.metric(
        "⏳ Pending Settlements",
        pending
    )

with col6:

    st.metric(
        "⚠️ Amount Mismatches",
        mismatch
    )

with col7:

    st.metric(
        "🔄 Refunds",
        refunds
    )
# ==========================================
# TRANSACTION STATUS CHART
# ==========================================

st.divider()

# ==========================================
# ANALYTICS OVERVIEW
# ==========================================

st.divider()

st.subheader("📈 Analytics Overview")

chart_col1, chart_col2 = st.columns(2)

# ------------------------------------------
# TRANSACTION STATUS
# ------------------------------------------

with chart_col1:

    st.markdown("#### 📊 Transaction Status")

    status_counts = transactions[
        "transaction_status"
    ].value_counts()

    st.bar_chart(status_counts)

# ------------------------------------------
# EXCEPTION TYPES
# ------------------------------------------

with chart_col2:

    st.markdown("#### ⚠️ Exception Types")

    issue_counts = ai_report[
        "issue"
    ].value_counts()

    st.bar_chart(issue_counts)

st.divider()

# ==========================================
# PRIORITY OVERVIEW
# ==========================================

st.subheader("🚨 Exception Priority")

priority_counts = ai_report[
    "priority"
].value_counts()

st.bar_chart(priority_counts)
# ==========================================
# FINANCIAL AMOUNT SUMMARY
# ==========================================

st.divider()

st.subheader("💰 Financial Amount Overview")

st.caption(
    "Overview of transaction, settlement, pending and reconciliation values."
)

total_transaction_amount = transactions["amount"].sum()

total_settlement_amount = transactions["settlement_amount"].sum()

pending_amount = transactions[
    transactions["settlement_status"] == "PENDING"
]["amount"].sum()

amount_difference = (
    total_transaction_amount
    - total_settlement_amount
)


col8, col9, col10, col11 = st.columns(4)

with col8:

    st.metric(
        "💰 Transaction Value",
        f"₹{total_transaction_amount:,.2f}"
    )

with col9:

    st.metric(
        "🏦 Settlement Value",
        f"₹{total_settlement_amount:,.2f}"
    )

with col10:

    st.metric(
        "⏳ Pending Value",
        f"₹{pending_amount:,.2f}"
    )

with col11:

    st.metric(
        "⚠️ Amount Difference",
        f"₹{amount_difference:,.2f}"
    )
st.caption(
    "Negative values indicate settlement value is higher than transaction value."
)

# ==========================================
# TRANSACTION SEARCH
# ==========================================

st.divider()

st.subheader("🔍 Transaction Search")

st.caption(
    "Search and investigate transactions using their transaction ID."
)

search = st.text_input(
    "Search Transaction ID",
    placeholder="Example: TXN00019",
    key="transaction_search"
)

# Start with sidebar-filtered transactions
search_results = df.copy()

# Apply transaction ID search
if search.strip():

    search_results = search_results[
        search_results["transaction_id"]
        .astype(str)
        .str.contains(
            search.strip(),
            case=False,
            na=False
        )
    ]

st.write(
    f"Showing **{len(search_results)}** transaction(s)"
)

if len(search_results) > 0:

    st.dataframe(
        search_results,
        use_container_width=True,
        hide_index=True
    )

else:

    st.warning(
        "No transactions found. Try another Transaction ID."
    )


# ==========================================
# AI EXCEPTION ANALYSIS
# ==========================================

st.divider()

st.subheader("🤖 AI Exception Analysis")

st.caption(
    "Filter detected exceptions by issue type and priority."
)

# ------------------------------------------
# FILTER COLUMNS
# ------------------------------------------

filter_col1, filter_col2 = st.columns(2)

with filter_col1:

    issue_options = [
        "All"
    ] + sorted(
        ai_report["issue"]
        .dropna()
        .unique()
        .tolist()
    )

    selected_issue = st.selectbox(
        "⚠️ Filter by Issue",
        issue_options,
        key="ai_issue_filter"
    )

with filter_col2:

    priority_options = [
        "All"
    ] + sorted(
        ai_report["priority"]
        .dropna()
        .unique()
        .tolist()
    )

    selected_priority = st.selectbox(
        "🚨 Filter by Priority",
        priority_options,
        key="ai_priority_filter"
    )


# ------------------------------------------
# APPLY AI FILTERS
# ------------------------------------------

filtered_ai = ai_report.copy()

if selected_issue != "All":

    filtered_ai = filtered_ai[
        filtered_ai["issue"]
        == selected_issue
    ]

if selected_priority != "All":

    filtered_ai = filtered_ai[
        filtered_ai["priority"]
        == selected_priority
    ]


st.write(
    f"Showing **{len(filtered_ai)}** exception(s)"
)


# ------------------------------------------
# DISPLAY AI RESULTS
# ------------------------------------------

if len(filtered_ai) > 0:

    st.dataframe(
        filtered_ai,
        use_container_width=True,
        hide_index=True
    )

else:

    st.success(
        "No exceptions match the selected filters."
    )


# ==========================================
# AI TRANSACTION INVESTIGATION
# ==========================================

st.divider()

st.subheader("🧠 AI Transaction Investigation")

if len(ai_report) > 0:

    selected_transaction = st.selectbox(
        "🔎 Select Transaction to Investigate",
        ai_report["transaction_id"].tolist(),
        key="ai_transaction_selector"
    )

    # Get AI report record
    selected_ai = ai_report[
        ai_report["transaction_id"] == selected_transaction
    ]

    # Get transaction record
    transaction_data = transactions[
        transactions["transaction_id"] == selected_transaction
    ]

    if len(selected_ai) > 0 and len(transaction_data) > 0:

        selected_row = selected_ai.iloc[0]
        transaction = transaction_data.iloc[0]

        st.markdown(
            f"### 💳 {selected_transaction}"
        )

        # ==========================================
        # TRANSACTION DETAILS
        # ==========================================

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Transaction Amount",
                f"₹{float(transaction['amount']):,.2f}"
            )

        with col2:
            st.metric(
                "Settlement Amount",
                f"₹{float(transaction['settlement_amount']):,.2f}"
            )

        with col3:
            st.metric(
                "Settlement Status",
                transaction["settlement_status"]
            )

        # ==========================================
        # AMOUNT RECONCILIATION
        # ==========================================

        st.write("### 💰 Amount Reconciliation")

        amount_difference = (
            float(transaction["amount"])
            - float(transaction["settlement_amount"])
        )

        if abs(amount_difference) < 0.01:

            st.success(
                "✓ Amounts match — no financial difference detected."
            )

        else:

            st.error(
                f"⚠️ Amount difference: ₹{amount_difference:,.2f}"
            )

        # ==========================================
        # ISSUE & PRIORITY
        # ==========================================

        col1, col2 = st.columns(2)

        with col1:

            st.write("**⚠️ Issue**")

            st.info(
                str(selected_row["issue"])
            )

        with col2:

            st.write("**🚨 Priority**")

            if str(selected_row["priority"]).upper() == "HIGH":

                st.error(
                    str(selected_row["priority"])
                )

            else:

                st.warning(
                    str(selected_row["priority"])
                )

        # ==========================================
        # AI EXPLANATION
        # ==========================================

        st.divider()

        st.write("### 🤖 AI Explanation")

        st.info(
            str(selected_row["ai_explanation"])
        )

        # ==========================================
        # RECOMMENDED ACTION
        # ==========================================

        st.write("### 🛠️ Recommended Action")

        st.success(
            str(selected_row["recommended_action"])
        )

        st.divider()

        st.caption(
            "AI-generated analysis based on transaction reconciliation results."
        )

    else:

        st.warning(
            "Transaction details could not be found."
        )


# ==========================================
# DOWNLOAD REPORT
# ==========================================

st.divider()

st.subheader("📥 Reports")

csv_data = ai_report.to_csv(index=False)

st.download_button(
    label="Download AI Exception Report",
    data=csv_data,
    file_name="ai_exception_report.csv",
    mime="text/csv"
)


# ==========================================
# FOOTER
# ==========================================

st.divider()

st.caption(
    "AI Finance Controller • Transaction Reconciliation System"
)
