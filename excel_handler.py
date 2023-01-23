from openpyxl import load_workbook

def excel_handle():
    wb = load_workbook('./analysis.xlsx')
    print(wb.get_sheet_names())

excel_handle()