from data_loader import load_banking77


train_df, test_df = load_banking77()

print("Train shape:", train_df.shape)
print("Test shape:", test_df.shape)

print("\nTrain columns:")
print(train_df.columns)

print("\nFirst 5 rows:")
print(train_df.head())