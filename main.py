import pandas as pd
import numpy as np
import openpyxl
import plotly.express as px
import plotly.graph_objects as go
import dtale
from datetime import datetime

now = datetime.now()
dt_string = now.strftime("%d-%m-%Y_%H-%M-%S")

wb = pd.ExcelFile('monthly_spending.xlsx')
worksheets = wb.sheet_names

jan = worksheets[3]
jan_frame = pd.read_excel(wb, jan)
jan_frame.rename(columns={'Unnamed: 1': 'Vendor'}, inplace = True)
# print(jan_frame.columns)
# print(jan_frame.head())

new_j_df = jan_frame.drop(jan_frame.index[[0,1]])

# print(new_j_df.head())

feb = worksheets[4]
feb_frame = pd.read_excel(wb, feb)
feb_frame.rename(columns={datetime(2021, 2, 1, 0, 0): 'F-21'}, inplace = True)

# print(feb_frame.columns)

fig = px.line(feb_frame, x='Day', y=['F-21','Income'], title='over time')
sun = px.sunburst(new_j_df, path=['category', 'Vendor'], values='amount')
sun.show()

# fig.show()

# d = dtale.show(feb_frame)

# d.open_browser()