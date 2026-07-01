import matplotlib.pyplot as plt
import pandas as pd

# Load the dataset
df = pd.read_csv("student.csv")
df["TotalMarks"] = df["InternalMarks"] + df["Externalmarks"]
plt.figure(figsize=(8,5))
plt.bar(df["Name"], df["TotalMarks"])
plt.title("Total Marks of Students")
plt.xlabel("Students")
plt.ylabel("Total Marks")
plt.show()

# Histogram
plt.figure(figsize=(6,5))
plt.hist(df["Attendence"], bins=5)
plt.title("Attendance Distribution")
plt.xlabel("Attendance")
plt.ylabel("Frequency")
plt.show()

# Pie Chart
gender_count = df["Gender"].value_counts()

plt.figure(figsize=(5,5))
plt.pie(gender_count,
        labels=gender_count.index,
        autopct="%1.1f%%",
        startangle=90)
plt.title("Gender Distribution")
plt.show()

# Scatter Plot
plt.figure(figsize=(6,5))
plt.scatter(df["Attendance"], df["TotalMarks"])
plt.title("Attendance vs Total Marks")
plt.xlabel("Attendance")
plt.ylabel("Total Marks")
plt.show()

print("\nInterpretation:")
print("Students with higher attendance generally tend to score higher total marks.")
