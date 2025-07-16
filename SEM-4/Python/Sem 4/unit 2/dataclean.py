import pandas as pd
class emp():
    def clean_data(self):
        df = pd.read_csv("demo.csv")
        df.drop_duplicates(inplace=True)
        df.dropna(inplace=True)
        return df

# Usage example
if __name__ == "__main__":
    cleaner = emp()
    cleaned_df = cleaner.clean_data()
    print(cleaned_df)
    