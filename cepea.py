import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from mpldatacursor import datacursor


def cleanData(dataframe):
    #transforma Data String em tipo datetime
    dataframe['Data'] = pd.to_datetime(dataframe['Data'], format='%d/%m/%Y')
    #troca ',' por '.' utilizando regex
    dataframe['À vista US$'] = dataframe['À vista US$'].str.replace(r'\,', '.').astype('float')
    #converte preço em dolar para tipo numérico
    dataframe['À vista US$'] = pd.to_numeric(dataframe['À vista US$'])
    #descarta coluna de preço em reais
    dataframe.drop('À vista R$', axis=1, inplace=True)
    #modifica nomes das colunas
    dataframe.columns = ['date', 'price']
    dataframe.sort_values(by='date',inplace=True, ascending=True)
    return dataframe

sojaData = pd.read_excel('sojaParanaDia.xls', 'Plan 1', index=False)
cafeData = pd.read_excel('cafeArabicaDia.xls', 'Plan 1', index=False)

sojaData = cleanData(sojaData)
cafeData = cleanData(cafeData)

minSojaDate = sojaData['date'][0]
minCafeDate = cafeData['date'][0]

maxDate = max([minCafeDate,minSojaDate])

sojaData = sojaData[sojaData['date'] > maxDate]
cafeData = cafeData[cafeData['date'] > maxDate]
sojaData['price'] = (sojaData['price'] - sojaData['price'].mean())/(sojaData['price'].max() - sojaData['price'].min())
cafeData['price'] = (cafeData['price'] - cafeData['price'].mean())/(cafeData['price'].max() - cafeData['price'].min())
lineSoja = plt.plot(sojaData['date'], sojaData['price'], label='Soja')
lineCafe = plt.plot(cafeData['date'], cafeData['price'], label='Café')
first_legend = plt.legend(handles=[lineSoja[0], lineCafe[0]])

datacursor()
plt.show()
