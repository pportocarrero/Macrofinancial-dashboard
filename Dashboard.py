# IMPORT CONFIGURATIONS

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import os
# import hydralit_components as hc
# from plotly.subplots import make_subplots
# from plotly_resampler import register_plotly_resampler
import platform
from io import BytesIO
# from pyxlsb import open_workbook as open_xlsb

st.set_page_config(
    layout='wide',
    page_title='Macrofinancial conditions',
    page_icon=''
)

@st.cache_data
def working_dir(folder='Macrofinancial-dashboard'):

    if platform.system() == 'Windows':

        return os.chdir('C:/Users/pport/OneDrive/Projects/' + folder)

    elif platform.system() == 'Darwin':

        return os.chdir('/Users/pportocarrero/OneDrive/Projects/' + folder)


def load_data(filename: str, format='feather'):

    if format == 'excel':

        return pd.read_excel(filename + '.xlsx')
    
    if format == 'feather':

        return pd.read_feather(filename)


# FIRE UP MARKET DATA

sp_500 = load_data('mercados/sp_500')  # S&P 500

dji_index = load_data('mercados/dji_index')  # DOW JONES

nasdaq_comp = load_data('mercados/nasdaq_comp')  # NASDAQ COMPOSITE

russell_2000 = load_data('mercados/russell_2000')  # RUSSELL 2000

russell_3000 = load_data('mercados/russell_3000')  # RUSSELL 3000

ftse_100 = load_data('mercados/ftse_100')  # FTSE 100

nikkei_225 = load_data('mercados/nikkei_225')  # NIKKEI 225

shanghai_comp = load_data('mercados/shanghai_comp')  # SHANGHAI COMPOSITE

vix_index = load_data('mercados/vix_index')  # VIX

move_index = load_data('mercados/move_index')  # MOVE Index

bvl_gen = load_data('mercados/bvl_gen', format='excel')  # ÍNDICE GENERAL DE LA BVL

wti_crude = load_data('mercados/wti_crude')  # WTI CRUDE

brent_crude = load_data('mercados/brent_crude')  # BRENT CRUDE

copper_fut = load_data('mercados/copper_futures')  # COPPER FUTURES

gold_fut = load_data('mercados/gold_futures')  # GOLD FUTURES

silver_fut = load_data('mercados/silver_futures')  # SILVER FUTURES

wheat_fut = load_data('mercados/wheat_futures')  # WHEAT FUTURES

soybean_fut = load_data('mercados/soybean_futures')  # SOYBEAN FUTURES

corn_fut = load_data('mercados/corn_futures')  # CORN FUTURES

gscpi = load_data('mercados/gscpi_data')  # GLOBAL SUPPLY CHAIN PRESSURE INDEX

usd_pen = load_data('mercados/usd_pen', format='excel')  # USD/PEN

# USA DATA

ust1m = load_data('mercados/ust1m', format='excel')  # US TREASURY 1 MONTH

ust3m = load_data('mercados/ust3m', format='excel')  # US TREASURY 3 MONTHS

ust6m = load_data('mercados/ust6m', format='excel')  # US TREASURY 6 MONTHS

ust1y = load_data('mercados/ust1y', format='excel')  # US TREASURY 1 YEAR

ust2y = load_data('mercados/ust2y', format='excel')  # US TREASURY 2 YEARS

ust3y = load_data('mercados/ust3y', format='excel')  # US TREASURY 3 YEARS

ust5y = load_data('mercados/ust5y', format='excel')  # US TREASURY 5 YEARS

ust7y = load_data('mercados/ust7y', format='excel')  # US TREASURY 7 YEARS

ust10y = load_data('mercados/ust10y', format='excel')  # US TREASURY 10 YEARS

ust20y = load_data('mercados/ust20y', format='excel')  # US TREASURY 20 YEARS

ust30y = load_data('mercados/ust30y', format='excel')  # US TREASURY 30 YEARS

ust_curve = load_data('mercados/ust_curve', format='excel')  # UST CURVE

us_gdp = load_data('mercados/us_gdp', format='excel')  # US QUATERLY GDP YOY

us_pce = load_data('mercados/us_pce', format='excel')  # US PCE INFLATION

us_core_pce = load_data('mercados/us_core_pce', format='excel')  # US CORE PCE INFLATION

fed_rate_upper = load_data('mercados/fed_rate_upper', format='excel')  # FEDERAL FUNDS RATE UPPER

fed_rate_lower = load_data('mercados/fed_rate_lower', format='excel')  # FEDERAL FUNDS RATE LOWER

# PERU DATA

bvl_gen = load_data('mercados/bvl_gen')  # ÍNDICE GENERAL DE LA BVL

pbi_peru = load_data('mercados/pbi_peru')  # PBI PERÚ

pbi_peru_des = load_data('mercados/pbi_peru_des')  # PBI PERÚ DESESTACIONALIZADO

pbi_peru_des_prom = load_data('mercados/pbi_peru_des_prom')  # PBI PERÚ DESESTACIONALIZADO PROMEDIO MÓVIL 3 MESES

exp_pbi_peru = load_data('mercados/expectativas_pbi_peru')  # EXPECTATIVAS PBI PERÚ

inflacion_peru = load_data('mercados/inflacion_peru')  # INFLACIÓN PERÚ

inflacion_peru_sub = load_data('mercados/inflacion_peru_sub')  # INFLACIÓN PERÚ SIN ALIMENTOS Y ENERGÍA

inflacion_peru_exp = load_data('mercados/inflacion_peru_exp')  # EXPECTATIVAS DE INFLACION A 12 MESES

tasa_bcrp = load_data('mercados/tasa_bcrp')  # TASA DE REFERENCIA DEL BCRP

exp_eco_3m = load_data('mercados/expectativas_eco_3m')  # EXPECTATIVAS DE LA ECONOMÍA A 3 MESES

exp_eco_12m = load_data('mercados/expectativas_eco_12m')  # EXPECTATIVAS DE LA ECONOMÍA A 12 MESES

# COLORS AND CONFIGS

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
color_transparente = 'rgba(0,0,0,0)'
color_bloomberg = 'rgb(255,160,40)'
bl_colors = ['#1d6a9c', '#2a9c68', '#9c2a2a', '#9c812a', '#6c2a9c']

font_name = 'arial'
text_size = 14

# SIDEBAR


# FUNCIONES

def delta_2d(dataframe):

    latest = dataframe['Close'].iloc[-1]

    t2 = dataframe['Close'].iloc[-2]

    delta = latest - t2

    delta_pct = latest / t2 - 1

    latest = '{:,.2f}'.format(latest)

    delta = '{:,.2f}'.format(delta)

    delta_pct = '{:,.2%}'.format(delta_pct)

    return latest, delta, delta_pct

#####################

def delta_4d(dataframe):

    latest = dataframe['Close'].iloc[-1]

    t2 = dataframe['Close'].iloc[-2]

    delta = latest - t2

    delta_pct = latest / t2 - 1

    latest = '{:,.4f}'.format(latest)

    delta = '{:,.4f}'.format(delta)

    delta_pct = '{:,.2%}'.format(delta_pct)

    return latest, delta, delta_pct

#####################

def delta_1y(dataframe):

    latest = dataframe.iloc[-1]

    t2 = dataframe.iloc[-13]

    delta = latest - t2

    delta_pct = latest / t2 - 1

    latest = '{:,.2f}'.format(latest)

    delta = '{:,.2f}'.format(delta)

    delta_pct = '{:,.2%}'.format(delta_pct)

    return latest, delta, delta_pct

############
def delta_1d(dataframe):

    latest = dataframe.iloc[-1]

    t2 = dataframe.iloc[-2]

    delta = latest - t2

    delta_pct = latest / t2 - 1

    latest = '{:,.2f}'.format(latest)

    delta = '{:,.2f}'.format(delta)

    delta_pct = '{:,.2%}'.format(delta_pct)

    return latest, delta, delta_pct

############


# MAIN TABS

st.title('Macrofinancial information')

tabs1 = st.tabs(['Summary', 'United States', 'Peru', 'News'])

