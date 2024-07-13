import pandas as pd
file_errors_location = 'I:\Py project\DBTGSchwerin\gesamte Information.xlsx'
df = pd.read_excel(file_errors_location)
print(df.values)