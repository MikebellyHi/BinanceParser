from binance.spot import Spot as Client

api = Client()
response = api.ticker_24hr()
tickers_price = api.ticker_price()
symbolList = []
priceList = []
highPriceList = []
lowPriceList = []
priceChangeList = []
pricePercentChangeList = []
volumeList = []
for pair in tickers_price:
    for pair2 in response:
        if pair['symbol'] == pair2['symbol']:
            symbolList.append(pair['symbol'])
            priceList.append(pair['price'])
            highPriceList.append(pair2['highPrice'])
            lowPriceList.append(pair2['lowPrice'])
            priceChangeList.append(pair2['priceChange'])
            pricePercentChangeList.append(pair2['priceChangePercent'] + '%')
            volumeList.append(pair2['volume'])

data = {'Название пары': symbolList, 'Текущая цена': priceList, 'Максимальная цена за сутки': highPriceList, 'Минимальная цена за сутки': lowPriceList, 'Изменение цены за сутки': priceChangeList, 'Изменение цены в процентах за сутки': pricePercentChangeList, 'Объем торгов за сутки': volumeList}

'''
Название пары - Текущая цена - Максимальная цена за сутки - Минимальная цена за сутки - Изменение цены за сутки - Изменение цены в процентах за сутки - Объем торгов за сутки
'''
