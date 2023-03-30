#Topics: Starting with Pandas, Series and DataFrame
import pandas as pd

#Create a Series object with the following data: [1, 2, 3, 4, 5]. Set the index to ['a', 'b', 'c', 'd', 'e'].
data = [1, 2, 3, 4, 5]
index = ['a', 'b', 'c', 'd', 'e']
series = pd.Series(data=data, index=index)

print(series.head())

#Create a DataFrame 
data = {
    'Name': ['John', 'Jane', 'Bob'],
    'Age': [24, 28, 35],
    'Gender': ['M', 'F', 'M']
}
df = pd.DataFrame(data)
print(df.head())


#Select the first three rows of the created DataFrame 
print(df.head(3))


#Select the "Age" column of the DataFrame created 
age_column = df['Age']
print(age_column.head())


#Add a new column to the DataFrame created in step 2 called "City" with the following data:
city_data = {
    'City': ['New York', 'Los Angeles', 'Chicago']
}

city_column = pd.DataFrame(city_data)

df['City'] = city_column

print(df.head())