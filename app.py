# -*- coding: utf-8 -*-
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from pandemic.web.Tools import Tools
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

#global_confirmed = "data/time_series_covid19_confirmed_global.csv"
#global_deaths = "data/time_series_covid19_deaths_global.csv"
#global_recovered = "data/time_series_covid19_recovered_global.csv"

global_confirmed = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
global_deaths = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv"
global_recovered = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv"

wh = Tools(global_confirmed, global_deaths, global_recovered)
dropdown = wh.create_country_dropdown()

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.COSMO])

server = app.server

multi_select_form = dbc.FormGroup(
    [
        dbc.Label("Select Countries:"),
        dcc.Dropdown(
            id="select_countries",
            options=dropdown,
            value=["Taiwan", "France"],
            multi=True)
    ]
)

# default dash-core-component
# multi_select = dcc.Dropdown(
#     id="select_countries",
#     options=dropdown,
#     value=["Taiwan*", "France"],
#     multi=True
# )

markdown_text = '''
The daily evolution of COVID-19 pandemic country by country since 22 January 2020.
'''

markdown_info = '''
**Declaim**: The time series data is retrieved daily from data repository for the 
[2019 Novel Coronavirus Visual Dashboard](https://github.com/CSSEGISandData/COVID-19) 
operated by the Johns Hopkins University Center for Systems Science and Engineering ([JHU CSSE](https://systems.jhu.edu)).
This website is strictly for personal learning purpose; the information presented here IS NOT for any medical
or policy guidance. Viewers SHALL consult the precise epidemic data from the official sources of each country.
'''

markdown_credit = '''
Page created by [I-Chun Shih](http://www.linkedin.com/in/icshih)@2020
'''

app.layout = dbc.Container(
    [
        html.H1("Coronavirus COVID-19 (a.k.a. Wuhan Virus)"),
        html.H2("嚴重特殊傳染性肺炎 COVID-19 (武漢肺炎)"),
        html.Div(
            [
                dcc.Markdown(children=markdown_text)
            ]),


        html.Hr(),

        dbc.Row(
          [
              dbc.Col(multi_select_form, md=2),
              dbc.Col(dcc.Graph(id="plot_countries"), md=10),
          ]
        ),

        html.Hr(),
        html.Div(
            [
                dcc.Markdown(children=markdown_info)
            ]
        ),

        html.Hr(),
        html.Div(
            [
                dcc.Markdown(children=markdown_credit)
            ]
        ),
    ],
    fluid=True,
)


@app.callback(
    Output(component_id='plot_countries', component_property='figure'),
    [Input(component_id='select_countries', component_property='value')])
def plot_countries(input_value):
    return wh.select_countries(input_value)


if __name__ == '__main__':
    app.run_server(debug=True)
