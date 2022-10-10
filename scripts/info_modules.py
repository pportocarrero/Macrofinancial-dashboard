#  Defining function to work with

import pandas as pd
import os
import platform
import requests_cache
import yfinance as yf

def working_folder(folder: str):

    if platform.system() == 'Windows':

        return os.chdir('C:/Users/pport/OneDrive/Projects/Macrofinancial-dashboard/' + folder + '/')

    if platform.system() == 'Darwin':

        return os.chdir('/Users/pportocarrero/OneDrive/Projects/Macrofinancial-dashboard/' + folder + '/')


def fin_inf(nombre, ticker, period, interval, group_by):

    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0'

    session = requests_cache.CachedSession('yfinance.cache')

    session.headers[user_agent] = 'financial_dashboard/1.0'

    y = yf.download(ticker, period=period, interval=interval, group_by=group_by)

    y.reset_index(level=0, inplace=True)

    y['SMA50'] = y['Close'].rolling(50).mean()

    y['SMA100'] = y['Close'].rolling(100).mean()

    y['SMA200'] = y['Close'].rolling(200).mean()

    return y.to_feather(nombre)

