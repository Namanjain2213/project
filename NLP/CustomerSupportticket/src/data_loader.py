from datasets import load_dataset


def load_banking77():
    dataset = load_dataset("mteb/banking77")

    train_df = dataset["train"].to_pandas()
    test_df = dataset["test"].to_pandas()

    return train_df, test_df