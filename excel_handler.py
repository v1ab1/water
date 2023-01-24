from datetime import datetime
from openpyxl import load_workbook

def excel_handle():
    wb = load_workbook('./analysis.xlsx')
    month = datetime.now().month
    month = month if len(f'{month}') >= 2 else f'0{month}'
    year = f'{datetime.now().year}'[-2:]
    date = f'{datetime.now().day}.{month}.{year}'
    if date in wb == False:
        return
    wb.create_sheet(date)
    wb.save('analysis.xlsx')

excel_handle()