#cleaning
import pandas as pd

data = {
    "Age": [25, 30, None, 40, 35]
}

df = pd.DataFrame(data)
df["Age"].fillna(df["Age"].mean(), inplace=True)

print(df)