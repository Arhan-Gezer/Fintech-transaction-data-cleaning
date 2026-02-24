import pandas as pd


# Read csv
df = pd.read_csv("transactions_raw.csv")


def missing_data_summary(df):
    print("\n===== MISSING DATA SUMMARY =====\n")

    total_rows = df.shape[0]
    total_columns = df.shape[1]
    total_missing_count = df.isnull().sum().sum()
    rows_with_missing = df[df.isnull().any(axis=1)].shape[0]

    print(f"Total rows: {total_rows}")
    print(f"Total columns: {total_columns}")
    print(f"Total missing cells: {total_missing_count}")
    print(f"Rows with at least one missing value: {rows_with_missing}")

    print("\n--- Missing by Column ---")
    missing_count = df.isnull().sum()
    missing_percent = (df.isnull().mean() * 100)

    summary = (
        pd.DataFrame({
            "missing_count": missing_count,
            "missing_percent": missing_percent
        })
        .sort_values(by="missing_percent", ascending=False)
    )

    print(summary[summary["missing_count"] > 0])
    print(f"\nOverall missing rate: {(total_missing_count / (total_rows * total_columns)) * 100:.2f}%")
    df.info()
    
                                                                               
missing_data_summary(df)

print("First 5 Row:")
print(df.head())

#number of duplicate transactions
duplicate_count = df["transaction_id"].duplicated().sum()
print(f"Duplicate transaction_id Count: {duplicate_count}")

#type control
print(df.dtypes)

#Check if there is a problem with unique types (if there is too many different currency type etc.)
for col in df.select_dtypes(include="object").columns:
    print(col, df[col].nunique()) 

df_clean = pd.read_csv("transactions_clean.csv")
missing_data_summary(df_clean)


