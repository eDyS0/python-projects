"""
Quote Tracker (market symbols etc) –
A program which can go out and check the current value of stocks for a list of symbols entered by the user.
Gets its data from googlefinance api.
Work still in progress -> save every value and compare with the new ones to check if the market has changed since last time.
"""

from googlefinance import getQuotes
import json
import sys

def get_data(symbols):
    sid = ''                #stock symbol
    value = ''
    dic_symbols = {}
    list_symbols = []
    [list_symbols.append(symbol) for symbol in symbols]
    try:
        result = json.dumps(getQuotes(list_symbols), indent=2).split(' ')
        
        for n, i in enumerate(result):  #add every symbol and its value to a dic
            if i == '"StockSymbol":':
                sid = result[n+1][:-2]
            if i == '"LastTradePrice":':
                value = result[n+1][:-2]
                dic_symbols[sid] = value
        print(dic_symbols)
    except:
        print('The program has encountered an error, verify your symbols.', file=sys.stderr)

def main():
    if len(sys.argv) > 1:
        get_data(sys.argv[1:])
    else:
        print("Usage: python quotetracker.py <symbol>", file=sys.stderr)
        
if __name__ == "__main__":
    main()
