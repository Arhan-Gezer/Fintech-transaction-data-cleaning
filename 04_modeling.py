import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv("transactions_clean.csv")

#
##making disputed column
df["is_disputed"] = (df["status"] == "disputed").astype(int)


print("Rows:", len(df))
print("Target distribution:")
print(df["is_disputed"].value_counts())
print("\nTarget rate (%):", df["is_disputed"].mean() * 100)

##Feature selection

feature_cols = [
    "risk_score",
    "amount",
    "country_mismatch",
    "ip_country_missing",
    "device_type_missing",
    "merchant_category_missing",
    "payment_method_missing",
    "merchant_category",
    "device_type",
    "payment_method"
]

X = df[feature_cols]
y = df["is_disputed"]
print("Feature shape:", X.shape)
#Categorical Encoding
X_encoded = pd.get_dummies(
    X,
    columns=["merchant_category", "device_type", "payment_method"],
    drop_first=True  # dummy trap'ı önlemek için
)
print("Encoded feature shape:", X_encoded.shape)
#print(X_encoded.columns)

X_train, X_test, y_train, y_test = train_test_split(
    X_encoded,
    y,
    test_size=0.2,
    random_state=0,
    stratify=y
)

print("Train shape:", X_train.shape)
print("Test shape:", X_test.shape)

print("\nTrain disputed distribution:")
print(y_train.value_counts())

print("\nTest disputed distribution:")
print(y_test.value_counts())





















