import matplotlib.pyplot as plt
import pandas as pd

# Load the dataset
df = pd.read_csv("student.csv")
df["TotalMarks"] = df["InternalMarks"] + df["Externalmarks"]
print("\nHighest Total Marks Student:")
print(df.loc[df["TotalMarks"].idxmax()])

print("\nLowest Total Marks Student:")
print(df.loc[df["TotalMarks"].idxmin()])

print("\nTop 3 Performers:")
print(df.nlargest(3, "TotalMarks"))

print("\nBottom 3 Performers:")
print(df.nsmallest(3, "TotalMarks"))

average = df["TotalMarks"].mean()

print("\nStudents Scoring Above Class Average:")
print(df[df["TotalMarks"] > average])

print("Count:", len(df[df["TotalMarks"] > average]))