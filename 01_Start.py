# IMPORT CONFIGURATIONS

import streamlit as st
# import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import os
# import hydralit_components as hc
from plotly.subplots import make_subplots
# from plotly_resampler import register_plotly_resampler
import locale
import platform
from io import BytesIO
from pyxlsb import open_workbook as open_xlsb

st.set_page_config(
    layout='wide',
    page_title='Condiciones macrofinancieras',
    page_icon=''
)

locale.setlocale(locale.LC_TIME, 'es_ES')

if platform.system() == 'Windows':

    os.chdir('C:/Users/pport/OneDrive/Projects/Macrofinancial-dashboard/')

if platform.system() == 'Darwin':

    os.chdir('/Users/pportocarrero/OneDrive/Projects/Macrofinancial-dashboard/')

# LOAD DATA AND OTHER CONFIGS

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

font_name = 'arial'
text_size = 14

# SIDEBAR

# ACÁ HAY QUE INCLUIR UNA OPCIÓN PARA QUE EL USUARIO CAMBIE DE IDIOMA

# RESUMEN

st.title('Resumen de los mercados financieros')

# DELTA DEL S&P 500

sp_500_latest = sp_500['Close'].iloc[-1]

sp_500_t2 = sp_500['Close'].iloc[-2]

delta_sp_500 = sp_500_latest - sp_500_t2

delta_sp_500_pct = sp_500_latest / sp_500_t2 - 1

sp_500_latest = "{:,.2f}".format(sp_500_latest).replace(',', ' ').replace('.', ',')

delta_sp_500_pct = '{:.2%}'.format(delta_sp_500_pct).replace('.', ',')

# DELTA DOW JONES

dji_latest = dji_index['Close'].iloc[-1]

dji_t2 = dji_index['Close'].iloc[-2]

delta_dji = dji_latest - dji_t2

delta_dji_pct = dji_latest / dji_t2 - 1

dji_latest = '{:,.2f}'.format(dji_latest).replace(',', ' '). replace('.', ',')

delta_dji_pct = '{:.2%}'.format(delta_dji_pct).replace('.', ',')

# DELTA NASDAQ 100

nasdaq_latest = nasdaq_100['Close'].iloc[-1]

nasdaq_t2 = nasdaq_100['Close'].iloc[-2]

delta_nasdaq = nasdaq_latest - nasdaq_t2

delta_nasdaq_pct = nasdaq_latest / nasdaq_t2 - 1

nasdaq_latest = '{:,.2f}'.format(nasdaq_latest).replace(',', ' ').replace('.', ',')

delta_nasdaq_pct = '{:.2%}'.format(delta_nasdaq_pct).replace('.', ',')

# DELTA VIX

vix_latest = vix_index['Close'].iloc[-1]

vix_t2 = vix_index['Close'].iloc[-2]

delta_vix = vix_latest - vix_t2

delta_vix_pct = vix_latest / vix_t2 - 1

vix_latest = '{:,.2f}'.format(vix_latest).replace(',', ' ').replace('.', ',')

delta_vix_pct = '{:.2%}'.format(delta_vix_pct).replace('.', ',')

# DELTA MOVE

move_latest = move_index['Close'].iloc[-1]

move_t2 = move_index['Close'].iloc[-2]

delta_move = move_latest - move_t2

delta_move_pct = move_latest / move_t2 - 1

move_latest = '{:,.2f}'.format(move_latest).replace(',', ' ').replace('.', ',')

delta_move_pct = '{:.2%}'.format(delta_move_pct).replace('.', ',')

# DELTA WTI CRUDE

wti_crude_latest = wti_crude['Close'].iloc[-1]

wti_crude_t2 = wti_crude['Close'].iloc[-2]

delta_wti = wti_crude_latest - wti_crude_t2

delta_wti_pct = wti_crude_latest / wti_crude_t2 - 1

wti_crude_latest = '{:,.2f}'.format(wti_crude_latest).replace(',', ' ').replace('.', ',')

delta_wti_pct = '{:.2%}'.format(delta_wti_pct).replace('.', ',')

# DELTA COPPER

copper_fut_latest = copper_fut['Close'].iloc[-1]

copper_fut_t2 = copper_fut['Close'].iloc[-2]

delta_copper = copper_fut_latest - copper_fut_t2

delta_copper_pct = copper_fut_latest / copper_fut_t2 - 1

copper_fut_latest = '{:,.4f}'.format(copper_fut_latest).replace(',', ' ').replace('.', ',')

delta_copper_pct = '{:.2%}'.format(delta_copper_pct).replace('.', ',')

# DELTA USD/PEN

usd_pen_latest = usd_pen['4. close'].iloc[-1]

usd_pen_t2 = usd_pen['4. close'].iloc[-2]

delta_usd_pen = usd_pen_latest - usd_pen_t2

delta_usd_pen_pct = usd_pen_latest / usd_pen_t2 - 1

usd_pen_latest = '{:,.4f}'.format(usd_pen_latest).replace(',', ' ').replace('.', ',')

delta_usd_pen_pct = '{:.2%}'.format(delta_usd_pen_pct).replace('.', ',')

# KPI's

kpi1 = st.columns(4)

kpi1[0].metric('S&P 500', str(sp_500_latest) + ' pts', str(delta_sp_500_pct) + ' (' + f'{delta_sp_500:.2f}'.replace('.', ',') + ' pts)')

kpi1[1].metric('Dow Jones 30', str(dji_latest) + ' pts', str(delta_dji_pct) + ' (' + f'{delta_dji:.2f}'.replace('.', ',') + ' pts)')

