import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    "Name": ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank", "Grace"],
    "Age": [25, 30, 35, 40, 28, 32, 45],
    "Department": ["HR", "IT", "Finance", "Marketing", "HR", "IT", "Finance"],
    "Salary": [50000, 60000, 70000, 80000, 52000, 62000, 75000]
}

df = pd.DataFrame(data)

df.to_csv("my_dataset.csv", index=False)
print("Dataset created and saved as 'my_dataset.csv'")


try:

    dataset = pd.read_csv("my_dataset.csv")
    
    print("\nFirst 5 rows of the dataset:")
    print(dataset.head())

    print("\nDataset Info:")
    print(dataset.info())
    print("\nMissing Values:")
    print(dataset.isnull().sum())
except FileNotFoundError:
    print("Error: The file 'my_dataset.csv' was not found!")
    exit()

print("\nBasic Statistics of Numerical Columns:")
print(dataset.describe())

grouped_data = dataset.groupby("Department")["Salary"].mean()
print("\nAverage Salary by Department:")
print(grouped_data)

plt.figure(figsize=(10, 6))
plt.plot(dataset["Age"], marker='o', label="Age", color="blue")
plt.title("Line Chart: Age vs Index")
plt.xlabel("Index")
plt.ylabel("Age")
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
sns.barplot(x=grouped_data.index, y=grouped_data.values, palette="viridis")
plt.title("Bar Chart: Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.show()

plt.figure(figsize=(10, 6))
sns.histplot(dataset["Age"], bins=10, kde=True, color="purple")
plt.title("Histogram: Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

plt.figure(figsize=(10, 6))
sns.scatterplot(x="Age", y="Salary", data=dataset, hue="Department", palette="Set2", s=100)
plt.title("Scatter Plot: Age vs Salary (Colored by Department)")
plt.xlabel("Age")
plt.ylabel("Salary")
plt.legend(title="Department")
plt.show()

print("\nObservations:")
print("- Employees in the 'Finance' department have the highest average salary.")
print("- The histogram shows that most employees are between 25 and 40 years old.")
print("- There is a positive trend between age and salary, indicating older employees may earn more.")
