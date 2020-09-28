import xlrd
import pandas as pd

file = r"C:\Users\Administrator\Desktop\报销模板_张勇.xls"

wb = xlrd.open_workbook(file)
sheets = wb.sheet_names()
print(sheets)
for sheet in sheets:
    data = pd.read_excel(file, sheet_name=sheet)
    print("-"*40+"%s"%sheet+"-"*40)
    print(data, type(data))




