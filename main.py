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

print(worksheets)