from datetime import datetime
import openpyxl
from parsers.aquamobil_aqua import parser as aquamobil_aqua
from parsers.aquamobil_arhiz import parser as aquamobil_arhiz
from parsers.aquamobil_artenza import parser as aquamobil_artenza
from parsers.aquamobil_kukuzar import parser as aquamobil_kukuzar
from parsers.aquamobil_sosnovskaya import parser as aquamobil_sosnovskaya
from parsers.chebarkul import parser as chebarkul
from parsers.crystal import parser as crystal
from parsers.gorny import parser as gorny
from parsers.lubima import parser as lubima
from parsers.luxe_luxik import parser as luxe_luxik
from parsers.luxe import parser as luxe
from parsers.niagara_caucasus import parser as niagara_caucasus
from parsers.niagara_premium import parser as niagara_premium
from parsers.niagara import parser as niagara
from parsers.vlasov import parser as vlasov
from parsers.zhivaya import parser as zhivaya

def excel_handle():
    wb = openpyxl.load_workbook('analysis.xlsx')
    month = datetime.now().month
    month = month if len(f'{month}') >= 2 else f'0{month}'
    year = f'{datetime.now().year}'[-2:]
    date = f'{datetime.now().day}.{month}.{year}'
    if date in wb:
        return
    last_sheet = wb.worksheets[-1]
    today_sheet = wb.copy_worksheet(last_sheet)
    today_sheet.title = date
    wb.save('analysis.xlsx')

excel_handle()