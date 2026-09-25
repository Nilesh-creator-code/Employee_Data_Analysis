from matplotlib import colors
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
# print(df.describe())

print("\nIndividual statistics")
print("Count of Salary: ", df["Salary"].count())
print("Average Salary: ", df["Salary"].mean())

print("Median Salary: ", df["Salary"].median())

print("Minimum Salary: ", df["Salary"].min())

print("Maximum Salary: ", df["Salary"].max())

print("Standard Deviation of Salary: ", df["Salary"].std())

print("Variance of Salary: ", df["Salary"].var())

print("Skewness of Salary: ", df["Salary"].skew())

print("Average Performance Score: ", df["Performance_Score"].mean())
print("Median Performance Score: ", df["Performance_Score"].median())
print("Minimum Performance Score: ", df["Performance_Score"].min())
print("Maximum Performance Score: ", df["Performance_Score"].max())

print("Average Experience Years: ", df["Experience_Years"].mean())
print("Median Experience Years: ", df["Experience_Years"].median())
print("Minimum Experience Years: ", df["Experience_Years"].min())
print("Maximum Experience Years: ", df["Experience_Years"].max())



print("\n Highest-paid employees:")
highest_paid = df.sort_values(by="Salary", ascending=False).head(10)

print(highest_paid.head(10))




# Lowest-paid employees
print("\n Lowest-paid employees:")
lowest_paid = df.sort_values(by="Salary", ascending=True).head(10)

print(lowest_paid.head(10))

# Display selected columns
print(lowest_paid[
    [
        "Employee_ID",
        "Gender",
        "Age",
        "Salary",
        "Experience_Years",
        "Performance_Score"
    ]
])


# Salary distribution
# print("\n Salary distribution:")
# plt.figure(figsize=(10, 6))
# sns.histplot(df["Salary"], bins=30, kde=True, color="red")   
# plt.title("Salary Distribution")
# plt.xlabel("Salary")
# plt.ylabel("Frequency")
# plt.show()

# plt.figure(figsize=(8, 6))
# sns.boxplot(x=df["Salary"], color="lightblue")
# plt.title("Salary Boxplot")
# plt.xlabel("Salary")

# plt.show()


# Salary distribution by Gender
# print("\n Salary distribution by Gender:")
# plt.figure(figsize=(10, 6))
# sns.histplot(
#     data=df,
#     x="Salary",
#     hue="Gender",
#     bins=30,
#     kde=True
# )
# plt.title("Salary Distribution by Gender")
# plt.xlabel("Salary")
# plt.ylabel("Frequency")
# plt.show()


# Average salary by department
department_salary = df.groupby("Department")["Salary"].mean().sort_values(ascending=False)
print("\n Average salary by department:")
print(department_salary)

# Visualize average salary by department
# plt.figure(figsize=(10, 6))

# colors = ["skyblue", "orange", "green", "red", "purple", "gold", "pink"]

# department_salary.plot(kind="bar", color=colors[:len(department_salary)])

# plt.title("Average Salary by Department")
# plt.xlabel("Department")
# plt.ylabel("Avergae Salary")

# plt.xticks(rotation=45)
# plt.tight_layout()

# plt.show()


# Department employment count
department_employment = df.groupby("Department").size()
print("\n Department employment count:")
print(department_employment)

plt.figure(figsize=(10, 6))

colors = [
    "red",
    "blue",
    "green",
    "orange",
    "purple",
    "yellow"
]

department_employment.plot(kind="bar", color=colors[:len(department_employment)])

plt.title("Number of Employees by Department")
plt.xlabel("Department")
plt.ylabel("Number of Employees")

plt.xticks(rotation=45)
plt.tight_layout()

# plt.show()

# Department Salary statistics
department_salary_stats = df.groupby("Department")["Salary"].agg(["mean", "std", "min", "max"])

print("\n Department Salary statistics:")
print(department_salary_stats)

# Experience vs Salary Visualization
# Scatter plot of Experience vs Salary
plt.figure(figsize=(10, 6))

sns.scatterplot(
    data=df,
    x="Experience_Years",
    y="Salary",
    hue="Department",
    palette="Set1"
)

plt.title("Experience vs Salary by Department")
plt.xlabel("Experience (Years)")
plt.ylabel("Salary")

# plt.show()

# Adding the trend line to the scatter plot
plt.figure(figsize=(10, 6))

sns.regplot(
    data=df,
    x="Experience_Years",
    y="Salary",
    scatter_kws={"s": 50, "alpha": 0.5},
    line_kws={"color": "red", "lw": 2}
)

plt.title("Experience vs Salary with Trend Line")
plt.xlabel("Experience (Years)")
plt.ylabel("Salary")

# plt.show()

# Avergae Salary byb performance score

performance_salary = df.groupby("Performance_Score")["Salary"].mean().sort_values(ascending=False)
print("\n Average Salary by Performance Score:")
print(performance_salary)

# Now i create bar chart of it
plt.figure(figsize=(8, 5))

performance_salary.plot(kind="bar", color="lightgreen")
plt.title("Average Salary by Performance Score")
plt.xlabel("Performance Score")
plt.ylabel("Average Salary")

plt.tight_layout()
plt.show()