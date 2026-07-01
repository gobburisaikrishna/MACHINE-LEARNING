import matplotlib.pyplot as plt
import pandas as pd

# Load the dataset
df = pd.read_csv("student.csv")
df["TotalMarks"] = df["InternalMarks"] + df["Externalmarks"]
df["Percentage"] = (df["TotalMarks"] / 100) * 100

print("\nUpdated DataFrame:")
print(df)
