import pandas as pd
import numpy as np

# create a sample dataset with missing values and duplicates
data = {'Name': ['John', 'Alice', 'Bob', 'Mary', 'John', 'Alice', 'Bob', 'Mary'],
        'Age': [28, 21, 24, np.nan, 28, 22, 24, 27],
        'Gender': ['M', 'F', 'M', 'F', 'M', 'F', 'M', 'F'],
        'Salary': [50000, np.nan, 60000, 70000, 50000, 55000, np.nan, 70000]}

df = pd.DataFrame(data)

#1: Handling Missing Data
# fill in missing values in Age column with median
df['Age'].fillna(df['Age'].median(), inplace=True)

# fill in missing values in Salary column with mean
df['Salary'].fillna(df['Salary'].mean(), inplace=True)

# print updated DataFrame
print(df)

# 2: Filling and Replacing Values
# replace 'M' and 'F' with 'Male' and 'Female'
df['Gender'].replace({'M': 'Male', 'F': 'Female'}, inplace=True)

# print updated DataFrame
print(df)


#3: Removing Duplicates
# drop duplicate rows
df.drop_duplicates(inplace=True)

# print updated DataFrame
print(df)


#4: Detecting and Removing Outliers
# detect outliers using IQR method
Q1 = df['Salary'].quantile(0.25)
Q3 = df['Salary'].quantile(0.75)
IQR = Q3 - Q1
upper_bound = Q3 + 1.5*IQR
lower_bound = Q1 - 1.5*IQR
outliers = df[(df['Salary'] < lower_bound) | (df['Salary'] > upper_bound)]

# remove outliers from DataFrame
df.drop(outliers.index, inplace=True)

# print updated DataFrame
print(df)



