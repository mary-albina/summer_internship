#cleaning2
import pandas as pd

data = {
    "CustomerID": [101, 102, 103, 102, 104, 103],
    "Name": ["John", "Mary", "Sam", "Mary", "Tom", "Sam"]
}

df = pd.DataFrame(data)

duplicates = df.duplicated().sum()

df_clean = df.drop_duplicates()

print("Duplicates Removed:", duplicates)
print(df_clean)