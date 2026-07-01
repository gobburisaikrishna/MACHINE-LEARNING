import matplotlib.pyplot as plt
import pandas as pd

# Load the dataset
df = pd.read_csv("student.csv")
df["TotalMarks"] = df["InternalMarks"] + df["Externalmarks"]
print("\nAttendance > 90")
print(df[df["Attendence"] > 90])

print("\nTotal Marks > 90")
print(df[df["TotalMarks"] > 90])

print("\nFemale Students")
print(df[df["Gender"] == "F"])

print("\nMale Students")
print(df[df["Gender"] == "M"])

print("\nExternal marks < 50")
print(df[df["Externalmarks"] < 50])
