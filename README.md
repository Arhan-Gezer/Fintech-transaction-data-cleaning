# FinTech Transaction Risk & Fraud Analysis
* End-to-end fraud risk analysis on a 20,000-row transaction dataset using Python and Scikit-learn.
* This project explores fraud detection under extreme class imbalance (~0.96% dispute rate) and evaluates model performance from both a technical and operational perspective.

## Dataset Overview
* Total transactions: 20,000
* Disputed transactions: 192 (~0.96%)
* Imbalance ratio: ~1:104
* Train/Test split: 80/20 (stratified)
* Each row represents a financial transaction from a payment platform.

## Data Cleaning
##Data Cleaning & Feature Engineering
- Converted timestamps to datetime
- Created missing-value indicator flags
- Median-based imputation (country-level & merchant-level)
- Country mismatch feature engineering
- One-hot encoding for categorical variables
- Stratified sampling to preserve class distribution

  
## KPI & Risk Analysis

- Calculated dispute rate and chargeback exposure
- Estimated net profit after chargeback losses
- Risk segmentation using quantile-based grouping
- High-risk segment showed higher dispute rate but also higher profit per transaction

## Fraud Modeling
Logistic Regression (class_weight="balanced")
- ROC-AUC: 0.53
- Recall (fraud class): ~0.52 at threshold 0.5
- High false positive rate under recall-optimized settings

Random Forest (200 trees)
- ROC-AUC: 0.52
- No significant improvement over linear baseline

## Key Insight
Despite testing both linear and non-linear models, performance remained close to random (ROC-AUC ≈ 0.52–0.54).

Feature distribution analysis revealed heavy overlap between fraud and non-fraud transactions, indicating limited discriminative signal in the current feature set.

Conclusion: Performance bottleneck appears data-driven rather than model-driven.

## Project Takeaway

This project demonstrates the importance of feature quality in imbalanced classification problems. 
It highlights that increasing model complexity does not compensate for weak data signal.

Emphasized practical evaluation techniques such as:
- Class-weight balancing
- Threshold optimization
- Precision–Recall tradeoff analysis
- Operational Top-K simulation

  
## Technologies

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib

## Data Dictionary (Key Fields)

| Column | Description |
|--------|------------|
| transaction_id | Unique transaction identifier |
| status | Transaction outcome (captured, failed, refunded, disputed) |
| risk_score | Fraud risk score (0–100) |
| amount | Transaction amount |
| country_mismatch | Country vs IP country mismatch flag |
| fee_amount | Platform commission |
| net_revenue | Platform earnings |
| chargeback_loss_est | Estimated dispute loss |
