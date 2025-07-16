import pandas as pd
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Emma"],
    "Age": [25, 30, 35, 28, 40],
    "Salary": [50000, 60000, 70000, 55000, 80000],
    "Department": ["HR", "IT", "Finance", "Marketing", "IT"]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
print("\n")


df_q1 = df.drop('Age', axis=1)
print("Q1. DataFrame after removing Age column:")
print(df_q1)
print("\n")


df_q2 = df.copy()
df_q2['Experience'] = [2, 5, 7, 3, 10]
print("Q2. DataFrame after adding Experience column:")
print(df_q2)
print("\n")


df_q3 = df.drop(['Salary', 'Department'], axis=1)
print("Q3. DataFrame after removing Salary and Department columns:")
print(df_q3)
print("\n")


df_q4 = df[['Name', 'Salary']]
print("Q4. DataFrame with only Name and Salary columns:")
print(df_q4)
print("\n")


df_q5 = df[df['Department'] == 'IT']
print("Q5. Employees in IT department:")
print(df_q5)
print("\n")


df_q6 = df.copy()
df_q6 = df_q6.rename(columns={'Salary': 'Income'})
print("Q6. DataFrame after renaming Salary to Income:")
print(df_q6)
print("\n")


df_q7 = df.copy()
df_q7.columns = [col.upper() for col in df_q7.columns]
print("Q7. DataFrame with uppercase column names:")
print(df_q7)
print("\n")


df_q8 = df[df['Age'] > 30]
print("Q8. Employees older than 30:")
print(df_q8)
print("\n")


df_q9 = df[df['Name'].str.startswith('A')]
print("Q9. Employees whose name starts with 'A':")
print(df_q9)
print("\n")


df_q10 = df[(df['Salary'] >= 55000) & (df['Salary'] <= 75000)]
print("Q10. Employees with salary between 55,000 and 75,000:")
print(df_q10)
print("\n")


df_q11 = df[df['Department'].isin(['IT', 'HR'])]
print("Q11. Employees who work in IT or HR:")
print(df_q11)
