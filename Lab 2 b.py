import matplotlib.pyplot as plt
import pandas as pd

# Load the dataset
df = pd.read_csv("student.csv")

import matplotlib.pyplot as plt
import pandas as pd

# Load the dataset
df = pd.read_csv("student.csv")

# Clean column headers just in case there are hidden spaces
df.columns = df.columns.str.strip()

# Print individual statistical metrics using your exact CSV spellings
print(f"Mean Attendance: {df['Attendence'].mean():.2f}%")
print(f"Average Internal Marks: {df['InternalMarks'].mean():.2f}")
print(f"Average External Marks: {df['Externalmarks'].mean():.2f}")

print(f"\nMaximum Internal Marks: {df['InternalMarks'].max()}")
print(f"Minimum Internal Marks: {df['InternalMarks'].min()}")

print(f"\nMaximum External Marks: {df['Externalmarks'].max()}")
print(f"Minimum External Marks: {df['Externalmarks'].min()}")

print(
    f"\nStandard Deviation of Internal Marks: {df['InternalMarks'].std():.2f}"
)

nt("\nSummary Statistics:")
print(df.describe())