kpi1[2].metric('Nasdaq 100', str(nasdaq_latest) + ' pts', str(delta_nasdaq_pct) + ' (' + f'{delta_nasdaq:.2f}'.replace('.', ',') + ' pts)')

kpi1[3].metric('Crudo WTI', str(wti_crude_latest) + ' US$/bbl', str(delta_wti_pct) + ' (' + f'{delta_wti:.2f}'.replace('.', ',') + ' US$/bbl)')

kpi2 = st.columns(4)

kpi2[0].metric('Índice de volatilidad VIX', str(vix_latest) + ' US$', str(delta_vix_pct) + ' (' + f'{delta_vix:.2f}'.replace('.', ',') + ' US$)', delta_color='inverse')

kpi2[1].metric('Índice de volatilidad MOVE', str(move_latest) + ' US$', str(delta_move_pct) + ' (' + f'{delta_move:.2f}'.replace('.', ',') + ' US$)', delta_color='inverse')

kpi2[2].metric('Cobre', str(copper_fut_latest) + ' US$/lb', str(delta_copper_pct) + ' (' + f'{delta_copper:.4f}'.replace('.', ',') + ' US$/lb)')

kpi2[3].metric('USD/PEN', 'S/ ' + str(usd_pen_latest) + ' /US$', str(delta_usd_pen_pct) + ' (S/ ' + f'{delta_usd_pen:.4f}'.replace('.', ',') + ' /US$)', delta_color='inverse')

###########

# FUNCTION TO CREATE AREA CHART
def line_chart(name, ticker_id, y_axis, us_recession=False):

    import plotly.graph_objects as go

    import streamlit as st

    if us_recession is True:

        fig = go.Figure()

        fig.add_trace(
            go.Scatter(
                name=name,
                x=ticker_id['Date'],
                y=ticker_id['Close'],
                line=dict(color='blue'),
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
            margin=dict(l=0, r=0, t=0, b=0),
            hovermode='x unified',
            yaxis=dict(tickformat=',.1f'),
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
                    dict(label='Máx.', step='all')
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
                line=dict(color='blue'),
                fill='tozeroy'
            )
        )

        fig.update_layout(
            margin=dict(l=0, r=0, t=0, b=0),
            hovermode='x unified',
            yaxis=dict(tickformat=',.1f'),
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
                    dict(label='Máx.', step='all')
                ]))
        )

        fig.update_yaxes(title_text=y_axis)

        return st.plotly_chart(fig, use_container_width=True)

###########

# CREATE FUNCTION FOR CANDLESTICK CHARTS

def olhc_chart(name, ticker_id, us_recession=False):

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
                increasing_line_color='green',
                decreasing_line_color='red',
                showlegend=False
            ),
            row=1,
            col=1
        )

        fig.add_trace(
            go.Bar(
                x=ticker_id['Date'],
                y=ticker_id['Volume'],
                showlegend=False,
                name='Volumen'
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
            margin=dict(l=0, r=0, t=0, b=0),
            hovermode='x unified',
            yaxis=dict(tickformat=',.1f'),
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
                    dict(label='Máx.', step='all')
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
                increasing_line_color='green',
                decreasing_line_color='red',
                showlegend=False
            ),
            row=1,
            col=1
        )

        fig.add_trace(
            go.Bar(
                x=ticker_id['Date'],
                y=ticker_id['Volume'],
                showlegend=False,
                name='Volumen'
            ),
            row=2,
            col=1
        )

        fig.update(layout_xaxis_rangeslider_visible=False)

        fig.update_layout(
            margin=dict(l=0, r=0, t=0, b=0),
            hovermode='x unified',
            yaxis=dict(tickformat=',.1f'),
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
                    dict(label='Máx.', step='all')
                ]))
        )

        return st.plotly_chart(fig, use_container_width=True)

###########

def two_chart(name: str, data_frame, y_axis, us_recession=False):

    st.markdown('**' + name + '**')

    chart = st.selectbox('Seleccione el tipo de gráfico', ('Gráfico de línea', 'Gráfico OHLC + Volumen'), key=name)

    if chart == 'Gráfico de línea':

        tab0 = st.tabs(['Gráfico', 'Tabla', 'Descargar'])

        with tab0[0]:

            line_chart(name, data_frame, y_axis, us_recession=False)

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
                label='Descarga la data',
                data=df_xlsx,
                file_name=name + '.xlsx'
            )

    elif chart == 'Gráfico OHLC + Volumen':

        tab1 = st.tabs(['Gráfico', 'Tabla'])

        with tab1[0]:

            olhc_chart(name, data_frame, us_recession=False)

        with tab1[1]:

            st.dataframe(data_frame)

###########
# ÍNDICES BURSÁTILES Y DE RENTA FIJA

main_tabs = st.tabs(['Equities y renta fija', 'Materias primas', 'Monedas'])

