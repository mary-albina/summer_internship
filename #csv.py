#csv
import pandas as pd

df = pd.read_csv("data.csv")

print("Average:", df["Score"].mean())
print("Highest:", df["Score"].max())
print("Lowest:", df["Score"].min())