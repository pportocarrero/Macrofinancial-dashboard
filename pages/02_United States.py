# IMPORT CONFIGURATIONS

import streamlit as st
# import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import os
# import hydralit_components as hc
# from plotly.subplots import make_subplots
import locale
import platform

st.set_page_config(
    layout='wide',
    page_title='Información de EE.UU.'
)

locale.setlocale(locale.LC_TIME, 'es_ES')

# register_plotly_resampler(mode="auto")

color_rojo = 'rgb(192,0,0)'
color_azul_oscuro = 'rgb(31,78,121)'
color_azul = 'rgb(0,112,192)'
color_celeste = 'rgb(5,148,185)'
color_gris = 'rgb(127,127,127)'
color_naranja = 'rgb(245,158,63)'
color_verde = 'rgb(147,194,73)'
color_negro = 'rgb(55,52,53)'
color_gris_oscuro = 'rgb(96,96,98)'
color_gris_claro = 'rgb(210,211,213)'
color_rojo_claro = 'rgb(237,50,55)'
color_celeste_claro = 'rgb(219,229,241)'
color_dorado = 'rgb(218,186,77)'
color_azul_gris = 'rgb(85,119,137)'
color_verde_oscuro = 'rgb(49,142,62)'
color_blanco = 'rgb(255,255,255)'

font_name = 'arial'
text_size = 14

# LOAD DATA

if platform.system() == 'Windows':

    os.chdir('C:/Users/pport/OneDrive/Projects/Macrofinancial-dashboard/')

if platform.system() == 'Darwin':

    os.chdir('/Users/pportocarrero/OneDrive/Projects/Macrofinancial-dashboard/')

# BASES DE EEUU

ust1m = pd.read_excel('mercados/ust1m.xlsx')  # US TREASURY 1 MONTH

ust3m = pd.read_excel('mercados/ust3m.xlsx')  # US TREASURY 3 MONTHS

ust6m = pd.read_excel('mercados/ust6m.xlsx')  # US TREASURY 6 MONTHS

ust1y = pd.read_excel('mercados/ust1y.xlsx')  # US TREASURY 1 YEAR

ust2y = pd.read_excel('mercados/ust2y.xlsx')  # US TREASURY 2 YEARS

ust3y = pd.read_excel('mercados/ust3y.xlsx')  # US TREASURY 3 YEARS

ust5y = pd.read_excel('mercados/ust5y.xlsx')  # US TREASURY 5 YEARS

ust7y = pd.read_excel('mercados/ust7y.xlsx')  # US TREASURY 7 YEARS

ust10y = pd.read_excel('mercados/ust10y.xlsx')  # US TREASURY 10 YEARS

ust20y = pd.read_excel('mercados/ust20y.xlsx')  # US TREASURY 20 YEARS

ust30y = pd.read_excel('mercados/ust30y.xlsx')  # US TREASURY 30 YEARS

ust_curve = pd.read_excel('mercados/ust_curve.xlsx')  # UST CURVE

us_gdp = pd.read_excel('mercados/us_gdp.xlsx')  # US QUATERLY GDP YOY

us_pce = pd.read_excel('mercados/us_pce.xlsx')  # US PCE INFLATION

us_core_pce = pd.read_excel('mercados/us_core_pce.xlsx')  # US CORE PCE INFLATION

fed_rate_upper = pd.read_excel('mercados/fed_rate_upper.xlsx')  # FEDERAL FUNDS RATE UPPER

fed_rate_lower = pd.read_excel('mercados/fed_rate_lower.xlsx')  # FEDERAL FUNDS RATE LOWER

############

# HEADER

st.title('Información macrofinanciera de Estados Unidos')

# RESUMEN

# DELTA PBI USA

us_gdp_latest = us_gdp['value'].iloc[-1]

us_gdp_t12 = us_gdp['value'].iloc[-13]

delta_us_gdp = us_gdp_latest - us_gdp_t12

us_gdp_latest = '{:,.2f}'.format(us_gdp_latest)

# DELTA INFLACIÓN PCE

us_pce_latest = us_pce['yoy_growth'].iloc[-1] * 100

delta_us_pce = us_pce_latest - 2.0

us_pce_latest = '{:,.2f}'.format(us_pce_latest)

