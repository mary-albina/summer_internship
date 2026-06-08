import pandas as pd

students = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Marks": [85, 72, 90, 78]
}
df = pd.DataFrame(students) 
result = df[df["Marks"] > 80]
print(result)
