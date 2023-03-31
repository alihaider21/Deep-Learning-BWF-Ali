#Task 14 Reading File in Pandas
import pandas as pd
from sqlite3 import connect

#reading csv file
read_csv = pd.read_csv('winequality.csv')
print(read_csv.head())

#reading excel file
read_excel = pd.read_excel('stock_data.xlsx')
print(read_excel.head())

#reading json 
data = {
  "Duration":{"0":60,"1":60,"2":60,"3":45,"4":45,"5":60
  },
  "Pulse":{"0":110,"1":117,"2":103,"3":109,"4":117,"5":102
  },
  "Maxpulse":{"0":130,"1":145,"2":135,"3":175,"4":148,"5":127
  },
  "Calories":{"0":409,"1":479,"2":340,"3":282,"4":406,"5":300
  }
}

read_json = pd.read_json(data)
print(read_json.head())

#reading sql file
#This is just an example query. for querying in pandas. we need to have connection with database
conn = connect(':memory:')
read_sql = pd.read_sql('SELECT int_column, date_column FROM test_data',
            conn,
            parse_dates=["date_column"])
print(read_sql.head())

#reading pickle file
read_pickle = pd.read_pickle('avoplotto.pkl')
print(read_pickle.head())
