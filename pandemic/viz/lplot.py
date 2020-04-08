import logging

import plotly.graph_objects as go
import numpy as np

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


def plot2_countries(country_data_list):
    fig = go.Figure()
    for c, d in country_data_list.items():
        fig.add_trace(go.Scatter(x=d.df.index, y=d.df[c], marker=dict(symbol="circle"), name=c))
    fig.update_traces(mode='lines+markers', showlegend=True, line=dict(shape="spline", smoothing=0.2))
    fig.update_xaxes(title=dict(text="Date"), type="date")
    fig.update_yaxes(title=dict(text="Number of Confirmed Cases"), type="log", range=[0, 5])
    fig.update_layout(width=1000,
                      height=600,
                      margin=dict(l=20, r=20, t=50, b=20),
                      plot_bgcolor="WhiteSmoke",
                      paper_bgcolor="LightSteelBlue",)


def plot_figure_country_region(df):
    rangeUpper = 5.0
    max_scale = np.log10(df.iloc[-1,].max())
    if max_scale > rangeUpper:
        rangeUpper = max_scale
    fig = go.Figure()
    for c in df.columns:
        fig.add_trace(go.Scatter(x=df.index, y=df[c], line=dict(width=4), name=c))
    fig.update_traces(mode='lines', showlegend=True, line=dict(shape="spline", smoothing=0.5))
    fig.update_xaxes(title=dict(text="Date"), type="date", autorange=False, range=[df.index[0], df.index[-1]])
    fig.update_yaxes(title=dict(text="Number of Confirmed Cases"), type="log", range=[0.0, rangeUpper])
    fig.update_layout(width=1000, height=600,
                      margin=dict(l=20, r=20, t=50, b=20),
                      plot_bgcolor="WhiteSmoke",
                      paper_bgcolor="LightSteelBlue", )
    return fig


def plot_confirmed_death_recovered_by(df):
    rangeUpper = 5.0
    max_scale = np.log10(df["Confirmed"][-1])
    if max_scale > rangeUpper:
        rangeUpper = max_scale
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df.index, y=df["Confirmed"],line=dict(width=4), name="Confirmed", fill="tonexty", mode="none"))
    fig.add_trace(go.Scatter(x=df.index, y=df["Death"],line=dict(width=4), name="Deaths", fill="tozeroy", mode="none"))
    fig.add_trace(go.Scatter(x=df.index, y=df["Recovered"],line=dict(width=4), name="Recovered", fill="tozeroy", mode="none"))
    fig.update_xaxes(title=dict(text="Date"), type="date", autorange=False, range=[df.index[0], df.index[-1]])
    fig.update_yaxes(title=dict(text="Number of Cases"), type="log", range=[0.0, rangeUpper])
    fig.update_layout(width=1000, height=600,
                      margin=dict(l=20, r=20, t=50, b=20),
                      plot_bgcolor="WhiteSmoke",
                      paper_bgcolor="LightSteelBlue", )
    return fig


def plot_figure_country_case_daily(df):
    fig = go.Figure()
    if df.columns.size == 1:
        country = df.columns[0]
        new_cases = df[country].iloc[1:].values - df[country].iloc[:-1].values
        fig.add_trace(go.Bar(x=df.index, y=new_cases, name=country))
        fig.update_xaxes(title=dict(text="Date"), type="date", autorange=False, range=[df.index[0], df.index[-1]])
        fig.update_yaxes(title=dict(text="Number of New Cases"))
        fig.update_layout(width=1000, height=600,
                      margin=dict(l=20, r=20, t=50, b=20),
                      plot_bgcolor="WhiteSmoke",
                      paper_bgcolor="LightSteelBlue", )
    return fig


def plot_figure_of(df, province):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df.index, y=df[province], marker=dict(symbol="circle"), name=province))
    fig.update_traces(mode='lines+markers', showlegend=True, line=dict(shape="spline", smoothing=0.2))
    fig.update_xaxes(title=dict(text="Date"), type="date", autorange=False, range=[df.index[0], df.index[-1]])
    fig.update_yaxes(title=dict(text="Number of Confirmed Cases"), type="log", range=[0, 5])
    fig.update_layout(width=1000, height=600,
            margin=dict(l=20, r=20, t=50, b=20),
            plot_bgcolor="WhiteSmoke",
            paper_bgcolor="LightSteelBlue",)
    return fig


def plot_all_figures(df):
    fig = go.Figure()
    for c in df.columns:
        fig.add_trace(go.Scatter(x=df.index, y=df[c], marker=dict(symbol="circle"), name=c))
    fig.update_traces(mode='lines+markers', showlegend=True, line=dict(shape="spline", smoothing=0.2))
    fig.update_xaxes(title=dict(text="Date"), type="date")
    fig.update_yaxes(title=dict(text="Number of Confirmed Cases"), type="log", range=[0, 5])
    fig.update_layout(width=1000,
                      height=600,
                      margin=dict(l=20, r=20, t=50, b=20),
                      plot_bgcolor="WhiteSmoke",
                      paper_bgcolor="LightSteelBlue",)
    return fig
