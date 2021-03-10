import pandas as pd
import numpy as np
import openpyxl
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

now = datetime.now()
dt_string = now.strftime("%d-%m-%Y_%H-%M-%S")

wb = pd.ExcelFile('monthly_spending.xlsx')
worksheets = wb.sheet_names

feb = worksheets[4]
feb_frame = pd.read_excel(wb, feb)
feb_frame.rename(columns={datetime(2021, 2, 1, 0, 0): 'F-21'}, inplace = True)

# print(feb_frame.columns)

fig = px.line(feb_frame, x='Day', y='F-21', title='over time')
fig.show()