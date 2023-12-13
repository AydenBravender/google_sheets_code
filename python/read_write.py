import gspread
import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.service_account import ServiceAccountCredentials


scope = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]
gr_10 = []
gr_11 = []
gr_12 = []

creds = ServiceAccountCredentials.from_json_keyfile_name("C:\\Users\\Bravender\\Desktop\\FBLA\\data\\secret_key.json", scopes=scope)

file = gspread.authorize(creds)
workbook = file.open("python_test")
sheet = workbook.sheet1

def find_grade_10():
    for i in sheet.range('B2:B8'):
        try:
            if int(i.value) == 10:
                gr_10.append(sheet.cell(i.row, 1).value)
        except ValueError:
            pass
    return gr_10

def find_grade_11():
    for i in sheet.range('B2:B8'):
        try:
            if int(i.value) == 11:
                gr_11.append(sheet.cell(i.row, 1).value)
        except ValueError:
            pass
    return gr_11

def find_grade_12():
    for i in sheet.range('B2:B8'):
        try:
            if int(i.value) == 12:
                gr_12.append(sheet.cell(i.row, 1).value)
        except ValueError:
            pass
    return gr_12

def find_name(name):
    i = 1
    cell_value = True
    while cell_value is not None:
        worksheet = workbook.get_worksheet(0)  # Get the first worksheet
        cell_value = worksheet.acell(f'A{i}').value
        if cell_value == name:
            return cell_value
        i =+1 

         
        

print(f"Grade 10's {find_grade_10()}")
print(f"Grade 11's {find_grade_11()}")
print(f"Grade 12's {find_grade_12()}")

name = input("enter name: ")
print(find_name(name))










    


