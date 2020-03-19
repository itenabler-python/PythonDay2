from openpyxl import *
import csv

workbook = load_workbook("testexcel.xlsx")
sheet = workbook["Sheet1"]

max_row = sheet.max_row
max_col = sheet.max_col

writefilecsv = open("testcsv", "w", newline='')
write1=csv.writer(writefilecsv)

for row in range(1, max_row+1):
    if row % 2 == 0:
        for cell in row:


