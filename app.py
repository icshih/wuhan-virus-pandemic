# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from pandemic.data.wuhanvirus import WuhanTimeSeries as wts

path_wv_time_series = "/Users/icshih/Programs/projects/WuhanVirus/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
wvts = wts(path_wv_time_series)


def create_country_dropdown():
    dropdown = list()
    countries = wvts.get_country_list()
    for n in countries:
        dropdown.append({"label": n, "value": n})
    return dropdown


def select_country(country):
    return wvts.get_country(country).get_figure()


dropdown = create_country_dropdown()

external_stylesheets = ['https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='嚴重特殊傳染性肺炎 COVID-19 (武漢肺炎)'),

    html.P(children="全球武漢肺炎發展趨勢"),


    html.Div(children='''
        COVID-19累計確診案例
    '''),

    html.Label("國家 (Country)"),
    dcc.Dropdown(
        options=dropdown,
        value='France'
    ),

    dcc.Graph(
        id='example-graph',
        figure=select_country("Taiwan*")
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)