with main_tabs[0]:

    st.subheader('Índices bursátiles y de renta fija')

    # S&P 500 y DJI

    eq = st.columns(2)

    with eq[0]:

        two_chart('S&P 500', sp_500, 'Puntos', True)

        with st.expander('Más información:'):

            st.write('''
            Fuente: Yahoo! Finance.
                
            El índice S&P 500 es considerado como el mejor barómetro de las compañías de alta capitalización en Estados Unidos. El índice incluye 500 compañías públicas de diferentes sectores de la economía y cubre aproximadamente el 80% del total de capitalización de mercado disponible. El S&P 500 es un índice bursátil ponderado en base a la capitalización de mercado de las compañías que la componen. De acuerdo a la Encuesta anual de activos, se estima que US$ 13 billones están indexados o comparados a este índice.
            ''')

    with eq[1]:

        two_chart('Dow Jones Industrial Average', dji_index, 'Puntos', True)

        with st.expander('Más información:'):

            st.write('''
            Fuente: Yahoo! Finance.
    
            El Dow Jones Industrial Average es un indicador ponderado por el precio de 30 compañías 'blue-chip' norteamericanas. Este índice cubre todas las industrias con la excepción de transportes y servicios públicos.
            ''')

    eq1 = st.columns(2)

    with eq1[0]:

        two_chart('Nasdaq 100', nasdaq_100, 'Puntos', True)

        with st.expander('Más información:'):

            st.write('''
            Fuente: Federal Reserve Bank of St. Louis (Federal Reserve Economic Data).
                
            El Nasdaq 100 es un índice basado en una canasta de 100 acciones de las empresas que más actividad tienen en la bolsa de valores Nasdaq. El índice incluye empresas de varios sectores, a excepción de las financieras. El índice se calcula en base a la ponderación de la capitalización de las empresas.
            ''')

    with eq1[1]:

        two_chart('Russell 3000', russell_3000, 'Puntos', True)

        with st.expander('Más información:'):

            st.write('''
            Fuente: Yahoo! Finance.
    
            Por su parte, el índice Russell 3000 es un índice bursátil ponderado por capitalización de mercado que provee exposición a todo el mercado bursátil norteamericano. Este índice sigue el desempeño de las 3 mil empresas norteamericanas públicas con mayor capitalización en el mercado, que representa el 97% de todas las empresas incorporadas en EE.UU. que cotizan en el mercado bursátil norteamericano.
            ''')

    eq3, eq4 = st.columns(2)

    with eq3:

        two_chart('Russell 2000', russell_2000, 'Puntos', True)

        with st.expander('Más información:'):

            st.write('''
            Fuente: Yahoo! Finance
    
            El índice Russell 2000 se refiere a un indice bursátil que mide el desempeño de las 2,000 compañías más pequeñas que forman parte del índice Russell 3000. Este índice es administrado por FTSE Russell y es considerado uno de los referentes de la salud de la economía norteamericana por su énfasis en compañías públicas pequeñas del mercado norteamericnano.
            ''')

    with eq4:

        st.markdown('**FTSE 100**')

        ftse_chart = st.selectbox('Seleccione el tipo de gráfico', ('Gráfico de línea', 'Gráfico OHLC + Volumen'), key='ftse_key')

        if ftse_chart == 'Gráfico de línea':

            line_chart('FTSE 100', ftse_100, 'Puntos', False)

        elif ftse_chart == 'Gráfico OHLC + Volumen':

            line_chart('FTSE 100', ftse_100, False)

        with st.expander('Más información'):

            st.write('''
            Fuente: Yahoo! Finance.
    
            El FTSE 100 es un índice bursátil de las 100 empresas que cotizan en el London Stock Exchange con la mayor capitalización de mercado.El índice es mantenido por el Grupo FTSE, una subsidiaria del Grupo London Stock Exchange.
            ''')

    # VIX y FTSE 100

    eq5 = st.columns(2)

    with eq5[0]:

        st.markdown('**Índice de volatilidad CBOE VIX**')

        vix_chart = st.selectbox('Seleccione el tipo de gráfico', ('Gráfico de línea', 'Gráfico OHLC + Volumen'), key='vix_key')

        if vix_chart == 'Gráfico de línea':

            line_chart('Índice VIX', vix_index, 'USD', True)

        elif vix_chart == 'Gráfico OHLC + Volumen':

            olhc_chart('Índice VIX', vix_index, True)

        with st.expander('Más información'):

            st.write('''
            Fuente: Yahoo! Finance.
    
            El índice VIX es una estimación destinada a producir una medida constante de la volatilidad esperada a 30 días del mercado bursátil norteamericano. Esta medida se deriva del precio "mid" de opciones call y put del índice S&P 500 a tiempo real. A nivel global, es una de las medidas de volatilidad más importantes -- ampliamente citada y seguida por medios especializados, así como por participantes del mercado como un indicador de seguimiento.
            ''')

    with eq5[1]:

        st.markdown('**Índice de volatilidad MOVE**')

        move_chart = st.selectbox('Seleccione el tipo de gráfico', ('Gráfico de línea', 'Gráfico OHLC + Volumen'), key='move_key')

        if move_chart == 'Gráfico de línea':

            line_chart('Índice MOVE', move_index, 'USD', True)

        elif move_chart == 'Gráfico OHLC + Volumen':

            olhc_chart('Índice MOVE', move_index, True)

        with st.expander('Más información'):

            st.write('''
            Fuente: Yahoo! Finance.
    
            El índice MOVE es una reconocida medida de la volatilidad de tasas de interés en EE.UU. que sigue el movimiento de la volatilidad implícita del rendimiento de instrumentos del Tesoro norteamericano a través de los precios vigentes de opciones a 1 mes de bonos del Tesoro norteamericano a 2, 5, 10 y 30 años.
    
            Es una media ponderada del rendimiento constante a 2, 5, 10 y 30 años de los bonos del Tesoro norteamericano con los siguientes pesos: 20%, 20%, 40% y 20%, respectivamente.
            ''')

    eq6 = st.columns(2)

    with eq6[0]:

        st.markdown('**Shanghai Composite**')

        shanghai_chart = st.selectbox('Seleccione el tipo de gráfico', ('Gráfico de línea', 'Gráfico OHLC + Volumen'), key='shanghai_key')

        if shanghai_chart == 'Gráfico de línea':

            line_chart('Shanghai Composite', shanghai_comp, 'Puntos', False)

        elif shanghai_chart == 'Gráfico OHLC + Volumen':

            olhc_chart('Shanghai Composite', shanghai_comp, False)

        with st.expander('Más información'):
            st.write('''
            Fuente: Yahoo! Finance.
    
            The SSE Composite Index also known as SSE Index is a stock market index of all stocks that are traded at the Shanghai Stock Exchange.
            ''')

    with eq6[1]:

        st.markdown('**Nikkei 225**')

        nikkei_chart = st.selectbox('Seleccione el tipo de gráfico', ('Gráfico de línea', 'Gráfico OHLC + Volumen'), key='nikkei_key')

        if nikkei_chart == 'Gráfico de línea':

            line_chart('Nikkei 225', nikkei_225, 'Puntos', False)

        elif nikkei_chart == 'Gráfico OHLC + Volumen':

            olhc_chart('Nikkei 225', nikkei_225, False)

        with st.expander('Más información'):

            st.write('''
            Fuente: Banco Central de Reserva del Perú.
    
            El índice Nikkei 225 is a stock market index for the Tokyo Stock Exchange. It has been calculated daily by the Nihon Keizai Shimbun newspaper since 1950.
            ''')

    # SHANGHAI Y NIKKEI 225

    eq7, eq8 = st.columns(2)

    with eq7:

        st.write('**S&P/BVL Perú General**')

        line_chart('S&P/BVL Perú General', bvl_gen, 'Puntos', False)

        with st.expander('Más información'):

            st.write('''
            Fuente: Standard & Poor's.
            ''')

