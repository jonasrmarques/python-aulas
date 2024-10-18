import requests
from openpyxl import Workbook



url = 'https://loteriascaixa-api.herokuapp.com/api/megasena'
res = requests.get(url)

convertJson = res.json()




wb = Workbook()
ws = wb.active

ws.append(['Data do Sorteia', 'Dezenas do Sorteio'])

for user in convertJson:
    lista = str(user['dezenas'])
    ws.append([user['data'], lista])

wb.save('datasEDezenas.xlsx')