with tabs1[0]:

    # RESUMEN

    st.subheader('Summary of financial information')

    # DELTA DEL S&P 500

    sp_500_delta = delta_2d(sp_500)

    # DELTA DOW JONES

    dji_delta = delta_2d(dji_index)

    # DELTA NASDAQ COMPOSITE

    nasdaq_delta = delta_2d(nasdaq_comp)

    # DELTA VIX

    vix_delta = delta_2d(vix_index)

    # DELTA MOVE

    move_delta = delta_2d(move_index)

    # DELTA WTI CRUDE

    wti_delta = delta_2d(wti_crude)

    # DELTA COPPER

    copper_delta = delta_4d(copper_fut)

    # DELTA USD/PEN

    usd_pen_delta = delta_4d(usd_pen)

    # KPI's

    kpi1 = st.columns(4)

    kpi1[0].metric(
        'S&P 500',
        str(sp_500_delta[0]) + ' pts',
        str(sp_500_delta[2]) + ' (' + str(sp_500_delta[1].replace('.', ',')) + ' pts)'
    )

    kpi1[1].metric(
        'Dow Jones 30',
        str(dji_delta[0]) + ' pts',
        str(dji_delta[2]) + ' (' + str(dji_delta[1].replace('.', ',')) + ' pts)'
    )

    kpi1[2].metric(
        'Nasdaq Composite',
        str(nasdaq_delta[0]) + ' pts',
        str(nasdaq_delta[2]) + ' (' + str(nasdaq_delta[1].replace('.', ',')) + ' pts)'
    )

    kpi1[3].metric(
        'WTI Crude',
        'US$ ' + str(wti_delta[0]),
        str(wti_delta[2]) + ' (US$ ' + str(wti_delta[1].replace('.', ',')) + ')'
    )

    kpi2 = st.columns(4)

    kpi2[0].metric(
        'VIX volatility index',
        'US$ ' + str(vix_delta[0]),
        str(vix_delta[2]) + ' (US$ ' + str(vix_delta[1]).replace('.', ',') + ')',
        delta_color='inverse'
    )

    kpi2[1].metric(
        'MOVE volatility index',
        'US$ ' + str(move_delta[0]),
        str(move_delta[2]) + ' (US$ ' + str(move_delta[1]).replace('.', ',') + ')',
        delta_color='inverse'
    )

    kpi2[2].metric(
        'Copper',
        'US$ ' + str(copper_delta[0]),
        str(copper_delta[2]) + ' (US$ ' + str(copper_delta[1]).replace('.', ',') + ')'
    )

    kpi2[3].metric(
        'USD/PEN',
        'S/ ' + str(usd_pen_delta[0]),
        str(usd_pen_delta[2]) + ' (S/ ' + usd_pen_delta[1].replace('.', ',') + ')',
        delta_color='inverse'
    )

    ###########

    # FUNCTION TO CREATE AREA CHART
    def line_chart(name, ticker_id, y_axis, decimals, us_recession=False):

        import plotly.graph_objects as go

        import streamlit as st

        colors = ["#1d6a9c", "#2a8ab8", "#3b8fad"]

        if us_recession is True:

            fig = go.Figure()

            fig.add_trace(
                go.Scatter(
                    name=name,
                    x=ticker_id['Date'],
                    y=ticker_id['Close'],
                    line=dict(color=bl_colors[0]),
                    fill='tozeroy'
                )
            )

            fig.add_vrect(
                x0='2020-02-01',
                x1='2020-04-01',
                fillcolor='rgb(127,127,127)',
                opacity=0.25,
                line_width=0
            )

            fig.update_layout(
                {'plot_bgcolor': color_transparente, 'paper_bgcolor': color_transparente},
                margin=dict(l=0, r=0, t=0, b=0),
                hovermode='x unified',
                yaxis=dict(tickformat=',.' + str(decimals) + 'f'),
                hoverlabel=dict(bgcolor='white', font_size=14, font_family='arial',font_color='black'),
                xaxis_rangeselector_font_color='white',
                xaxis_rangeselector_activecolor=bl_colors[0],
                xaxis_rangeselector_bgcolor=color_transparente
            )

            fig.update_xaxes(
                rangebreaks=[dict(bounds=["sat", "mon"])],
                rangeselector=dict(
                    buttons=list([
                        dict(count=3, label='3D', step='day', stepmode='backward'),
                        dict(count=1, label='1M', step='month', stepmode='backward'),
                        dict(count=3, label='3M', step='month', stepmode='backward'),
                        dict(count=6, label='6M', step='month', stepmode='backward'),
                        dict(count=1, label='YTD', step='year', stepmode='todate'),
                        dict(count=1, label='1A', step='year', stepmode='backward'),
                        dict(label='MAX', step='all')
                    ]))
            )

            fig.update_yaxes(title_text=y_axis)

            return st.plotly_chart(fig, use_container_width=True)

        elif us_recession is False:

            fig = go.Figure()

            fig.add_trace(
                go.Scatter(
                    name=name,
                    x=ticker_id['Date'],
                    y=ticker_id['Close'],
                    line=dict(color=bl_colors[0]),
                    fill='tozeroy'
                )
            )

            fig.update_layout(
                {'plot_bgcolor': color_transparente, 'paper_bgcolor': color_transparente},
                margin=dict(l=0, r=0, t=0, b=0),
                hovermode='x unified',
                hoverlabel=dict(bgcolor='white', font_size=14, font_family='arial', font_color='black'),
                yaxis=dict(tickformat=',.' + str(decimals) + 'f'),
                xaxis_rangeselector_font_color='white',
                xaxis_rangeselector_activecolor=bl_colors[0],
                xaxis_rangeselector_bgcolor=color_transparente
            )

            fig.update_xaxes(
                rangebreaks=[dict(bounds=["sat", "mon"])],
                rangeselector=dict(
                    buttons=list([
                        dict(count=3, label='3D', step='day', stepmode='backward'),
                        dict(count=1, label='1M', step='month', stepmode='backward'),
                        dict(count=3, label='3M', step='month', stepmode='backward'),
                        dict(count=6, label='6M', step='month', stepmode='backward'),
                        dict(count=1, label='YTD', step='year', stepmode='todate'),
                        dict(count=1, label='1Y', step='year', stepmode='backward'),
                        dict(label='MAX', step='all')
                    ])),
                    rangeslider=dict(visible=True)
            )

            fig.update_yaxes(title_text=y_axis)

            return st.plotly_chart(fig, use_container_width=True)

    ###########

    # CREATE FUNCTION FOR CANDLESTICK CHARTS

    def olhc_chart(name, ticker_id, decimals, us_recession=False):

        import plotly.graph_objects as go

        from plotly.subplots import make_subplots

        import streamlit as st

        if us_recession is True:

            fig = make_subplots(
                rows=2,
                cols=1,
                shared_xaxes=True,
                vertical_spacing=0.03,
                row_width=[0.2, 0.7]
            )

            fig.add_trace(
                go.Candlestick(
                    x=ticker_id['Date'],
                    open=ticker_id['Open'],
                    high=ticker_id['High'],
                    low=ticker_id['Low'],
                    close=ticker_id['Close'],
                    name=name,
                    increasing_line_color=bl_colors[1],
                    decreasing_line_color=bl_colors[2],
                    showlegend=False
                ),
                row=1,
                col=1
            )

            fig.add_trace(
                go.Scatter(
                    name='SMA(50)',
                    x=ticker_id['Date'],
                    y=ticker_id['SMA50'],
                    mode='lines',
                    showlegend=True
                ),
                row=1,
                col=1
            )

            fig.add_trace(
                go.Scatter(
                    name='SMA(100)',
                    x=ticker_id['Date'],
                    y=ticker_id['SMA100'],
                    mode='lines',
                    showlegend=True
                ),
                row=1,
                col=1
            )

            fig.add_trace(
                go.Scatter(
                    name='SMA(200)',
                    x=ticker_id['Date'],
                    y=ticker_id['SMA200'],
                    mode='lines',
                    showlegend=True
                ),
                row=1,
                col=1
            )

            fig.add_trace(
                go.Bar(
                    x=ticker_id['Date'],
                    y=ticker_id['Volume'],
                    showlegend=False,
                    name='Volume'
                ),
                row=2,
                col=1
            )

            fig.add_vrect(
                x0='2020-02-01',
                x1='2020-04-01',
                fillcolor='rgb(127,127,127)',
                opacity=0.25,
                line_width=0
            )

            fig.update(layout_xaxis_rangeslider_visible=False)

            fig.update_layout(
                {'plot_bgcolor': color_transparente, 'paper_bgcolor': color_transparente},
                margin=dict(l=0, r=0, t=0, b=0),
                hovermode='x unified',
                yaxis=dict(tickformat=',.' + str(decimals) + 'f'),
                hoverlabel=dict(bgcolor='white', font_size=14, font_family='arial', font_color='black'),
                xaxis_rangeselector_font_color='white',
                xaxis_rangeselector_activecolor=bl_colors[0],
                xaxis_rangeselector_bgcolor=color_transparente
            )

            fig.update_xaxes(
                rangebreaks=[dict(bounds=["sat", "mon"])],
                rangeselector=dict(
                    buttons=list([
                        dict(count=3, label='3D', step='day', stepmode='backward'),
                        dict(count=1, label='1M', step='month', stepmode='backward'),
                        dict(count=3, label='3M', step='month', stepmode='backward'),
                        dict(count=6, label='6M', step='month', stepmode='backward'),
                        dict(count=1, label='YTD', step='year', stepmode='todate'),
                        dict(count=1, label='1Y', step='year', stepmode='backward'),
                        dict(label='MAX', step='all')
                    ]))
            )

            return st.plotly_chart(fig, use_container_width=True)

        elif us_recession is False:

            fig = make_subplots(
                rows=2,
                cols=1,
                shared_xaxes=True,
                vertical_spacing=0.03,
                row_width=[0.2, 0.7]
            )

            fig.add_trace(
                go.Candlestick(
                    x=ticker_id['Date'],
                    open=ticker_id['Open'],
                    high=ticker_id['High'],
                    low=ticker_id['Low'],
                    close=ticker_id['Close'],
                    name=name,
                    increasing_line_color=bl_colors[1],
                    decreasing_line_color=bl_colors[2],
                    showlegend=False
                ),
                row=1,
                col=1
            )

            fig.add_trace(
                go.Scatter(
                    name='SMA(50)',
                    x=ticker_id['Date'],
                    y=ticker_id['SMA50'],
                    mode='lines',
                    showlegend=True
                ),
                row=1,
                col=1
            )

            fig.add_trace(
                go.Scatter(
                    name='SMA(100)',
                    x=ticker_id['Date'],
                    y=ticker_id['SMA100'],
                    mode='lines',
                    showlegend=True
                ),
                row=1,
                col=1
            )

            fig.add_trace(
                go.Scatter(
                    name='SMA(200)',
                    x=ticker_id['Date'],
                    y=ticker_id['SMA200'],
                    mode='lines',
                    showlegend=True
                ),
                row=1,
                col=1
            )

            fig.add_trace(
                go.Bar(
                    x=ticker_id['Date'],
                    y=ticker_id['Volume'],
                    showlegend=False,
                    name='Volume'
                ),
                row=2,
                col=1
            )

            fig.update(layout_xaxis_rangeslider_visible=False)

            fig.update_layout(
                {'plot_bgcolor': color_transparente, 'paper_bgcolor': color_transparente},
                margin=dict(l=0, r=0, t=0, b=0),
                hovermode='x unified',
                yaxis=dict(tickformat=',.' + str(decimals) + 'f'),
                hoverlabel=dict(bgcolor='white', font_size=14, font_family='arial', font_color='black'),
                xaxis_rangeselector_font_color='white',
                xaxis_rangeselector_activecolor=bl_colors[0],
                xaxis_rangeselector_bgcolor=color_transparente
            )

            fig.update_xaxes(
                rangebreaks=[dict(bounds=["sat", "mon"])],
                rangeselector=dict(
                    buttons=list([
                        dict(count=3, label='3D', step='day', stepmode='backward'),
                        dict(count=1, label='1M', step='month', stepmode='backward'),
                        dict(count=3, label='3M', step='month', stepmode='backward'),
                        dict(count=6, label='6M', step='month', stepmode='backward'),
                        dict(count=1, label='YTD', step='year', stepmode='todate'),
                        dict(count=1, label='1Y', step='year', stepmode='backward'),
                        dict(label='MAX', step='all')
                    ]))
            )

            return st.plotly_chart(fig, use_container_width=True)

    ###########

    def two_chart(name: str, data_frame, y_axis, decimals, us_recession=False):

        st.markdown('**' + name + '**')

        chart = st.selectbox('Select the type of chart', ('Line chart', 'OHLC chart + Volume'), key=name)

        if chart == 'Line chart':

            tab0 = st.tabs(['Chart', 'Dataset', 'Download'])

            with tab0[0]:

                line_chart(name, data_frame, y_axis, decimals, us_recession=False)

            with tab0[1]:

                st.dataframe(data_frame)

            with tab0[2]:

                def to_excel(data_frame):

                    output = BytesIO()

                    writer = pd.ExcelWriter(output, engine='xlsxwriter')

                    data_frame.to_excel(writer, index=False, sheet_name='Hoja1')

                    workbook = writer.book

                    worksheet = writer.sheets['Hoja1']

                    format1 = workbook.add_format({'num_format': '0.00'})

                    worksheet.set_column('A:A', None, format1)

                    writer.save()

                    processed_data = output.getvalue()

                    return processed_data

                df_xlsx = to_excel(data_frame)

                st.download_button(
                    label='Download data',
                    data=df_xlsx,
                    file_name=name + '.xlsx'
                )

        elif chart == 'OHLC chart + Volume':

            tab1 = st.tabs(['Chart', 'Dataset', 'Download'])

            with tab1[0]:

                olhc_chart(name, data_frame, decimals, us_recession=False)

            with tab1[1]:

                st.dataframe(data_frame)

            with tab1[2]:

                def to_excel(data_frame):

                    output = BytesIO()

                    writer = pd.ExcelWriter(output, engine='xlsxwriter')

                    data_frame.to_excel(writer, index=False, sheet_name='Hoja1')

                    workbook = writer.book

                    worksheet = writer.sheets['Hoja1']

                    format1 = workbook.add_format({'num_format': '0.00'})

                    worksheet.set_column('A:A', None, format1)

                    writer.save()

                    processed_data = output.getvalue()

                    return processed_data

                df_xlsx = to_excel(data_frame)

                st.download_button(
                    label='Download data',
                    data=df_xlsx,
                    file_name=name + '.xlsx'
                )


    ###########

    # ÍNDICES BURSÁTILES Y DE RENTA FIJA

    main_tabs = st.tabs(['Equities', 'Fixed income', 'Commodities', 'Currencies'])  # AÑADIR UN EQUITY SNAPSHOT POR SECTOR DEL S&P 500 EN BASE AL CRECIMIENTO DE ACA ACCIÓN

    with main_tabs[0]:

        st.subheader('Equities')

        # S&P 500 y DJI

        eq = st.columns(2)

        with eq[0]:

            two_chart('S&P 500', sp_500, 'Points', decimals=0, us_recession=True)

            with st.expander('More information:'):

                st.write('''
                Source: Yahoo! Finance.
                    
                El índice S&P 500 es considerado como el mejor barómetro de las compañías de alta capitalización en Estados Unidos. El índice incluye 500 compañías públicas de diferentes sectores de la economía y cubre aproximadamente el 80% del total de capitalización de mercado disponible. El S&P 500 es un índice bursátil ponderado en base a la capitalización de mercado de las compañías que la componen. De acuerdo a la Encuesta anual de activos, se estima que US$ 13 billones están indexados o comparados a este índice.
                ''')

        with eq[1]:

            two_chart('Dow Jones Industrial Average', dji_index, 'Points', decimals=0, us_recession=True)

            with st.expander('More information:'):

                st.write('''
                Source: Yahoo! Finance.
        
                El Dow Jones Industrial Average es un indicador ponderado por el precio de 30 compañías 'blue-chip' norteamericanas. Este índice cubre todas las industrias con la excepción de transportes y servicios públicos.
                ''')

        eq1 = st.columns(2)

        with eq1[0]:

            two_chart('Nasdaq Composite', nasdaq_comp, 'Points', decimals=0, us_recession=True)

            with st.expander('More information:'):

                st.write('''
                Source: Yahoo! Finance.
                    
                El Nasdaq Composite es un índice basado en una canasta de 100 acciones de las empresas que más actividad tienen en la bolsa de valores Nasdaq. El índice incluye empresas de varios sectores, a excepción de las financieras. El índice se calcula en base a la ponderación de la capitalización de las empresas.
                ''')

        with eq1[1]:

            two_chart('Russell 3000', russell_3000, 'Points', decimals=0, us_recession=True)

            with st.expander('More information:'):

                st.write('''
                Source: Yahoo! Finance.
        
                Por su parte, el índice Russell 3000 es un índice bursátil ponderado por capitalización de mercado que provee exposición a todo el mercado bursátil norteamericano. Este índice sigue el desempeño de las 3 mil empresas norteamericanas públicas con mayor capitalización en el mercado, que representa el 97% de todas las empresas incorporadas en EE.UU. que cotizan en el mercado bursátil norteamericano.
                ''')

        eq3, eq4 = st.columns(2)

        with eq3:

            two_chart('Russell 2000', russell_2000, 'Points', decimals=0, us_recession=True)

            with st.expander('More information:'):

                st.write('''
                Source: Yahoo! Finance
        
                El índice Russell 2000 se refiere a un indice bursátil que mide el desempeño de las 2,000 compañías más pequeñas que forman parte del índice Russell 3000. Este índice es administrado por FTSE Russell y es considerado uno de los referentes de la salud de la economía norteamericana por su énfasis en compañías públicas pequeñas del mercado norteamericnano.
                ''')

        with eq4:

            two_chart('FTSE 100', ftse_100, 'Points', decimals=0, us_recession=False)

            with st.expander('More information'):

                st.write('''
                Source: Yahoo! Finance.
        
                El FTSE 100 es un índice bursátil de las 100 empresas que cotizan en el London Stock Exchange con la mayor capitalización de mercado.El índice es mantenido por el Grupo FTSE, una subsidiaria del Grupo London Stock Exchange.
                ''')

        # VIX y FTSE 100

        eq5 = st.columns(2)

        with eq5[0]:

            two_chart('CBOE VIX volatility index', vix_index, 'US$', decimals=1, us_recession=True)

            with st.expander('More information'):

                st.write('''
                Source: Yahoo! Finance.
        
                El índice VIX es una estimación destinada a producir una medida constante de la volatilidad esperada a 30 días del mercado bursátil norteamericano. Esta medida se deriva del precio "mid" de opciones call y put del índice S&P 500 a tiempo real. A nivel global, es una de las medidas de volatilidad más importantes -- ampliamente citada y seguida por medios especializados, así como por participantes del mercado como un indicador de seguimiento.
                ''')

        with eq5[1]:

            two_chart('BofA MOVE volatility index', move_index, 'US$', decimals=1, us_recession=True)

            with st.expander('More information'):

                st.write('''
                Source: Yahoo! Finance.
        
                El índice MOVE es una reconocida medida de la volatilidad de tasas de interés en EE.UU. que sigue el movimiento de la volatilidad implícita del rendimiento de instrumentos del Tesoro norteamericano a través de los precios vigentes de opciones a 1 mes de bonos del Tesoro norteamericano a 2, 5, 10 y 30 años.
        
                Es una media ponderada del rendimiento constante a 2, 5, 10 y 30 años de los bonos del Tesoro norteamericano con los siguientes pesos: 20%, 20%, 40% y 20%, respectivamente.
                ''')

        eq6 = st.columns(2)

        with eq6[0]:

            two_chart('Shanghai Composite', shanghai_comp, 'Points', decimals=0, us_recession=False)

            with st.expander('More information'):
                st.write('''
                Source: Yahoo! Finance.
        
                The SSE Composite Index also known as SSE Index is a stock market index of all stocks that are traded at the Shanghai Stock Exchange.
                ''')

        with eq6[1]:

            two_chart('Nikkei 225', nikkei_225, 'Points', decimals=1, us_recession=False)

            with st.expander('More information'):

                st.write('''
                Source: Banco Central de Reserva del Perú.
        
                El índice Nikkei 225 is a stock market index for the Tokyo Stock Exchange. It has been calculated daily by the Nihon Keizai Shimbun newspaper since 1950.
                ''')

        # SHANGHAI Y NIKKEI 225

        eq7, eq8 = st.columns(2)

        with eq7:

            st.write('**S&P/BVL Peru General**')

            tab0 = st.tabs(['Chart', 'Dataset', 'Download'])

            with tab0[0]:

                line_chart('S&P/BVL Peru General', bvl_gen, 'Points', decimals=0, us_recession=False)

            with tab0[1]:

                st.dataframe(bvl_gen)

            with tab0[2]:
                def to_excel(data_frame):
                    output = BytesIO()

                    writer = pd.ExcelWriter(output, engine='xlsxwriter')

                    data_frame.to_excel(writer, index=False, sheet_name='Hoja1')

                    workbook = writer.book

                    worksheet = writer.sheets['Hoja1']

                    format1 = workbook.add_format({'num_format': '0.00'})

                    worksheet.set_column('A:A', None, format1)

                    writer.save()

                    processed_data = output.getvalue()

                    return processed_data


                df_xlsx = to_excel(bvl_gen)

                st.download_button(
                    label='Download data',
                    data=df_xlsx,
                    file_name='bvl_gen.xlsx'
                )

            with st.expander('More information'):

                st.write('''
                Source: Standard & Poor's.
                ''')

    with main_tabs[1]:

    # MATERIAS PRIMAS

        st.subheader('Commodities')

        # CRUDOS WTI Y BRENT

        com1, com2 = st.columns(2)

        with com1:

            two_chart('WTI Crude (US$/bl)', wti_crude, 'US$', decimals=2, us_recession=True)

            with st.expander('More information'):
                st.write('''
                    Source: Yahoo! Finance.
                        
                    WTI is the underlying commodity of the New York Mercantile Exchange's (NYMEX) oil futures contract and is considered a high-quality oil that is easily refined.
                        
                    West Texas Intermediate (WTI) crude oil is a specific grade of crude oil and one of the main three benchmarks in oil pricing, along with Brent and Dubai Crude. WTI is known as a light sweet oil because it contains between 0.24% and 0.34% sulfur, making it "sweet," and has a low density (specific gravity), making it "light."
                    ''')

        with com2:

            two_chart('Brent Crude (US$/bl)', brent_crude, 'US$', decimals=2, us_recession=True)

            with st.expander('More information'):

                st.write('''
                        Source: Yahoo! Finance.
                        
                        Brent actually refers to oil from four different fields in the North Sea: Brent, Forties, Oseberg, and Ekofisk. Crude from this region is light and sweet, making them ideal for the refining of diesel fuel, gasoline, and other high-demand products. And because the supply is waterborne, it’s easy to transport to distant locations.
                        ''')

        # COBRE Y ORO

        comm1 = st.columns(2)

        with comm1[0]:

            two_chart('Copper (US$/lb)', copper_fut, 'US$', decimals=2, us_recession=True)

            with st.expander('More information)'):

                st.write('''
                    Source: Yahoo! Finance.
                    ''')

        with comm1[1]:

            two_chart('Gold (US$/Tr.Oz.)', gold_fut, 'US$', decimals=2, us_recession=True)

            with st.expander('More information'):

                st.write('''
                    Source: Banco Central de Reserva del Perú.
                    ''')

        # SILVER Y TRIGO

        comm2 = st.columns(2)

        with comm2[0]:

            two_chart('Silver (US$/Tr.Oz.)', silver_fut, 'US$', decimals=2, us_recession=True)

            with st.expander('More information'):

                st.write('''
                    Source: Yahoo! Finance.
                    
                    Silver futures are standardized, exchange-traded contracts in which the contract buyer agrees to take delivery, from the seller, a specific quantity of silver at a predetermined price on a future delivery date. Though its use as the nation's coinage was discontinued in 1965, at the turn of the century, an even more important economic function emerged for silver: that of an industrial raw material. Today, silver is sought as a valuable and practical industrial commodity, and silver futures are seen as an appealing investment that can be traded nearly 24 hours per day, 6 days per week. The largest industrial users of silver are the photographic, jewelry, and electronic industries. Silver futures are available for trading in the COMEX Division at the New York Mercantile Exchange (NYMEX).
                    ''')

        with comm2[1]:

            two_chart('Wheat (cUS$/bushel)', wheat_fut, 'cUS$', decimals=2, us_recession=True)

            with st.expander('More information'):

                st.write('''
                    Source: Yahoo! Finance.
                    
                    Representing the majority of the U.S. wheat crop, Hard Red Winter wheat is the primary ingredient in the world’s production of bread. KC HRW Wheat futures are by no means new; in fact, they’ve traded since 1876 – longer than the Chicago SRW Wheat futures. However, what market participants are noticing as of late is newfound liquidity. Bid-ask spread, market depth and breadth of participants have improved dramatically. Trades at the Chicago Board of Trade (CBOT - CME Group).
                    ''')

        comm3 = st.columns(2)

        with comm3[0]:

            two_chart('Corn (cUS$/bushel)', corn_fut, 'cUS$', decimals=2, us_recession=True)

            with st.expander('More information'):

                st.write('''
                    Source: Yahoo! Finance.
    
                    Corn futures are the most liquid and active market in grains, with 350,000 contracts traded per day. Trades at the Chicago Board of Trade (CBOT- CME Group).
                ''')

        with comm3[1]:

            two_chart('Soybean oil (cUS$/lb)', soybean_fut, 'cUS$', decimals=2, us_recession=True)

            with st.expander('More information'):
                st.write('''
                    Source: Yahoo! Finance.
    
                    Soybean futures are an easy, liquid tool for speculating or hedging against price movements for one of the world’s most widely grown crops. Seek rewards, manage risks and diversify your portfolio. Our global contracts enable you to trade around the new crop of the northern hemisphere in November and the South American new crop in May. Trades at the Chicago Board of Trade (CBOT - CME Group).
                ''')

        comm4 = st.columns(2)

        with comm4[0]:

            st.write('**Global Supply Chain Pressure Index**')

            tab0 = st.tabs(['Chart', 'Dataset', 'Download'])

            with tab0[0]:
                line_chart('Global Supply Chain Pressure Index', gscpi, 'Points', decimals=2, us_recession=True)

            with tab0[1]:

                st.dataframe(gscpi)

            with tab0[2]:
                def to_excel(data_frame):

                    output = BytesIO()

                    writer = pd.ExcelWriter(output, engine='xlsxwriter')

                    data_frame.to_excel(writer, index=False, sheet_name='Hoja1')

                    workbook = writer.book

                    worksheet = writer.sheets['Hoja1']

                    format1 = workbook.add_format({'num_format': '0.00'})

                    worksheet.set_column('A:A', None, format1)

                    writer.save()

                    processed_data = output.getvalue()

                    return processed_data

                df_xlsx = to_excel(gscpi)

                st.download_button(
                    label='Download data',
                    data=df_xlsx,
                    file_name='gscpi.xlsx'
                )

                with st.expander('More information'):
                    st.write('''
                            Source: Reserva Federal de Nueva York.
                            
                            Es un índice construido con el objetivo de proveer información sobre presiones a la cadena de suministros global, que puedan indicar restricciones significativas por el lado de la oferta, y que puedan afectar la producción global. Este indicador es compuesto con información de costos de transporte, cuellos de botella en la producción global, e información relevante sobre la producción manufacturera. Utiliza data del Baltic Dry Index (BDI), Harpex index, y del U.S. Bureau of Labor Statistics. Este índice también usa componentes de las encuestas PMI (Purchasing-Managers' Index) de China, Japón, la zona euro, Corea del Sur, Taiwán, Reino Unido y Estados Unidos.
                            ''')

    # TIPO DE CAMBIO

    with main_tabs[2]:

        st.subheader('FX')

