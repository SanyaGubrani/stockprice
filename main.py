import yfinance as yf
from forex_python.converter import CurrencyCodes
import matplotlib.pyplot as plt
from requests.exceptions import HTTPError

stock = input("Enter the stock symbol: ").upper()

try:

    ticker = yf.Ticker(stock).info

    def convert_market_cap(market_cap, currency_symbol):
        """Function to convert market capital to readable format"""

        if market_cap < 1_000_000_000:
            return f"{currency_symbol}{market_cap / 1_000_000:.2f}M"
        elif market_cap < 1_000_000_000_000:
            return f"{currency_symbol}{market_cap / 1_000_000_000:.2f}B"
        else:
            return f"{currency_symbol}{market_cap / 1_000_000_000_000:.2f}T"


    #Fetching & printing stock's information

    market_price = ticker['currentPrice']
    previous_day_close = ticker['regularMarketPreviousClose']
    company_name = ticker['longName']
    sector = ticker['sector']
    market_cap = ticker['marketCap']
    currency_name = ticker['currency']

    currency_codes = CurrencyCodes()
    currency_symbol = currency_codes.get_symbol(currency_name)

    print(f'Ticker: {stock}')
    print('Company Name:', company_name)
    print('Sector:', sector)
    print('Market Cap:', convert_market_cap(market_cap, currency_symbol))
    print('Current Market Price:', f"{currency_symbol}{market_price:,.2f}")
    print('Previous Day Close Price:', f"{currency_symbol}{previous_day_close:,.2f}")


    #Fetching & Plotting the closing price history of past 5 years of the stock:
    
    price_history = yf.Ticker(stock).history(period='5y', interval='1mo', actions=False)

    close_prices = price_history['Close']

    plt.plot(close_prices)
    plt.title(f"{stock} Price History")
    plt.xlabel("Date")
    plt.ylabel("Closing Price")
    plt.show()


except HTTPError:

    print(f"Invalid stock symbol or data not available for {stock}")