# DELTA INFLACIÓN CORE PCE

us_pce_core_latest = us_core_pce['yoy_growth'].iloc[-1] * 100

delta_us_pce_core = us_pce_core_latest - 2.0

us_pce_core_latest = '{:,.2f}'.format(us_pce_core_latest)

# FED FEDERAL FUNDS RATE

fed_rate_upper_latest = fed_rate_upper['value'].iloc[-1]

fed_rate_upper_t2 = fed_rate_upper['value'].iloc[-30]

delta_fed_rate_upper = (fed_rate_upper_latest - fed_rate_upper_t2) * 100

fed_rate_upper_latest = '{:,.2f}'.format(fed_rate_upper_latest)

fed_rate_lower_latest = fed_rate_lower['value'].iloc[-1]

fed_rate_lower_t2 = fed_rate_lower['value'].iloc[-2]

delta_fed_rate_lower = fed_rate_lower_latest - fed_rate_lower_t2

fed_rate_lower_latest = '{:,.2f}'.format(fed_rate_lower_latest)

st.subheader('Resumen de indicadores clave')

us = st.columns(4)

us[0].metric(
    'Producto Bruto Interno',
    str(us_gdp_latest) + '% a/a',
    f'{delta_us_gdp:.2f}' + ' p.p. a/a'
)

us[1].metric(
    'Inflación PCE',
    str(us_pce_latest) + '% a/a',
    f'{delta_us_pce:.2f}' + ' p.p. sobre el objetivo (2%)',
    delta_color='inverse'
)

us[2].metric(
    'Inflación subyacente PCE',
    str(us_pce_core_latest) + '% a/a',
    f'{delta_us_pce_core:.2f}' + ' p.p. sobre el objetivo (2%)',
    delta_color='inverse'
)

us[3].metric(
    'Tasa de fondos federales de la Fed',
    str(fed_rate_lower_latest) + '-' + str(fed_rate_upper_latest) + '%',
    f'{delta_fed_rate_upper:.2f}' + ' puntos básicos m/m',
    delta_color='inverse'
)

# MAIN TABS

main_tabs = st.tabs(['Macroeconomía', 'Finanzas', 'Finanzas públicas', 'Indicadores avanzados'])

with main_tabs[0]:

    st.subheader('Macroeconomía')

    st.write('PBI EEUU')
    'FRED'

    st.write('Componentes del PBI')
    'FRED'

    st.write('**Inflación e inflación subyacente (PCE y CPI)**')
    'FRED'
    'PCE: PCEPI'
    'Core PCE: PCEPILFE'
    'CPI: USACPIALLMINMEI'
    'Core CPI: USACPICORMINMEI'

    st.write('Desempleo')
    'FRED'

    st.write('**Inventarios retail**')
    'https://fred.stlouisfed.org/series/RETAILIMSA'

with main_tabs[1]:

    st.subheader('Finanzas')

    st.write('Curva de treasury')
    'FRED'

    st.write('Rendimientos de los bonos')
    'FRED'

    st.write('Spread de 3m-10 años')
    'FRED'

    st.write('Spread 2-10 años')
    'FRED'

    st.write('Federal Funds Rate (upper and lower bound, también incluir la tasa real)')
    'FRED'

    st.write('Fed dot plots')
    'FRED'

with main_tabs[2]:

    st.subheader('Finanzas públicas')

    st.write('**Federal Reserve Balance Sheet**')
    'https://fred.stlouisfed.org/series/WALCL'

    st.write('**Deuda de EEUU**')

with main_tabs[3]:

    st.subheader('Indicadores adelantados')

    st.write('Nóminas no agrícolas')
    'FRED'

    st.write('Peticiones iniciales de desempleo')
    'FRED'

    st.write('Peticiones continuas de desempleo')
    'FRED'

    st.write('Probabilidad de recesión de NY Fed')
    'Federal Reserve Bank of New York'
    'https://www.newyorkfed.org/research/capital_markets/ycfaq#/interactive'

    st.write('Empire State Manufacturing Survey')
    'Federal Reserve Bank of New York'
    'https://www.newyorkfed.org/survey/empire/empiresurvey_overview'

    st.write('GDPNow Proyección de GDP de la Federal Reserve Bank of Atlanta')
    'Federal Reserve Bank of Atlanta'
