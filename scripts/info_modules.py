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

    y['Date'] = y['Date'].dt.tz_localize(None)

    y['SMA50'] = y['Close'].rolling(50).mean()

    y['SMA100'] = y['Close'].rolling(100).mean()

    y['SMA200'] = y['Close'].rolling(200).mean()

    return y.to_feather(nombre)

def fred_info(name, series_id):

    import numpy as np
    import requests
    import pandas as pd
    from datetime import date

    with open('fred_key.txt', 'r') as file:

        fred_key_str = file.read().rstrip()

    url = 'https://api.stlouisfed.org/fred/series/observations?series_id=' + series_id + '&api_key=' + fred_key_str + '&file_type=json'

    r = requests.get(url)

    json_data = r.json()

    df_data = pd.json_normalize(json_data, record_path=['observations'])

    today = date.today()

    today = pd.to_datetime(today)

    df_data['date'] = pd.to_datetime(df_data['date'])

    start = df_data['date'].searchsorted('2012-01-01')

    end = df_data['date'].searchsorted(today)

    df_data = df_data.iloc[start:end]

    df_data = df_data.drop(columns=['realtime_start', 'realtime_end'])

    df_data['value'].replace('.', np.nan, inplace=True)

    df_data.dropna(subset=['value'], inplace=True)

    return df_data.to_excel(name + '.xlsx')

def fx_info(currency_1: str, currency_2: str, name: str):

    import pandas as pd
    import requests

    with open('av_key.txt', 'r') as file:

        av_key_str = file.read().rstrip()

    url = 'https://www.alphavantage.co/query?function=FX_DAILY&from_symbol=' + currency_1 + '&to_symbol=' + currency_2 + '&outputsize=full&apikey=' + av_key_str + '&datatype=json'

    param_headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"
                      }

    r = requests.get(url, headers=param_headers)

    data = r.json()

    data_df = pd.DataFrame(data['Time Series FX (Daily)']).T

    data_df.index.name = 'Date'

    data_df = data_df.rename(columns={'4. close': 'Close'})

    data_df.reset_index()

    data_df.sort_values(by='Date', inplace=True)

    return data_df.to_excel(name + '.xlsx')



#%%
