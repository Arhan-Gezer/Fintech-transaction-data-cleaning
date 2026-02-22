import pandas as pd
import numpy as np

RAW_PATH = "transactions_raw.csv"
CLEAN_PATH = "transactions_clean.csv"

def main():
    df = pd.read_csv(RAW_PATH)



    #timestamp type is wrong
    df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")  #errors="coerce" -> if there is wrong date or format pandas writes NaT(missing datetime)
    print(df["timestamp"].dtype)
    #print(df["timestamp"].isnull().sum())  # To check No wrong datetime

    #Create missing flags (keep missingness info)
    df["ip_country_missing"] = df["ip_country"].isna().astype(int)
    df["device_type_missing"] = df["device_type"].isna().astype(int)
    df["merchant_category_missing"] = df["merchant_category"].isna().astype(int)
    df["payment_method_missing"] = df["payment_method"].isna().astype(int)
    df["risk_score_missing"] = df["risk_score"].isna().astype(int)
    df["customer_age_missing"] = df["customer_age"].isna().astype(int)



    #mismatch after fallback (so NaN dosen't create fake mismatches)

    df["ip_country"] = df["ip_country"].fillna(df["country"])
    df["country_mismatch"] = (df["country"] != df["ip_country"]).astype(int)


    print("\nIP country missing rate (%):")
    print(df["ip_country_missing"].mean() * 100)

    print("\nCountry mismatch rate (%):")  #before fallback for accuracy
    print(df["country_mismatch"].mean() * 100)

    #Cathegorical types' missing = 'unknown'
    for col in ["device_type", "merchant_category", "payment_method"]:
            df[col] = df[col].fillna("unknown")

    # customer_age = country median
    df["customer_age"] = pd.to_numeric(df["customer_age"], errors="coerce")
    df["customer_age"] = df["customer_age"].fillna(
        df.groupby("country")["customer_age"].transform("median")
    )

    # risk_score = merchant_category median
    df["risk_score"] = pd.to_numeric(df["risk_score"], errors="coerce")
    df["risk_score"] = df["risk_score"].fillna(
        df.groupby("merchant_category")["risk_score"].transform("median")
    )

    #df["risk_score"] = df["risk_score"].round().clip(0, 100)

    #Creating Risk Segments
    
    df.to_csv(CLEAN_PATH, index=False)
    print(f"\nSave clean dataset to -> {CLEAN_PATH}")


if __name__ == "__main__":
    main()





