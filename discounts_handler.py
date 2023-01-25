from datetime import datetime

from discounts_parsers.aquamobil.aquamobil_1 import parser as aquamobil_1
from discounts_parsers.aquamobil.aquamobil_2 import parser as aquamobil_2
from discounts_parsers.aquamobil.aquamobil_3 import parser as aquamobil_3
from discounts_parsers.aquamobil.aquamobil_4 import parser as aquamobil_4
from discounts_parsers.chebarkul.chebarkul import parser as chebarkul
from discounts_parsers.crystal.crystal import parser as crystal
from discounts_parsers.gorny.gorny import parser as gorny
from discounts_parsers.luxe.luxe import parser as luxe
from discounts_parsers.niagara.niagara import parser as niagara
from discounts_parsers.zhivaya.zhivaya import parser as zhivaya

async def discounts_handle():
    month = datetime.now().month
    month = month if len(f'{month}') >= 2 else f'0{month}'
    year = f'{datetime.now().year}'[-2:]
    date = f'{datetime.now().day}.{month}.{year}'
    my_file = open("date.txt", "r")
    dateTxt = my_file.read()
    my_file.close()
    if date == dateTxt:
        return
    my_file = open("date.txt", "w")
    my_file.write(f'{date}')
    my_file.close()
    try:
        await aquamobil_1()
    except:
        pass
    try:
        await aquamobil_2()
    except:
        pass
    try:
        await aquamobil_3()
    except:
        pass
    try:
        await aquamobil_4()
    except:
        pass
    try:
        await chebarkul()
    except:
        pass
    try:
        await crystal()
    except:
        pass
    try:
        await gorny()
    except:
        pass
    try:
        await luxe()
    except:
        pass
    try:
        await niagara()
    except:
        pass
    try:
        await zhivaya()
    except:
        pass