# with tabs[1]:

#    st.subheader('S&P 500 snapshot')

with tabs1[1]:

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

    fed_rate_upper_t2 = fed_rate_upper['value'].iloc[-3]  # CHANGE ACCORDINGLY

    delta_fed_rate_upper = (fed_rate_upper_latest - fed_rate_upper_t2) * 100

    fed_rate_upper_latest = '{:,.2f}'.format(fed_rate_upper_latest)

    fed_rate_lower_latest = fed_rate_lower['value'].iloc[-1]

    fed_rate_lower_t2 = fed_rate_lower['value'].iloc[-3]

    delta_fed_rate_lower = fed_rate_lower_latest - fed_rate_lower_t2

    fed_rate_lower_latest = '{:,.2f}'.format(fed_rate_lower_latest)

    st.subheader('USA: Summary of key indicators')

    us = st.columns(4)

    us[0].metric(
        'Gross Domestic Product',
        str(us_gdp_latest) + '% y/y',
        f'{delta_us_gdp:.2f}' + ' p.p. y/y'
    )

    us[1].metric(
        'PCE Inflation',
        str(us_pce_latest) + '% y/y',
        f'{delta_us_pce:.2f}' + ' p.p. above target (2%)',
        delta_color='inverse'
    )

    us[2].metric(
        'Core PCE inflation',
        str(us_pce_core_latest) + '% y/y',
        f'{delta_us_pce_core:.2f}' + ' p.p. above target (2%)',
        delta_color='inverse'
    )

    us[3].metric(
        'Federal Funds Rate',
        str(fed_rate_lower_latest) + '-' + str(fed_rate_upper_latest) + '%',
        f'{delta_fed_rate_upper:,.0f}' + ' p.b. vs previous',
        delta_color='inverse'
    )

    # MAIN TABS

    main_tabs = st.tabs(['Macroeconomics', 'Finance', 'Public finances', 'Leading indicators'])

    with main_tabs[0]:
        st.subheader('Macroeconomics')

        st.write('USA GDP')
        'FRED'

        st.write('GDP Components')
        'FRED'

        st.write('**Inflation and core inflation (PCE and CPI)**')
        'FRED'
        'PCE: PCEPI'
        'Core PCE: PCEPILFE'
        'CPI: USACPIALLMINMEI'
        'Core CPI: USACPICORMINMEI'

        st.write('Unemployment')
        'FRED'

        st.write('**Retail inventories**')
        'https://fred.stlouisfed.org/series/RETAILIMSA'

    with main_tabs[1]:
        st.subheader('Finance')

        st.write('US Treasury Curve')
        'FRED'

        st.write('Bond yields')
        'FRED'

        st.write('3m-10y Spread')
        'FRED'

        st.write('2-10y Spread')
        'FRED'

        st.write('Federal Funds Rate (upper and lower bound, include real rate)')
        'FRED'

        st.write('Fed dot plots')
        'FRED'

    with main_tabs[2]:
        st.subheader('Public finances')

        st.write('**Federal Reserve Balance Sheet**')
        'https://fred.stlouisfed.org/series/WALCL'

        st.write('**USA debt**')

    with main_tabs[3]:
        st.subheader('Leading indicators')

        st.write('Nonfarm payrolls')
        'FRED'

        st.write('Initial jobless claims')
        'FRED'

        st.write('Continued jobless claims')
        'FRED'

        st.write('NY Fed Recession Probability')
        'Federal Reserve Bank of New York'
        'https://www.newyorkfed.org/research/capital_markets/ycfaq#/interactive'

        st.write('Empire State Manufacturing Survey')
        'Federal Reserve Bank of New York'
        'https://www.newyorkfed.org/survey/empire/empiresurvey_overview'

        st.write('GDPNow: Federal Reserve Bank of Atlanta GDP forecast')
        'Federal Reserve Bank of Atlanta'

