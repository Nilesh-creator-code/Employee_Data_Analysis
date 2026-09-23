import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv(r"D:\Learning_Project\Emplyee_Salary_Analysis\main\employee_performance.csv")


# print(df.to_string())  # Display the entire DataFrame

# Show the null values in the dataset
# print(df.isnull().sum())

# Manage the null values in the dataset
df["Experience_Years"] = df["Experience_Years"].fillna(
    df["Experience_Years"].median()
)

df["Performance_Score"] = df["Performance_Score"].fillna(
    df["Performance_Score"].median()
)

df["Salary"] = df["Salary"].fillna(
    df["Salary"].median()
)

df["Age"] = df["Age"].fillna(
    df["Age"].median()
)

print("\nNull values:")
print(df.isnull().sum())

# Check data types
print("\nData types:")
print(df.dtypes)

# Display final columns
print("\nFinal columns:", df.columns.tolist())


# Print all duplicate value in dataset
# print("duplicate : ", df.duplicated().sum())
df = df.drop_duplicates()
# print(df.dtypes)

# print(df.to_string())  # Display the entire DataFrame after filling null values

# print(df.columns.tolist())

# Convert numeric coulmn

numeric_columns = [
    "Age",
    "Experience_Years",
    "Salary",
    "Performance_Score"
]

for col in numeric_columns:
    df[col] = pd.to_numeric(df[col], errors="coerce")


# Now check the invalid values
print("Invalid values count:")

print("Age:", (df["Age"] < 0).sum())

print("Experience:", (df["Experience_Years"] < 0).sum())

print("Salary:", (df["Salary"] < 0).sum())

print("Performance:", (df["Performance_Score"] < 0).sum())


# Now i perfrom statical analysis on the dataset
print("\nStatistical Analysis:")
print(df.describe())