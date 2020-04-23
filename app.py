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

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.COSMO])
app.config.suppress_callback_exceptions = True
app.title = "COVID-19 Pandemic"
server = app.server

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
                        html.P(
                            "Following the daily evolution of the pandemic country by country.",
                            className="lead", style={"font-size": "200%"}),
                    ]
                )
            ], className="mt-3 mb-5 mx-5",
        ),
    ], id="title_info", fluid=True,
)

country_evolution2 = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        dcc.Dropdown(id="select_countries-2", options=dropdown, value=["Taiwan", "France"],
                                     placeholder="Select Countries", multi=True, className="my-2")
                    ], className="col-2",
                ),
                dbc.Col(
                    [
                        dcc.Graph(id="plot_countries_infection_rate-2", config=config, className="ml-2 my-2")

                    ], className="col-10",
                ),
            ], className="mb-5 mx-5"
        ),
    ], id="country_view", fluid=True,
)

country_evolution = dbc.Container([
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader("Progression", style={"font-size": "200%"}),
                dbc.CardBody([
                    dbc.Row([
                        dbc.Col([
                            dbc.FormGroup([
                                dbc.Label("Country:"),
                                dcc.Dropdown(id="select_countries", options=dropdown,
                                             value=["Taiwan", "France"],
                                             placeholder="Select Countries", multi=True,
                                             className="my-2"),
                            ]),
                            # dbc.FormGroup([
                            #     dbc.Label("Y-Axis Scale:"),
                            #     dbc.Checklist(
                            #         options=[{
                            #             "label": "log", "value": "true"
                            #         }],
                            #         value="true",
                            #         id="switch",
                            #         switch=True)
                            # ]),
                        ], className="col-3"),
                        dbc.Col([
                            dbc.Tabs([
                                dbc.Tab([
                                    dcc.Graph(id="plot_countries_infection_rate", config=config,
                                              style={'height': '50vh'}, className="ml-2 my-2")
                                ], label="Since 22 January 2020"),
                                dbc.Tab([
                                    dcc.Graph(id="plot_country_confirmed_100_plus", config=config,
                                              style={'height': '50vh'}, className="ml-2 my-2")
                                ], label="Since 100+ Confirmed Cases"),
                            ])
                        ], className="col-9", ),
                    ], className="m-2", style={"font-size": "140%"}),
                ])
            ], color="light")
        ]),
    ], className="mb-5 mx-5")
], id="country_view2", fluid=True, )

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

app.layout = html.Div([
    title_info,
    # country_evolution2,
    country_evolution,
    declaim_author
])


@app.callback(
    Output(component_id='plot_countries_infection_rate', component_property='figure'),
    [Input(component_id='select_countries', component_property='value'),
     Input("plot_countries_infection_rate", "clickData")])
def plot_countries_infection_rate(input_value, click_data):
    if click_data is None:
        return wh.select_countries(input_value)
    else:
        curve0 = click_data["points"][0]
        date = curve0["x"]
        return wh.select_countries(input_value, date)


@app.callback(
    Output(component_id='plot_country_confirmed_100_plus', component_property='figure'),
    [Input(component_id='select_countries', component_property='value')])
def plot_country_confirmed_100_plus(input_value):
    return wh.select_countries_100_plus(input_value)


if __name__ == '__main__':
    app.run_server(debug=True)
