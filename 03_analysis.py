import pandas as pd
import numpy as np

#1) KPI (Key Performance Indicator)
import pandas as pd

CLEAN_PATH = "transactions_clean.csv"

df = pd.read_csv(CLEAN_PATH)

print("\n===== GENERAL KPI SUMMARY =====\n")

# 1️⃣ Total transactions
total_tx = len(df)
print(f"Total Transactions: {total_tx:,}")

# 2️⃣ Status dağılımı (%)
status_distribution = df["status"].value_counts(normalize=True) * 100
print("\nStatus Distribution (%):")
print(status_distribution)

# 3️⃣ Capture / Refund / Dispute rate
capture_rate = (df["status"] == "captured").mean() * 100
refund_rate = (df["status"] == "refunded").mean() * 100
dispute_rate = (df["status"] == "disputed").mean() * 100

print(f"\nCapture Rate: {capture_rate:.2f}%")
print(f"Refund Rate: {refund_rate:.2f}%")
print(f"Dispute Rate: {dispute_rate:.2f}%")

# 4️⃣ Revenue KPI
total_fee = df["fee_amount"].sum()
total_net_revenue = df["net_revenue"].sum()
total_chargeback_loss = df["chargeback_loss_est"].sum()

print(f"\nTotal Fee Revenue: {total_fee:,.2f}")
print(f"Total Net Revenue: {total_net_revenue:,.2f}")
print(f"Total Chargeback Loss Estimate: {total_chargeback_loss:,.2f}")

# 5️⃣ Net Profit Estimate
net_profit_estimate = total_net_revenue - total_chargeback_loss
print(f"\nEstimated Net Profit After Chargebacks: {net_profit_estimate:,.2f}")














#finding overall dispute rate 
dispute_rate = (df["status"] == "disputed").mean() * 100
print(f"Overall dispute rate: {dispute_rate:.2f}%")


dispute_by_mismatch = (
    df.groupby("country_mismatch")["status"]
      .apply(lambda x: (x == "disputed").mean() * 100)
)

print(dispute_by_mismatch)  #Dispute is not affected by mismatch


#all risk_score are stacked at low with %85 low if we do labels with 0 30 60 90 so we do qcut for equal distribution
df["risk_segment_q"] = pd.qcut(
    df["risk_score"],
    q=3,
    labels=["Low", "Medium", "High"]
)

print(df["risk_segment_q"].value_counts(dropna=False))

dispute_by_segment = (
    df.groupby("risk_segment_q")["status"]
      .apply(lambda x: (x == "disputed").mean() * 100)
)

print("\nDispute rate by risk segment (%):")
print(dispute_by_segment)