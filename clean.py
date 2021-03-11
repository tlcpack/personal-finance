import pandas as pd
import numpy as np
import openpyxl
from datetime import datetime

df = pd.read_csv('mint-transactions-3-11-21.csv')

# columns = ['Date', 'Description', 'Original Description', 'Amount', 
# 'Transaction Type', 'Category', 'Account Name', 'Labels', 'Notes']

df['Date'] = pd.to_datetime(df['Date'])
df.sort_values(by='Date', ascending = False, inplace = True)

print(df.shape)

filtered_df = df.query("Date >= '2015-04-03'")

print(filtered_df.tail())