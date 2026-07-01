
import pandas as pd
import matplotlib.pyplot as plt



df = pd.read_csv("student.csv")

print("First 5 Records:")
print(df.head())

print("\nLast 5 Records:")
print(df.tail())

print("\nShape of Dataset:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nData Types:")
print(df.dtypes)