with main_tabs[1]:

# MATERIAS PRIMAS

    st.subheader('Materias primas')

    # CRUDOS WTI Y BRENT

    com1, com2 = st.columns(2)

    with com1:

        st.markdown('**Crudo WTI y Brent (US$/barril)**')

        crude_chart = st.selectbox('Seleccione el tipo de gráfico', ('Gráfico de línea', 'Gráfico OHLC + Volumen'), key='crude_key')

        if crude_chart == 'Gráfico de línea':

            fig_crude = go.Figure()

            fig_crude.add_trace(
                go.Line(
                    name='Crudo WTI',
                    x=wti_crude['Date'],
                    y=wti_crude['Close'],
                    line=dict(color=color_azul)
                )
            )

            fig_crude.add_trace(
                go.Line(
                    name='Crudo Brent',
                    x=brent_crude['Date'],
                    y=brent_crude['Close'],
                    line=dict(color=color_rojo)
                )
            )

            fig_crude.add_vrect(
                x0='2001-03-01',
                x1='2001-11-01',
                fillcolor=color_gris,
                opacity=0.25,
                line_width=0
            )

            fig_crude.add_vrect(
                x0='2007-12-01',
                x1='2009-06-01',
                fillcolor=color_gris,
                opacity=0.25,
                line_width=0
            )

            fig_crude.add_vrect(
                x0='2020-02-01',
                x1='2020-04-01',
                fillcolor=color_gris,
                opacity=0.25,
                line_width=0
            )

            fig_crude.update_layout(
                {'plot_bgcolor': color_blanco, 'paper_bgcolor': color_blanco},
                font=dict(family='arial'),
                font_size=14,
                margin=dict(l=0, r=0, t=0, b=0),
                legend=dict(orientation="h", valign="bottom", xanchor="left", x=0, y=-0.13)
            )

            fig_crude.update_xaxes(
                title='Fecha',
                rangebreaks=[dict(bounds=["sat", "mon"])],
                rangeselector=dict(
                    buttons=list([
                        dict(count=3, label='3D', step='day', stepmode='backward'),
                        dict(count=5, label='1S', step='day', stepmode='backward'),
                        dict(count=1, label='1M', step='month', stepmode='backward'),
                        dict(count=6, label='6M', step='month', stepmode='backward'),
                        dict(count=1, label='YTD', step='year', stepmode='todate'),
                        dict(count=1, label='1A', step='year', stepmode='backward'),
                        dict(label='Máx.', step='all')
                    ]))
            )

            st.plotly_chart(fig_crude, use_container_width=True)

        elif crude_chart == 'Gráfico OHLC + Volumen':

            fig_crude = make_subplots()

            fig_crude.add_trace(
                go.Candlestick(
                    x=wti_crude['Date'],
                    open=wti_crude['Open'],
                    high=wti_crude['High'],
                    low=wti_crude['Low'],
                    close=wti_crude['Close'],
                    name='WTI',
                    showlegend=True,
                    increasing_line_color=color_azul,
                    decreasing_line_color=color_rojo
                )
            )

            fig_crude.add_trace(
                go.Candlestick(
                    x=brent_crude['Date'],
                    open=brent_crude['Open'],
                    high=brent_crude['High'],
                    low=brent_crude['Low'],
                    close=brent_crude['Close'],
                    name='Brent',
                    showlegend=True,
                    increasing_line_color=color_azul_oscuro,
                    decreasing_line_color=color_rojo_claro
                )
            )

            fig_crude.update(layout_xaxis_rangeslider_visible=False)

            fig_crude.update_layout(
                {'plot_bgcolor': color_blanco, 'paper_bgcolor': color_blanco},
                font=dict(family='arial'),
                font_size=14,
                margin=dict(l=0, r=0, t=0, b=0),
                legend=dict(orientation="h", valign="bottom", xanchor="left", x=0, y=-0.13)
            )

            fig_crude.update_xaxes(
                rangebreaks=[dict(bounds=["sat", "mon"])],
                rangeselector=dict(
                    buttons=list([
                        dict(count=3, label='3D', step='day', stepmode='backward'),
                        dict(count=5, label='1S', step='day', stepmode='backward'),
                        dict(count=1, label='1M', step='month', stepmode='backward'),
                        dict(count=6, label='6M', step='month', stepmode='backward'),
                        dict(count=1, label='YTD', step='year', stepmode='todate'),
                        dict(count=1, label='1A', step='year', stepmode='backward'),
                        dict(label='Máx.', step='all')
                    ]))
            )

            st.plotly_chart(fig_crude, use_container_width=True)

        with st.expander('Más información'):
            st.write('''
                Fuente: Federal Reserve Bank of St. Louis.
                    
                WTI is the underlying commodity of the New York Mercantile Exchange's (NYMEX) oil futures contract and is considered a high-quality oil that is easily refined.
                    
                West Texas Intermediate (WTI) crude oil is a specific grade of crude oil and one of the main three benchmarks in oil pricing, along with Brent and Dubai Crude. WTI is known as a light sweet oil because it contains between 0.24% and 0.34% sulfur, making it "sweet," and has a low density (specific gravity), making it "light."
                
                Brent actually refers to oil from four different fields in the North Sea: Brent, Forties, Oseberg, and Ekofisk. Crude from this region is light and sweet, making them ideal for the refining of diesel fuel, gasoline, and other high-demand products. And because the supply is waterborne, it’s easy to transport to distant locations.
                ''')

    with com2:

        st.write('**Principales metales**')

        metals_chart = st.selectbox('Seleccione el tipo de gráfico', ('Gráfico de línea', 'Gráfico OHLC + Volumen'), key='metals_key')

        if metals_chart == 'Gráfico de línea':

            fig_metals = make_subplots(specs=[[{"secondary_y": True}]])

            fig_metals.add_trace(
                go.Line(
                    name='Cobre (izq.)',
                    x=copper_fut['Date'],
                    y=copper_fut['Close'],
                    line=dict(color=color_rojo)
                ),
                secondary_y=False
            )

            fig_metals.add_trace(
                go.Line(
                    name='Oro (der.)',
                    x=gold_fut['Date'],
                    y=gold_fut['Close'],
                    line=dict(color=color_azul)
                ),
                secondary_y=True
            )

            fig_metals.add_vrect(
                x0='2001-03-01',
                x1='2001-11-01',
                fillcolor=color_gris,
                opacity=0.25,
                line_width=0
            )

            fig_metals.add_vrect(
                x0='2007-12-01',
                x1='2009-06-01',
                fillcolor=color_gris,
                opacity=0.25,
                line_width=0
            )

            fig_metals.add_vrect(
                x0='2020-02-01',
                x1='2020-04-01',
                fillcolor=color_gris,
                opacity=0.25,
                line_width=0
            )

            fig_metals.update_layout(
                {'plot_bgcolor': color_blanco, 'paper_bgcolor': color_blanco},
                font=dict(family='arial'),
                font_size=14,
                margin=dict(l=0, r=0, t=0, b=0),
                legend=dict(orientation="h", valign="bottom", xanchor="left", x=0, y=-0.13)
            )

            fig_metals.update_yaxes(title='US$/lb', secondary_y=False)

            fig_metals.update_yaxes(title='US$/Oz.tr.', secondary_y=True)

            fig_metals.update_xaxes(
                title='Fecha',
                # rangeslider_visible=True,
                rangeselector=dict(
                    buttons=list([
                        dict(count=3, label='3D', step='day', stepmode='backward'),
                        dict(count=5, label='1S', step='day', stepmode='backward'),
                        dict(count=1, label='1M', step='month', stepmode='backward'),
                        dict(count=6, label='6M', step='month', stepmode='backward'),
                        dict(count=1, label='YTD', step='year', stepmode='todate'),
                        dict(count=1, label='1A', step='year', stepmode='backward'),
                        dict(count=5, label='5A', step='year', stepmode='backward'),
                        dict(label='Máx.', step='all')
                    ]))
            )

            st.plotly_chart(fig_metals, use_container_width=True)

        elif metals_chart == 'Gráfico OHLC + Volumen':

            fig_metals = make_subplots(specs=[[{"secondary_y": True}]])

            fig_metals.add_trace(
                go.Candlestick(
                    x=copper_fut['Date'],
                    open=copper_fut['Open'],
                    high=copper_fut['High'],
                    low=copper_fut['Low'],
                    close=copper_fut['Close'],
                    name='Cobre (izq.)',
                    showlegend=True,
                    increasing_line_color=color_azul,
                    decreasing_line_color=color_rojo
                ),
                secondary_y=False
            )

            fig_metals.add_trace(
                go.Candlestick(
                    x=gold_fut['Date'],
                    open=gold_fut['Open'],
                    high=gold_fut['High'],
                    low=gold_fut['Low'],
                    close=gold_fut['Close'],
                    name='Oro (der.)',
                    showlegend=True,
                    increasing_line_color=color_azul_oscuro,
                    decreasing_line_color=color_rojo_claro
                ),
                secondary_y=True
            )

            fig_metals.update(layout_xaxis_rangeslider_visible=False)

            fig_metals.update_layout(
                {'plot_bgcolor': color_blanco, 'paper_bgcolor': color_blanco},
                font=dict(family='arial'),
                font_size=14,
                margin=dict(l=0, r=0, t=0, b=0),
                legend=dict(orientation="h", valign="bottom", xanchor="left", x=0, y=-0.13)
            )

            fig_metals.update_xaxes(
                rangebreaks=[dict(bounds=["sat", "mon"])],
                rangeselector=dict(
                    buttons=list([
                        dict(count=3, label='3D', step='day', stepmode='backward'),
                        dict(count=5, label='1S', step='day', stepmode='backward'),
                        dict(count=1, label='1M', step='month', stepmode='backward'),
                        dict(count=6, label='6M', step='month', stepmode='backward'),
                        dict(count=1, label='YTD', step='year', stepmode='todate'),
                        dict(count=1, label='1A', step='year', stepmode='backward'),
                        dict(label='Máx.', step='all')
                    ]))
            )

            fig_metals.update_yaxes(title='US$/lb', secondary_y=False)

            fig_metals.update_yaxes(title='US$/Oz.tr.', secondary_y=True)

            st.plotly_chart(fig_metals, use_container_width=True)

        with st.expander('Más información'):

            st.write('''
                    Fuente: Banco Central de Reserva del Perú.
                    ''')

    # COBRE Y ORO

    comm1 = st.columns(2)

    with comm1[0]:

        st.write('**Plata (US$/Oz.tr.)**')

        silver_chart = st.selectbox('Seleccione el tipo de gráfico', ('Gráfico de línea', 'Gráfico OHLC + Volumen'), key='silver_key')

        if silver_chart == 'Gráfico de línea':

            fig_silver = go.Figure()

            fig_silver.add_trace(
                go.Line(
                    name='Plata (US$/Oz.tr.)',
                    x=silver_fut['Date'],
                    y=silver_fut['Close'],
                    line=dict(color=color_azul)
                ))

            fig_silver.update_layout(
                {'plot_bgcolor': color_blanco, 'paper_bgcolor': color_blanco},
                font=dict(family='arial'),
                font_size=14,
                margin=dict(l=0, r=0, t=0, b=0)
            )

            fig_silver.update_yaxes(title='US$')

            fig_silver.update_xaxes(
                title='Fecha',
                # rangeslider_visible=True,
                rangeselector=dict(
                    buttons=list([
                        dict(count=3, label='3D', step='day', stepmode='backward'),
                        dict(count=5, label='1S', step='day', stepmode='backward'),
                        dict(count=1, label='1M', step='month', stepmode='backward'),
                        dict(count=6, label='6M', step='month', stepmode='backward'),
                        dict(count=1, label='YTD', step='year', stepmode='todate'),
                        dict(count=1, label='1A', step='year', stepmode='backward'),
                        dict(label='Máx.', step='all')
                    ]))
            )

            st.plotly_chart(fig_silver, use_container_width=True)

        elif silver_fut == 'Gráfico OHLC + Volumen':

            fig_silver = make_subplots(
                rows=2,
                cols=1,
                shared_xaxes=True,
                vertical_spacing=0.03,
                # subplot_titles=('OLHC', 'Volumen'),
                row_width=[0.2, 0.7]
            )

            fig_silver.add_trace(
                go.Candlestick(
                    x=silver_fut['Date'],
                    open=silver_fut['Open'],
                    high=silver_fut['High'],
                    low=silver_fut['Low'],
                    close=silver_fut['Close'],
                    name='OLHC',
                    showlegend=False
                ),
                row=1,
                col=1
            )

            fig_silver.add_trace(
                go.Bar(
                    x=silver_fut['Date'],
                    y=silver_fut['Volume'],
                    showlegend=False,
                    name='Volumen'
                ),
                row=2,
                col=1
            )

            fig_silver.update(layout_xaxis_rangeslider_visible=False)

            fig_silver.update_layout(
                {'plot_bgcolor': color_blanco, 'paper_bgcolor': color_blanco},
                font=dict(family='arial'),
                font_size=12,
                margin=dict(l=0, r=0, t=0, b=0)
            )

            fig_silver.update_xaxes(
                rangebreaks=[dict(bounds=["sat", "mon"])],
                rangeselector=dict(
                    buttons=list([
                        dict(count=3, label='3D', step='day', stepmode='backward'),
                        dict(count=5, label='1S', step='day', stepmode='backward'),
                        dict(count=1, label='1M', step='month', stepmode='backward'),
                        dict(count=6, label='6M', step='month', stepmode='backward'),
                        dict(count=1, label='YTD', step='year', stepmode='todate'),
                        dict(count=1, label='1A', step='year', stepmode='backward'),
                        dict(label='Máx.', step='all')
                    ]))
            )

            st.plotly_chart(fig_silver, use_container_width=True)

        with st.expander('Más información)'):

            st.write('''
                Fuente: Banco Central de Reserva del Perú.
                
                Silver futures are standardized, exchange-traded contracts in which the contract buyer agrees to take delivery, from the seller, a specific quantity of silver at a predetermined price on a future delivery date. Though its use as the nation's coinage was discontinued in 1965, at the turn of the century, an even more important economic function emerged for silver: that of an industrial raw material. Today, silver is sought as a valuable and practical industrial commodity, and silver futures are seen as an appealing investment that can be traded nearly 24 hours per day, 6 days per week. The largest industrial users of silver are the photographic, jewelry, and electronic industries. Silver futures are available for trading in the COMEX Division at the New York Mercantile Exchange (NYMEX).
                ''')

    with comm1[1]:

        st.write('**Trigo (cUS$/bushel)**')

        wheat_chart = st.selectbox('Seleccione el tipo de gráfico', ('Gráfico de línea', 'Gráfico OHLC + Volumen'), key='wheat_key')

        if wheat_chart == 'Gráfico de línea':

            fig_wheat = go.Figure()

            fig_wheat.add_trace(
                go.Line(
                    name='Trigo (US$/bushel)',
                    x=wheat_fut['Date'],
                    y=wheat_fut['Close'],
                    line=dict(color=color_rojo)
                ))

            fig_wheat.update_layout(
                {'plot_bgcolor': color_blanco, 'paper_bgcolor': color_blanco},
                font=dict(family='arial'),
                font_size=14,
                margin=dict(l=0, r=0, t=0, b=0)
            )

            fig_wheat.update_yaxes(title='cUS$')

            fig_wheat.update_xaxes(
                title='Fecha',
                # rangeslider_visible=True,
                rangeselector=dict(
                    buttons=list([
                        dict(count=3, label='3D', step='day', stepmode='backward'),
                        dict(count=5, label='1S', step='day', stepmode='backward'),
                        dict(count=1, label='1M', step='month', stepmode='backward'),
                        dict(count=6, label='6M', step='month', stepmode='backward'),
                        dict(count=1, label='YTD', step='year', stepmode='todate'),
                        dict(count=1, label='1A', step='year', stepmode='backward'),
                        dict(label='Máx.', step='all')
                    ]))
            )

            st.plotly_chart(fig_wheat, use_container_width=True)

        elif wheat_chart == 'Gráfico OHLC + Volumen':

            fig_wheat = make_subplots(
                rows=2,
                cols=1,
                shared_xaxes=True,
                vertical_spacing=0.03,
                # subplot_titles=('OLHC', 'Volumen'),
                row_width=[0.2, 0.7]
            )

            fig_wheat.add_trace(
                go.Candlestick(
                    x=wheat_fut['Date'],
                    open=wheat_fut['Open'],
                    high=wheat_fut['High'],
                    low=wheat_fut['Low'],
                    close=wheat_fut['Close'],
                    name='OLHC',
                    showlegend=False
                ),
                row=1,
                col=1
            )

            fig_wheat.add_trace(
                go.Bar(
                    x=wheat_fut['Date'],
                    y=wheat_fut['Volume'],
                    showlegend=False,
                    name='Volumen'
                ),
                row=2,
                col=1
            )

            fig_wheat.update(layout_xaxis_rangeslider_visible=False)

            fig_wheat.update_layout(
                {'plot_bgcolor': color_blanco, 'paper_bgcolor': color_blanco},
                font=dict(family='arial'),
                font_size=12,
                margin=dict(l=0, r=0, t=0, b=0)
            )

            fig_wheat.update_xaxes(
                rangebreaks=[dict(bounds=["sat", "mon"])],
                rangeselector=dict(
                    buttons=list([
                        dict(count=3, label='3D', step='day', stepmode='backward'),
                        dict(count=5, label='1S', step='day', stepmode='backward'),
                        dict(count=1, label='1M', step='month', stepmode='backward'),
                        dict(count=6, label='6M', step='month', stepmode='backward'),
                        dict(count=1, label='YTD', step='year', stepmode='todate'),
                        dict(count=1, label='1A', step='year', stepmode='backward'),
                        dict(label='Máx.', step='all')
                    ]))
            )

            st.plotly_chart(fig_wheat, use_container_width=True)

        with st.expander('Más información'):

            st.write('''
                Fuente: Banco Central de Reserva del Perú.
                
                Representing the majority of the U.S. wheat crop, Hard Red Winter wheat is the primary ingredient in the world’s production of bread. KC HRW Wheat futures are by no means new; in fact, they’ve traded since 1876 – longer than the Chicago SRW Wheat futures. However, what market participants are noticing as of late is newfound liquidity. Bid-ask spread, market depth and breadth of participants have improved dramatically. Trades at the Chicago Board of Trade (CBOT - CME Group).
                ''')

    # SILVER Y TRIGO

    comm2 = st.columns(2)

    with comm2[0]:

        st.write('**Maíz (cUS$/bushel)**')

        corn_chart = st.selectbox('Seleccione el tipo de gráfico', ('Gráfico de línea', 'Gráfico OHLC + Volumen'), key='corn_key')

        if corn_chart == 'Gráfico de línea':

            fig_corn = go.Figure()

            fig_corn.add_trace(
                go.Line(
                    name='Maíz (cUS$/bushel)',
                    x=corn_fut['Date'],
                    y=corn_fut['Close'],
                    line=dict(color=color_azul)
                ))

            fig_corn.update_layout(
                {'plot_bgcolor': color_blanco, 'paper_bgcolor': color_blanco},
                font=dict(family='arial'),
                font_size=14,
                margin=dict(l=0, r=0, t=0, b=0)
            )

            fig_corn.update_yaxes(title='cUS$')

            fig_corn.update_xaxes(
                title='Fecha',
                # rangeslider_visible=True,
                rangeselector=dict(
                    buttons=list([
                        dict(count=3, label='3D', step='day', stepmode='backward'),
                        dict(count=5, label='1S', step='day', stepmode='backward'),
                        dict(count=1, label='1M', step='month', stepmode='backward'),
                        dict(count=6, label='6M', step='month', stepmode='backward'),
                        dict(count=1, label='YTD', step='year', stepmode='todate'),
                        dict(count=1, label='1A', step='year', stepmode='backward'),
                        dict(label='Máx.', step='all')
                    ]))
            )

            st.plotly_chart(fig_corn, use_container_width=True)

        elif corn_chart == 'Gráfico OHLC + Volumen':

            fig_corn = make_subplots(
                rows=2,
                cols=1,
                shared_xaxes=True,
                vertical_spacing=0.03,
                # subplot_titles=('OLHC', 'Volumen'),
                row_width=[0.2, 0.7]
            )

            fig_corn.add_trace(
                go.Candlestick(
                    x=corn_fut['Date'],
                    open=corn_fut['Open'],
                    high=corn_fut['High'],
                    low=corn_fut['Low'],
                    close=corn_fut['Close'],
                    name='OLHC',
                    showlegend=False
                ),
                row=1,
                col=1
            )

            fig_corn.add_trace(
                go.Bar(
                    x=corn_fut['Date'],
                    y=corn_fut['Volume'],
                    showlegend=False,
                    name='Volumen'
                ),
                row=2,
                col=1
            )

            fig_corn.update(layout_xaxis_rangeslider_visible=False)

            fig_corn.update_layout(
                {'plot_bgcolor': color_blanco, 'paper_bgcolor': color_blanco},
                font=dict(family='arial'),
                font_size=12,
                margin=dict(l=0, r=0, t=0, b=0)
            )

            fig_corn.update_xaxes(
                rangebreaks=[dict(bounds=["sat", "mon"])],
                rangeselector=dict(
                    buttons=list([
                        dict(count=3, label='3D', step='day', stepmode='backward'),
                        dict(count=5, label='1S', step='day', stepmode='backward'),
                        dict(count=1, label='1M', step='month', stepmode='backward'),
                        dict(count=6, label='6M', step='month', stepmode='backward'),
                        dict(count=1, label='YTD', step='year', stepmode='todate'),
                        dict(count=1, label='1A', step='year', stepmode='backward'),
                        dict(label='Máx.', step='all')
                    ]))
            )

            st.plotly_chart(fig_corn, use_container_width=True)

        with st.expander('Más información'):

            st.write('''
                Fuente: Banco Central de Reserva del Perú.
                
                Corn futures are the most liquid and active market in grains, with 350,000 contracts traded per day. Trades at the Chicago Board of Trade (CBOT- CME Group).
                ''')

    with comm2[1]:

        st.write('**Aceite de soya (cUS$/lb)**')

        soybean_chart = st.selectbox('Seleccione el tipo de gráfico', ('Gráfico de línea', 'Gráfico OHLC + Volumen'), key='soybean_key')

        if soybean_chart == 'Gráfico de línea':

            fig_soybean = go.Figure()

            fig_soybean.add_trace(
                go.Line(
                    name='Aceite de soya (cUS$/lb)',
                    x=soybean_fut['Date'],
                    y=soybean_fut['Close'],
                    line=dict(color=color_rojo)
                ))

            fig_soybean.update_layout(
                {'plot_bgcolor': color_blanco, 'paper_bgcolor': color_blanco},
                font=dict(family='arial'),
                font_size=14,
                margin=dict(l=0, r=0, t=0, b=0)
            )

            fig_soybean.update_yaxes(title='cUS$')

            fig_soybean.update_xaxes(
                title='Fecha',
                # rangeslider_visible=True,
                rangeselector=dict(
                    buttons=list([
                        dict(count=3, label='3D', step='day', stepmode='backward'),
                        dict(count=5, label='1S', step='day', stepmode='backward'),
                        dict(count=1, label='1M', step='month', stepmode='backward'),
                        dict(count=6, label='6M', step='month', stepmode='backward'),
                        dict(count=1, label='YTD', step='year', stepmode='todate'),
                        dict(count=1, label='1A', step='year', stepmode='backward'),
                        dict(label='Máx.', step='all')
                    ]))
            )

            st.plotly_chart(fig_soybean, use_container_width=True)

        elif soybean_chart == 'Gráfico OHLC + Volumen':

            fig_soybean = make_subplots(
                rows=2,
                cols=1,
                shared_xaxes=True,
                vertical_spacing=0.03,
                # subplot_titles=('OLHC', 'Volumen'),
                row_width=[0.2, 0.7]
            )

            fig_soybean.add_trace(
                go.Candlestick(
                    x=soybean_fut['Date'],
                    open=soybean_fut['Open'],
                    high=soybean_fut['High'],
                    low=soybean_fut['Low'],
                    close=soybean_fut['Close'],
                    name='OLHC',
                    showlegend=False
                ),
                row=1,
                col=1
            )

            fig_soybean.add_trace(
                go.Bar(
                    x=soybean_fut['Date'],
                    y=soybean_fut['Volume'],
                    showlegend=False,
                    name='Volumen'
                ),
                row=2,
                col=1
            )

            fig_soybean.update(layout_xaxis_rangeslider_visible=False)

            fig_soybean.update_layout(
                {'plot_bgcolor': color_blanco, 'paper_bgcolor': color_blanco},
                font=dict(family='arial'),
                font_size=12,
                margin=dict(l=0, r=0, t=0, b=0)
            )

            fig_soybean.update_xaxes(
                rangebreaks=[dict(bounds=["sat", "mon"])],
                rangeselector=dict(
                    buttons=list([
                        dict(count=3, label='3D', step='day', stepmode='backward'),
                        dict(count=5, label='1S', step='day', stepmode='backward'),
                        dict(count=1, label='1M', step='month', stepmode='backward'),
                        dict(count=6, label='6M', step='month', stepmode='backward'),
                        dict(count=1, label='YTD', step='year', stepmode='todate'),
                        dict(count=1, label='1A', step='year', stepmode='backward'),
                        dict(label='Máx.', step='all')
                    ]))
            )

            st.plotly_chart(fig_soybean, use_container_width=True)

        with st.expander('Más información'):

            st.write('''
                Fuente: Banco Central de Reserva del Perú.
                
                Soybean futures are an easy, liquid tool for speculating or hedging against price movements for one of the world’s most widely grown crops. Seek rewards, manage risks and diversify your portfolio. Our global contracts enable you to trade around the new crop of the northern hemisphere in November and the South American new crop in May. Trades at the Chicago Board of Trade (CBOT - CME Group).
                ''')

# TIPO DE CAMBIO

with main_tabs[2]:

    st.subheader('Tipo de cambio')
