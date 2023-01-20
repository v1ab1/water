from aquamobil import parser as aquamobil
from chebarkul import parser as chebarkul
from gorny import parser as gorny
from lubima import parser as lubima
from vlasov import parser as vlasov
# from zhivaya import parser as zhivaya
from prettytable import PrettyTable
funclist = [aquamobil, chebarkul, gorny, lubima, vlasov]
complist = ["aquamobil", "chebarkulsky istok", "gorny", "lubima", "vlasov kluch"]
pricelist = []
for func in funclist:
    pricelist.append(int(func()))
outTable = PrettyTable()
outTable.field_names = [' '] + complist
outTable.add_row(['price'] + pricelist)
print(outTable)
