# IMPORT CONFIGURATIONS
import streamlit as st
# import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import os
# import hydralit_components as hc
# from plotly.subplots import make_subplots
# from plotly_resampler import register_plotly_resampler
import locale
import platform

st.set_page_config(
    layout='wide',
    page_title='Condiciones financieras'
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

# BASES DE PERÚ

bvl_gen = pd.read_feather('mercados/bvl_gen')  # ÍNDICE GENERAL DE LA BVL

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

# SIDEBAR


# RESUMEN

st.title('Información macrofinanciera de Perú')

st.subheader('Resumen de indicadores clave de Perú')

# DELTA PBI

pbi_peru_latest = pbi_peru['Var. % a/a'].iloc[-1]

pbi_peru_t12 = pbi_peru['Var. % a/a'].iloc[-13]

delta_pbi_peru = pbi_peru_latest - pbi_peru_t12

delta_pbi_peru_pct = pbi_peru_latest / pbi_peru_t12 - 1

pbi_peru_latest = "{:,.1f}".format(pbi_peru_latest).replace('.', ',')

delta_pbi_peru_pct = '{:.2%}'.format(delta_pbi_peru_pct).replace('.', ',')

# DELTA INFLACIÓN

inflacion_peru_latest = inflacion_peru['Var. % a/a'].iloc[-1]

inflacion_peru_t12 = inflacion_peru['Var. % a/a'].iloc[-13]

# delta_inflacion_peru = inflacion_peru_latest - inflacion_peru_t12

delta_inflacion_peru = inflacion_peru_latest - 3.00

inflacion_peru_latest = "{:,.2f}".format(inflacion_peru_latest).replace('.', ',')

# DELTA INFLACIÓN SIN ALIMENTOS Y ENERGÍA

inflacion_peru_sub_latest = inflacion_peru_sub['Var. % a/a'].iloc[-1]

inflacion_peru_sub_t12 = inflacion_peru_sub['Var. % a/a'].iloc[-13]

# delta_inflacion_peru_sub = inflacion_peru_sub_latest - inflacion_peru_sub_t12

delta_inflacion_peru_sub = inflacion_peru_sub_latest - 3.00

inflacion_peru_sub_latest = "{:,.2f}".format(inflacion_peru_sub_latest).replace('.', ',')

# DELTA TASA DE REFERENCIA

tasa_bcrp_latest = tasa_bcrp['Tasa %'].iloc[-1]

tasa_bcrp_t2 = tasa_bcrp['Tasa %'].iloc[-2]

delta_tasa_bcrp = (tasa_bcrp_latest - tasa_bcrp_t2) * 100

tasa_bcrp_latest = '{:,.2f}'.format(tasa_bcrp_latest).replace('.', ',')

# DELTA RENDIMIENTO BONO 10 AÑOS PEN

# DELTA RENDIMIENTO BONO 10 AÑOS USD

# DELTA TIPO DE CAMBIO

# DELTA BVL PERÚ GEN

bvl_gen_latest = bvl_gen['Close'].iloc[-1]

bvl_gen_t2 = bvl_gen['Close'].iloc[-2]

delta_bvl_gen = bvl_gen_latest - bvl_gen_t2

delta_bvl_gen_pct = bvl_gen_latest / bvl_gen_t2 - 1

bvl_gen_latest = '{:,.2f}'.format(bvl_gen_latest).replace(',', ' ').replace('.', ',')

delta_bvl_gen_pct = '{:.2%}'.format(delta_bvl_gen_pct).replace('.', ',')

# RESUMEN

per1 = st.columns(4)

per1[0].metric('Producto Bruto Interno', str(pbi_peru_latest) + '% a/a', f'{delta_pbi_peru:.2f}' + ' p.p. a/a')

per1[1].metric('Inflación', str(inflacion_peru_latest) + '% a/a',
               f'{delta_inflacion_peru:.2f}' + ' p.p. sobre el rango meta', delta_color='inverse')

per1[2].metric('Inflación ex. alimentos y energía', str(inflacion_peru_sub_latest) + '% a/a',
               f'{delta_inflacion_peru_sub:.2f}' + ' p.p. sobre el rango meta', delta_color='inverse')

per1[3].metric('Tasa de referencia del BCRP', str(tasa_bcrp_latest) + '%',
               f'{delta_tasa_bcrp:.0f}' + ' puntos básicos m/m', delta_color='inverse')

# BODY

main_tabs = st.tabs(['Macroeconomía', 'Finanzas', 'Finanzas públicas', 'Indicadores adelantados'])

with main_tabs[0]:

    st.subheader('Macroeconomía')

    st.markdown('**Producto Bruto Interno**')

    fig_pbi_peru = go.Figure()

    fig_pbi_peru.add_trace(
        go.Bar(
            name='PBI (var. % a/a)',
            x=pbi_peru['date'],
            y=pbi_peru['Var. % a/a'],
            marker_color=color_azul,
            # line=dict(color=color_azul),
            showlegend=True
        )
    )

    fig_pbi_peru.add_trace(
        go.Line(
            name='Expectativas PBI 12 meses (%)',
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
        title='Fecha',
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

    st.plotly_chart(fig_pbi_peru, use_container_width=True)

    with st.expander('Más información'):
        st.write('''
        Fuente: Banco Central de Reserva del Perú.
            
        PBI peruano
            
        PBI peruano desestacionalizado
            
        PBI peruano desestacionalizado media móvil 3 meses
        ''')

    per2 = st.columns(2)

    with per2[0]:
        st.markdown('**Inflación**')

        fig_inflacion = go.Figure()

        fig_inflacion.add_trace(
            go.Line(
                name='Inflación (Var % a/a)',
                x=inflacion_peru['date'],
                y=inflacion_peru['Var. % a/a'],
                line=dict(color=color_rojo),
                showlegend=True
            )
        )

        fig_inflacion.add_trace(
            go.Line(
                name='Inflación ex. alimentos y energía (Var % a/a)',
                x=inflacion_peru_sub['date'],
                y=inflacion_peru_sub['Var. % a/a'],
                line=dict(color=color_azul),
                showlegend=True
            )
        )

        fig_inflacion.add_trace(
            go.Line(
                name='Expectativas de inflación a 12 meses (%)',
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
                    dict(count=1, label='1A', step='year', stepmode='backward'),
                    dict(count=5, label='5A', step='year', stepmode='backward'),
                    dict(label='Máx.', step='all')
                ]))
        )

        st.plotly_chart(fig_inflacion, use_container_width=True)

        with st.expander('Más información'):
            st.write('''
            Fuente: Banco Central de Reserva del Perú.
            ''')

    with per2[1]:
        st.markdown('**Tasa de referencia de la política monetaria del BCRP**')

        fig_tasa_bcrp = go.Figure()

        fig_tasa_bcrp.add_trace(
            go.Line(
                name='Tasa de referencia BCRP',
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
            title='Fecha',
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

        with st.expander('Más información'):
            st.write('''
            Fuente: Banco Central de Reserva del Perú.
            ''')

    st.markdown('**Expectativas de la economía peruana a 3 y 12 meses**')

    fig_exp_eco = go.Figure()

    fig_exp_eco.add_trace(
        go.Line(
            name='A 3 meses',
            x=exp_eco_3m['date'],
            y=exp_eco_3m['Expectativas a 3 meses'],
            line=dict(color=color_azul),
            showlegend=True
        )
    )

    fig_exp_eco.add_trace(
        go.Line(
            name='A 12 meses',
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
        annotation_text='Tramo optimista',
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
        title='Fecha',
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

    st.plotly_chart(fig_exp_eco, use_container_width=True)

    with st.expander('Más información'):
        st.write('''
        Fuente: Banco Central de Reserva del Perú.
        ''')

    st.markdown('**Desempleo**')
    'BCRP'

with main_tabs[1]:

    st.subheader('Finanzas')

    st.markdown('**6. Tasa de referencia de la política monetaria**')
    'BCRP'

    st.write('**7. Rendimiento del bono a 10 años PEN**')

    st.write('**8. Rendimiento del bono a 10 años USD**')

with main_tabs[2]:

    st.subheader('Indicadores avanzados de coyuntura económica')
