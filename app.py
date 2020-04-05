# -*- coding: utf-8 -*-
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from pandemic.web.Tools import Tools

file = "data/time_series_covid19_confirmed_global.csv"

wh = Tools(file)
dropdown = wh.create_country_dropdown()

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

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

app.layout = dbc.Container(
    [
        html.H1("Coronavirus COVID-19 (a.k.a. Wuhan Virus)"),
        html.P("This simple application follows the daily progress of the virus in each country. "
               "The data is collected and organised by the Johns Hopkins University Center for "
               "Systems Science and Engineering (JHU CSSE)."),


        html.Hr(),

        dbc.Row(
          [
              dbc.Col(multi_select_form, md=2),
              dbc.Col(dcc.Graph(id="plot_countries"), md=10),
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
