import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("salaries.csv")

print("--- Initial Data Exploration ---")
print(df.head())
print("\n--- Summary Statistics ---")
print(df.describe())

# Data Cleaning / Manipulation
print("\n--- Average Salary by Department ---")
# Group by department and calculate the mean salary
dept_salary = df.groupby("Department")["Salary"].mean().sort_values(ascending=False)
print(dept_salary)

# Finding the highest paid role
highest_paid = df.loc[df["Salary"].idxmax()]
print("\n--- Highest Paid Role ---")
print(f"Role: {highest_paid['Job Title']}, Salary: ${highest_paid['Salary']}")

# Data Visualization
# Let's create a bar chart of average salary by department
plt.figure(figsize=(10, 6))
dept_salary.plot(kind="bar", color="skyblue", edgecolor="black")
plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary ($)")
plt.xticks(rotation=45)
plt.tight_layout()

# Save the plot instead of showing it so the script can run seamlessly
plt.savefig("department_salaries.png")
print("\nSaved visualization to 'department_salaries.png'")
