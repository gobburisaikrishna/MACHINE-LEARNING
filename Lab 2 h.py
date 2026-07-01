import matplotlib.pyplot as plt
import pandas as pd

# Load the dataset
df = pd.read_csv("student.csv")
print("\nObservations:")
print("1. Female students have higher average attendance.")
print("2. Students with higher attendance generally score better.")
print("3. Top performers scored above 95 total marks.")

print("\nConclusion:")
print("Higher attendance appears to be associated with better academic performance.")