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

# BASES DEL RESUMEN

sp_500 = pd.read_feather('mercados/sp_500')  # S&P 500

# sp_500_intraday = pd.read_feather('mercados/sp_500_intraday')  # S&P 500 INTRADAY

dji_index = pd.read_feather('mercados/dji_index')  # DOW JONES

nasdaq_100 = pd.read_feather('mercados/nasdaq_100')  # NASDAQ 100

russell_2000 = pd.read_feather('mercados/russell_2000')  # RUSSELL 2000

russell_3000 = pd.read_feather('mercados/russell_3000')  # RUSSELL 3000

ftse_100 = pd.read_feather('mercados/ftse_100')  # FTSE 100

nikkei_225 = pd.read_feather('mercados/nikkei_225')  # NIKKEI 225

shanghai_comp = pd.read_feather('mercados/shanghai_comp')  # SHANGHAI COMPOSITE

vix_index = pd.read_feather('mercados/vix_index')  # VIX

move_index = pd.read_feather('mercados/move_index')  # MOVE Index

bvl_gen = pd.read_excel("mercados/bvl_gen.xlsx")  # ÍNDICE GENERAL DE LA BVL

wti_crude = pd.read_feather('mercados/wti_crude')  # WTI CRUDE

brent_crude = pd.read_feather('mercados/brent_crude')  # BRENT CRUDE

copper_fut = pd.read_feather('mercados/copper_futures')  # COPPER FUTURES

gold_fut = pd.read_feather('mercados/gold_futures')  # GOLD FUTURES

silver_fut = pd.read_feather('mercados/silver_futures')  # SILVER FUTURES

wheat_fut = pd.read_feather('mercados/wheat_futures')  # WHEAT FUTURES

soybean_fut = pd.read_feather('mercados/soybean_futures')  # SOYBEAN FUTURES

corn_fut = pd.read_feather('mercados/corn_futures')  # CORN FUTURES

usd_pen = pd.read_excel('mercados/usd_pen.xlsx')  # USD/PEN

# BASES DE EEUU

# BASES DE PERÚ

pbi_peru = pd.read_feather('mercados/pbi_peru')  # PBI PERÚ

pbi_peru_des = pd.read_feather('mercados/pbi_peru_des')  # PBI PERÚ DESESTACIONALIZADO

pbi_peru_des_prom = pd.read_feather('mercados/pbi_peru_des_prom')  # PBI PERÚ DESESTACIONALIZADO PROMEDIO MÓVIL 3 MESES

exp_pbi_peru = pd.read_feather('mercados/expectativas_pbi_peru')  # EXPECTATIVAS PBI PERÚ

inflacion_peru = pd.read_feather('mercados/inflacion_peru')  # INFLACIÓN PERÚ

inflacion_peru_sub = pd.read_feather('mercados/inflacion_peru_sub')  # INFLACIÓN PERÚ SIN ALIMENTOS Y ENERGÍA

inflacion_peru_exp = pd.read_feather('mercados/inflacion_peru_exp')  # EXPECTATIVAS DE INFLACION A 12 MESES

tasa_bcrp = pd.read_feather('mercados/tasa_bcrp')  # TASA DE REFERENCIA DEL BCRP

exp_eco_3m = pd.read_feather('mercados/expectativas_eco_3m')  # EXPECTATIVAS DE LA ECONOMÍA A 3 MESES

exp_eco_12m = pd.read_feather('mercados/expectativas_eco_12m')  # EXPECTATIVAS DE LA ECONOMÍA A 12 MESES

# HEADER

st.title('Información macrofinanciera de Estados Unidos')


# RESUMEN

# ESTADOS UNIDOS

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
