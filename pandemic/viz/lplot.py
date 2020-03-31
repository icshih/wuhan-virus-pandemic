import logging

import plotly.graph_objects as go

logger = logging.getLogger("lplot")


def plot_country_state(country, date, cases, province=""):
    data_state = cases[province + "/" + country]
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=date, y=data_state, marker=dict(symbol="circle"), name=province + "/" + country))
    fig.update_traces(mode='lines+markers', showlegend=True, line=dict(shape="spline", smoothing=0.2))
    fig.update_xaxes(title=dict(text="Date"), type="date", autorange=False, range=[date[0], date[-1]])
    fig.update_yaxes(title=dict(text="Number of Confirmed Cases"), type="log", range=[0, 5])
    fig.update_layout(width=1000,
                      height=600,
                      margin=dict(l=20, r=20, t=50, b=20),
                      plot_bgcolor="WhiteSmoke",
                      paper_bgcolor="LightSteelBlue",)
    return fig


def plot_countries(country_list, date, cases):
    fig = go.Figure()
    for c in country_list:
        key = "/"+c
        try:
            cases_in_country = cases[key]
            fig.add_trace(go.Scatter(x=date, y=cases_in_country, marker=dict(symbol="circle"), name=c))
        except KeyError:
            logger.warning(key + " is not found in the data.")
    fig.update_traces(mode='lines+markers', showlegend=True, line=dict(shape="spline", smoothing=0.2))
    fig.update_xaxes(title=dict(text="Date"), type="date", autorange=False, range=[date[0], date[-1]])
    fig.update_yaxes(title=dict(text="Number of Confirmed Cases"), type="log", range=[0, 5])
    fig.update_layout(width=1000,
                      height=600,
                      margin=dict(l=20, r=20, t=50, b=20),
                      plot_bgcolor="WhiteSmoke",
                      paper_bgcolor="LightSteelBlue",)
    return fig


def plots(date, cases):
    fig = go.Figure()
    for n, v in cases.items():
        fig.add_trace(go.Scatter(x=date, y=v, marker=dict(symbol="circle-open"), name=n))
    fig.update_traces(mode='lines+markers', showlegend=True, line=dict(shape="spline", smoothing=0.2))
    fig.update_xaxes(title=dict(text="Date"), type="date", autorange=False, range=[date[0], date[-1]])
    fig.update_yaxes(title=dict(text="Number of Confirmed Cases"), type="log", range=[0, 5])
    fig.update_layout(width=1000,
                      height=600,
                      margin=dict(l=20, r=20, t=50, b=20),
                      plot_bgcolor="WhiteSmoke",
                      paper_bgcolor="LightSteelBlue", )
    return fig
