import pandas as pd

# Load spreadsheet
xl = pd.ExcelFile('Data_Lecture 3.xlsx')

# Load a sheet into a DataFrame by its name
df1 = xl.parse('Ice Cream Data')

# Load a sheet into a DataFrame by its index (0-based)
df2 = xl.parse(0)

print(df1.columns)
