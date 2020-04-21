# -*- coding: utf-8 -*-
import json
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from pandemic.web.Tools import Tools
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

global_confirmed = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
global_deaths = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv"
global_recovered = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv"

wh = Tools(global_confirmed, global_deaths, global_recovered)
dropdown = wh.create_country_dropdown()

appTest = dash.Dash(__name__, external_stylesheets=[dbc.themes.COSMO])
appTest.config.suppress_callback_exceptions = True
appTest.title = "COVID-19 Pandemic"
server = appTest.server

config = {'modeBarButtonsToRemove': ['hoverClosestCartesian',
                                     'zoom2d', 'hoverCompareCartesian', 'zoomInGeo', 'zoomOutGeo',
                                     'hoverClosestGeo', 'hoverClosestGl2d', 'toggleHover',
                                     'zoomInMapbox', 'zoomOutMapbox', 'toggleSpikelines'],
          'displaylogo': False}

markdown_declaim_author = '''
**Declaim**: The time series data is retrieved daily from data repository for the 
[2019 Novel Coronavirus Visual Dashboard](https://github.com/CSSEGISandData/COVID-19) 
operated by the Johns Hopkins University Center for Systems Science and Engineering ([JHU CSSE](https://systems.jhu.edu)).
This website is strictly for personal learning purpose; the information presented here IS NOT for any medical
or policy guidance. Viewers SHALL consult the precise epidemic data from the official sources of each country.

---

Page created by [I-Chun Shih](http://www.linkedin.com/in/icshih)@2020

'''

title_info = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H1("Coronavirus COVID-19 Pandemic", className="p-4 bg-primary text-white"),
                    ]),
                dbc.Col(
                    [
                        html.H1("嚴重特殊傳染性肺炎 (武漢肺炎)", className="p-4 bg-primary text-white text-right"),
                    ], width="auto"),
            ], className="mt-3 mb-5 mx-5", no_gutters=True,
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.P("Following the daily evolution of the pandemic country by country since 22 January 2020.",
                               className="lead", style={"font-size": "200%"}),
                    ]
                )
            ], className="mt-3 mb-5 mx-5",
        ),
    ], id="title_info", fluid=True,
)

country_evolution = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        dcc.Dropdown(id="select_countries", options=dropdown, value=["Taiwan", "France"],
                                     placeholder="Select Countries", multi=True, className="my-2")
                    ], className="col-2",
                ),
                dbc.Col(
                    [
                        dcc.Graph(id="plot_countries_infection_rate", config=config, className="ml-2 my-2")

                    ], className="col-10",
                ),
            ], className="mb-5 mx-5"
        ),
    ], id="country_view", fluid=True,
)

declaim_author = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        dcc.Markdown(children=markdown_declaim_author, style={"font-size": "140%"}),
                    ]
                )
            ], className="mb-5 mx-5"
        ),
    ], id="declaim_author_view", fluid=True,
)

appTest.layout = html.Div([
    title_info,
    country_evolution,
    declaim_author
])


@appTest.callback(
    Output(component_id='plot_countries_infection_rate', component_property='figure'),
    [Input(component_id='select_countries', component_property='value'),
     Input("plot_countries_infection_rate", "clickData")])
def plot_countries_with_infection_rate(input_value, click_data):
    if click_data is None:
        return wh.select_countries(input_value)
    else:
        curve0 = click_data["points"][0]
        date = curve0["x"]
        return wh.select_countries(input_value, date)


if __name__ == '__main__':
    appTest.run_server(debug=True)