with tabs1[2]:

    st.subheader('Peru: Summary of key indicators')

    # DELTA PBI

    pbi_peru_delta = delta_1y(pbi_peru['Var. % a/a'])

    # DELTA INFLACIÓN

    inflacion_delta = delta_1y(inflacion_peru['Var. % a/a'])

    # DELTA INFLACIÓN SIN ALIMENTOS Y ENERGÍA

    core_inflacion_delta = delta_1y(inflacion_peru_sub['Var. % a/a'])

    # DELTA TASA DE REFERENCIA

    tasa_bcrp_delta = delta_1d(tasa_bcrp['Tasa %'])

    # DELTA RENDIMIENTO BONO 10 AÑOS PEN

    # DELTA RENDIMIENTO BONO 10 AÑOS USD

    # DELTA TIPO DE CAMBIO

    # RESUMEN

    per1 = st.columns(4)

    per1[0].metric(
        'Gross Domestic Product',
        pbi_peru_delta[0] + '% y/y',
        pbi_peru_delta[1] + ' p.p. y/y'
    )

    per1[1].metric(
        'Inflation',
        str(inflacion_delta[0]) + '% y/y',
        inflacion_delta[1] + ' p.p. above target',
        delta_color='inverse'
    )

    per1[2].metric(
        'Inflation ex. food & energy',
        str(core_inflacion_delta[0]) + '% y/y',
        core_inflacion_delta[1] + ' p.p. above target',
        delta_color='inverse'
    )

    per1[3].metric(
        'BCRP reference rate',
        str(tasa_bcrp_delta[0]) + '%',
        tasa_bcrp_delta[1] + ' bps m/m',
        delta_color='inverse'
    )

    # BODY

    main_tabs = st.tabs(['Macroeconomics', 'Finance', 'Public finances', 'Leading indicators'])

    with main_tabs[0]:
        st.subheader('Macroeconomics')

        st.markdown('**Gross Domestic Product**')

        fig_pbi_peru = go.Figure()

        fig_pbi_peru.add_trace(
            go.Bar(
                name='GDP (% var. y/y)',
                x=pbi_peru['date'],
                y=pbi_peru['Var. % a/a'],
                marker_color=color_azul,
                # line=dict(color=color_azul),
                showlegend=True
            )
        )

        fig_pbi_peru.add_trace(
            go.Line(
                name='12-month GDP expectations (%)',
                x=exp_pbi_peru['date'],
                y=exp_pbi_peru['Expectativas PBI (%)'],
                line=dict(color=color_rojo),
                showlegend=True
            )
        )

        # fig_pbi_peru.add_trace(
        #    go.Line(
        #        name='PBI desestacionalizado (var. % m/m)',
        #        x=pbi_peru_des['date'],
        #        y=pbi_peru_des['Var. % m/m'],
        #        line=dict(color=color_rojo),
        #        showlegend=True
        #    )
        # )

        # fig_pbi_peru.add_trace(
        #    go.Line(
        #        name='PBI desestacionalizado (var. % promedio móvil 3 meses)',
        #        x=pbi_peru_des_prom['date'],
        #        y=pbi_peru_des_prom['Var. % promedio móvil 3m'],
        #        line=dict(color=color_azul_oscuro),
        #        showlegend=True
        #    )
        # )

        fig_pbi_peru.update_layout(
            {'plot_bgcolor': color_blanco, 'paper_bgcolor': color_blanco},
            font=dict(family='arial'),
            font_size=14,
            margin=dict(l=0, r=0, t=0, b=0),
            legend=dict(orientation="h", valign="bottom", xanchor="left", x=0, y=-0.13)
        )

        fig_pbi_peru.add_vrect(
            x0='2020-03-01',
            x1='2021-02-28',
            fillcolor=color_gris,
            opacity=0.25,
            line_width=0
        )

        fig_pbi_peru.update_yaxes(
            title='%',
            showgrid=False,
            zeroline=True,
            zerolinecolor='black',
            zerolinewidth=1
        )

        fig_pbi_peru.update_xaxes(
            title='Date',
            # rangeslider_visible=True,
            rangeselector=dict(
                buttons=list([
                    dict(count=6, label='6M', step='month', stepmode='backward'),
                    dict(count=1, label='YTD', step='year', stepmode='todate'),
                    dict(count=1, label='1Y', step='year', stepmode='backward'),
                    dict(count=5, label='5Y', step='year', stepmode='backward'),
                    dict(label='Max.', step='all')
                ]))
        )

        st.plotly_chart(fig_pbi_peru, use_container_width=True)

        with st.expander('More information'):
            st.write('''
            Source: Banco Central de Reserva del Perú.

            PBI peruano

            PBI peruano desestacionalizado

            PBI peruano desestacionalizado media móvil 3 meses
            ''')

        per2 = st.columns(2)

        with per2[0]:
            st.markdown('**Inflation**')

            fig_inflacion = go.Figure()

            fig_inflacion.add_trace(
                go.Line(
                    name='Inflation (% var. y/y)',
                    x=inflacion_peru['date'],
                    y=inflacion_peru['Var. % a/a'],
                    line=dict(color=color_rojo),
                    showlegend=True
                )
            )

            fig_inflacion.add_trace(
                go.Line(
                    name='Inflation ex. food & energy (% var. y/y)',
                    x=inflacion_peru_sub['date'],
                    y=inflacion_peru_sub['Var. % a/a'],
                    line=dict(color=color_azul),
                    showlegend=True
                )
            )

            fig_inflacion.add_trace(
                go.Line(
                    name='12-month inflation expectations (%)',
                    x=inflacion_peru_exp['date'],
                    y=inflacion_peru_exp['Expectativas'],
                    line=dict(color=color_gris),
                    showlegend=True
                )
            )

            fig_inflacion.update_layout(
                {'plot_bgcolor': color_blanco, 'paper_bgcolor': color_blanco},
                font=dict(family='arial'),
                font_size=14,
                margin=dict(l=0, r=0, t=0, b=0),
                legend=dict(orientation="h", valign="bottom", xanchor="left", x=0, y=-0.13)
            )

            fig_inflacion.add_hline(y=1, line_width=1)

            fig_inflacion.add_hline(y=3, line_width=1)

            fig_inflacion.add_vrect(
                x0='2020-03-01',
                x1='2021-02-28',
                fillcolor=color_gris,
                opacity=0.25,
                line_width=0
            )

            fig_inflacion.update_yaxes(
                title='%'
            )

            fig_inflacion.update_xaxes(
                title='Fecha',
                # rangeslider_visible=True,
                rangeselector=dict(
                    buttons=list([
                        dict(count=6, label='6M', step='month', stepmode='backward'),
                        dict(count=1, label='YTD', step='year', stepmode='todate'),
                        dict(count=1, label='1Y', step='year', stepmode='backward'),
                        dict(count=5, label='5Y', step='year', stepmode='backward'),
                        dict(label='Max.', step='all')
                    ]))
            )

            st.plotly_chart(fig_inflacion, use_container_width=True)

            with st.expander('More information'):
                st.write('''
                Source: Banco Central de Reserva del Perú.
                ''')

        with per2[1]:
            st.markdown('**BCRP monetary policy reference rate**')

            fig_tasa_bcrp = go.Figure()

            fig_tasa_bcrp.add_trace(
                go.Line(
                    name='BCRP reference rate',
                    x=tasa_bcrp['date'],
                    y=tasa_bcrp['Tasa %'],
                    line=dict(color=color_azul),
                    showlegend=False
                )
            )

            fig_tasa_bcrp.add_vrect(
                x0='2020-03-01',
                x1='2021-02-28',
                fillcolor=color_gris,
                opacity=0.25,
                line_width=0
            )

            fig_tasa_bcrp.update_layout(
                {'plot_bgcolor': color_blanco, 'paper_bgcolor': color_blanco},
                font=dict(family='arial'),
                font_size=14,
                margin=dict(l=0, r=0, t=0, b=0),
                # legend=dict(orientation="h", valign="bottom", xanchor="left", x=0, y=-0.13)
            )

            fig_tasa_bcrp.update_yaxes(
                title='%'
            )

            fig_tasa_bcrp.update_xaxes(
                title='Date',
                # rangeslider_visible=True,
                rangeselector=dict(
                    buttons=list([
                        dict(count=6, label='6M', step='month', stepmode='backward'),
                        dict(count=1, label='YTD', step='year', stepmode='todate'),
                        dict(count=1, label='1A', step='year', stepmode='backward'),
                        dict(count=5, label='5A', step='year', stepmode='backward'),
                        dict(label='Máx.', step='all')
                    ]))
            )

            st.plotly_chart(fig_tasa_bcrp, use_container_width=True)

            with st.expander('More information'):
                st.write('''
                Source: Banco Central de Reserva del Perú.
                ''')

        st.markdown('**3 and 12 month expectations on the economy**')

        fig_exp_eco = go.Figure()

        fig_exp_eco.add_trace(
            go.Line(
                name='3 months ahead',
                x=exp_eco_3m['date'],
                y=exp_eco_3m['Expectativas a 3 meses'],
                line=dict(color=color_azul),
                showlegend=True
            )
        )

        fig_exp_eco.add_trace(
            go.Line(
                name='12 months ahead',
                x=exp_eco_12m['date'],
                y=exp_eco_12m['Expectativas a 12 meses'],
                line=dict(color=color_rojo),
                showlegend=True
            )
        )

        fig_exp_eco.add_vrect(
            x0='2020-03-01',
            x1='2021-02-28',
            fillcolor=color_gris,
            opacity=0.25,
            line_width=0
        )

        fig_exp_eco.add_hline(
            y=50,
            line_width=1,
            annotation_text='Optimism',
            annotation_position='top left'
        )

        fig_exp_eco.update_layout(
            {'plot_bgcolor': color_blanco, 'paper_bgcolor': color_blanco},
            font=dict(family='arial'),
            font_size=14,
            margin=dict(l=0, r=0, t=0, b=0),
            legend=dict(orientation="h", valign="bottom", xanchor="left", x=0, y=-0.13)
        )

        fig_exp_eco.update_yaxes(
            title='%'
        )

        fig_exp_eco.update_xaxes(
            title='Date',
            # rangeslider_visible=True,
            rangeselector=dict(
                buttons=list([
                    dict(count=6, label='6M', step='month', stepmode='backward'),
                    dict(count=1, label='YTD', step='year', stepmode='todate'),
                    dict(count=1, label='1Y', step='year', stepmode='backward'),
                    dict(count=5, label='5Y', step='year', stepmode='backward'),
                    dict(label='Max.', step='all')
                ]))
        )

        st.plotly_chart(fig_exp_eco, use_container_width=True)

        with st.expander('More information'):
            st.write('''
            Source: Banco Central de Reserva del Perú.
            ''')

        st.markdown('**Unemployment**')
        'BCRP'

    with main_tabs[1]:

        st.subheader('Finance')

        st.markdown('**BCRP monetary policy reference rate**')
        'BCRP'

        st.write('**Yield of the PEN 10 year bond**')

        st.write('**Yield of the USD 10 year bond**')

    with main_tabs[2]:

        st.subheader('Leading indicators')

with tabs1[3]:

    st.subheader('News')
