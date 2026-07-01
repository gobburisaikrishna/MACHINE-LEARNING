import matplotlib.pyplot as plt
import pandas as pd

# Load the dataset
df = pd.read_csv("student.csv")
df["TotalMarks"] = df["InternalMarks"] + df["Externalmarks"]
print("\nAverage Total Marks of Male Students:")
print(df[df["Gender"] == "M"]["TotalMarks"].mean())

print("\nAverage Total Marks of Female Students:")
print(df[df["Gender"] == "F"]["TotalMarks"].mean())

print("\nAverage Attendance by Gender:")
print(df.groupby("Gender")["Attendence"].mean())