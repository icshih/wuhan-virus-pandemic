# -*- coding: utf-8 -*-
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from pandemic.web.tools import Tools

wh = Tools(
    "/Users/icshih/Programs/projects/WuhanVirus/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv")
dropdown = wh.create_country_dropdown()

# external_stylesheets = ['https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css']
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

# dash-bootstrap-component
select = dbc.Select(
    id="select_country",
    options=dropdown,
    value="France"
)

# default dash-core-component
select2 = dcc.Dropdown(
    id="select_country",
    options=dropdown,
    value='France'
)

app.layout = dbc.Container(
    [
        html.H1("Coronavirus COVID-19 (a.k.a. Wuhan Virus)"),
        html.P("This simple application follows the daily progress of the virus in each country. "
               "The data is collected and organised by the Johns Hopkins University Center for "
               "Systems Science and Engineering (JHU CSSE)."),

        dbc.Row(
            [
                dbc.Label("Country"),
                dbc.Col(select, md=4),
            ],
            align="center",
        ),
        dbc.Row(
            [
                dbc.Col(dcc.Graph(id="plot_country"), md=8)
            ],
        ),
    ],
    fluid=True,
)


# html.Div(children=[
#     html.H1(children='嚴重特殊傳染性肺炎 COVID-19 (武漢肺炎)'),
#     html.P(children="全球武漢肺炎發展趨勢"),
#     html.Div(children='''
#         COVID-19累計確診案例
#     '''),
#     html.Label("國家 (Country)"),
#     dcc.Dropdown(
#         id="select_country",
#         options=dropdown,
#         value='France'
#     ),
#     dcc.Graph(id="plot_country")
# ])


@app.callback(
    Output(component_id='plot_country', component_property='figure'),
    [Input(component_id='select_country', component_property='value')])
def plot_the_country(input_value):
    return wh.select_country(input_value)


if __name__ == '__main__':
    app.run_server(debug=True)
