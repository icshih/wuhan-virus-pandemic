import logging

import plotly.graph_objects as go
import numpy as np
import pandas as pd
from pandemic.data.Analytics import fit, func

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
                      paper_bgcolor="LightSteelBlue", )
    return fig


def plot_countries(country_list, date, cases):
    fig = go.Figure()
    for c in country_list:
        key = "/" + c
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
                      paper_bgcolor="LightSteelBlue", )
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
                      paper_bgcolor="LightSteelBlue", )


def plot_figure_country_region(df):
    """
    Used by Tools
    :param df:
    :return:
    """
    rangeUpper = 5.0
    max_scale = np.log10(df.iloc[-1,].max())
    if max_scale > rangeUpper:
        rangeUpper = max_scale
    fig = go.Figure()
    for c in df.columns:
        fig.add_trace(go.Scatter(x=df.index, y=df[c], name=c,
                                 line=dict(width=4), hovertemplate="%{x}<br>Cases: %{y:d}", hoverinfo="x+text"))
    fig.update_traces(mode='lines', line=dict(shape="spline", smoothing=0.5))
    fig.update_xaxes(title=dict(text="Date", font=dict(size=16)),
                     type="date", autorange=False, range=[df.index[0], df.index[-1]],
                     ticks="inside")
    fig.update_yaxes(visible=True, title=dict(text="Number of Confirmed Cases", font=dict(size=16)),
                     type="log", autorange=True, range=[0.0, rangeUpper], showgrid=True, gridcolor="#eee",
                     ticks="inside", tickson="labels")
    fig.update_layout(
        showlegend=True, legend=dict(font=dict(size=14)),
        margin=dict(l=20, r=20, t=50, b=50),
        plot_bgcolor="white",
        paper_bgcolor="white", )
    return fig


def plot_figure_confirmed_100_plus(df):
    """
    Used by Tools
    Plot the evolution of confirmed cases after the days with more than 100 cases.
    :param df: The DataFrome with countries as columns.
    :return:
    """
    range_upper = 5.0
    max_scale = np.log10(df.iloc[-1,].max())
    if max_scale > range_upper:
        range_upper = max_scale
    fig = go.Figure()
    longest_day = 0
    for c in df.columns:
        cty = df[c]
        hundred = cty[cty > 100]
        days = np.arange(len(hundred))
        if len(days) > longest_day:
            longest_day = len(days)
        fig.add_trace(go.Scatter(x=days, y=hundred, name=c,
                                 line=dict(width=4), hovertemplate="Days: %{x}<br>Cases: %{y:d}", hoverinfo="x+text"))
    fig.update_traces(mode='lines', line=dict(shape="spline", smoothing=0.5))
    fig.update_xaxes(title=dict(text="Days After 100+ Cases", font=dict(size=16)),
                     autorange=False, range=[0, longest_day],
                     ticks="inside")
    fig.update_yaxes(visible=True, title=dict(text="Number of Confirmed Cases", font=dict(size=16)),
                     type="log", autorange=True, range=[0.0, range_upper], showgrid=True, gridcolor="#eee",
                     ticks="inside", tickson="labels")
    fig.update_layout(
        showlegend=True, legend=dict(font=dict(size=14)),
        margin=dict(l=20, r=20, t=50, b=50),
        plot_bgcolor="white",
        paper_bgcolor="white", )
    return fig


def plot_confirmed_death_recovered_by(df):
    rangeUpper = 5.0
    max_scale = np.log10(df["Confirmed"][-1])
    if max_scale > rangeUpper:
        rangeUpper = max_scale
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(x=df.index, y=df["Confirmed"], name="Confirmed", line=dict(width=4), fill="tonexty", mode="none"))
    fig.add_trace(go.Scatter(x=df.index, y=df["Death"], name="Deaths", line=dict(width=4), fill="tozeroy", mode="none"))
    fig.add_trace(
        go.Scatter(x=df.index, y=df["Recovered"], name="Recovered", line=dict(width=4), fill="tozeroy", mode="none"))
    fig.update_xaxes(title=dict(text="Date", font=dict(size=16)),
                     type="date", autorange=False, range=[df.index[0], df.index[-1]],
                     ticks="inside")
    fig.update_yaxes(visible=True, title=dict(text="Number of Cases", font=dict(size=16)),
                     type="log", range=[0.0, rangeUpper], showgrid=True, gridcolor="#eee",
                     ticks="inside", tickson="labels")
    fig.update_layout(
        showlegend=True, legend=dict(font=dict(size=14)),
        margin=dict(l=20, r=20, t=50, b=50),
        plot_bgcolor="white",
        paper_bgcolor="white", )
    return fig


def plot_confirmed_infection_rate(df, date=None, period=7):
    """
    Used by Tools
    :param df:
    :param date: None or Date type
    :param period:
    :return:
    """
    # Adjust maximum value at y-axis
    rangeUpper = 5.0
    max_scale = np.log10(df["Confirmed"][-1])
    if max_scale > rangeUpper:
        rangeUpper = max_scale
    fig = go.Figure()

    fig.add_trace(
        go.Scatter(x=df.index, y=df["Confirmed"], name="Confirmed",
                   line=dict(width=4), fill="tonexty", fillcolor="#DCDCDC", mode="none",
                   hovertemplate="%{x}<br>Cases: %{y:d}", hoverinfo="x+text"))
    fig.add_trace(
        go.Scatter(x=df.index, y=df["Recovered"], name="Recovered",
                   line=dict(width=4), fill="tonexty", fillcolor="#C0C0C0", mode="none",
                   hovertemplate="%{x}<br>Cases: %{y:d}", hoverinfo="x+text"))
    fig.add_trace(
        go.Scatter(x=df.index, y=df["Death"], name="Deaths",
                   line=dict(width=4), fill="tozeroy", fillcolor="#808080", mode="none",
                   hovertemplate="%{x}<br>Cases: %{y:d}", hoverinfo="x+text"))

    if date is not None:
        confirmed = df["Confirmed"]
        x_date, popt, pcov = fit(confirmed, date, period)
        # Create predicted data
        cf_pred = confirmed[x_date[0]:confirmed.index[-1]]
        y_pred_model = 10 ** func(range(len(cf_pred)), *popt)
        cf_model = pd.Series(y_pred_model, index=cf_pred.index)
        # On_Date
        on_date = cf_model.iloc[0:period + 1]
        # Off_Date
        off_date = cf_model.iloc[period:]

        if popt[1] > 0.0:
            infect_rate = "20% new cases in <i>" + str(round(0.2 / popt[1])) + "</i> days*"
            fig.add_trace(
                go.Scatter(x=off_date.index, y=off_date, mode='lines', name="Projected",
                           line=dict(color='Black', width=4, dash='dot'),
                           showlegend=False, hovertemplate="%{x}<br>Projected Cases: %{y:.0f}", hoverinfo="x+text"))
        else:
            infect_rate = "No new cases"

        fig.add_trace(
            go.Scatter(x=on_date.index, y=on_date, mode='lines', name="Fitted",
                       line=dict(color='Black', width=4),
                       showlegend=False, hovertemplate="%{x}<br>" + infect_rate, hoverinfo="x+text"))

    fig.update_xaxes(title=dict(text="Date", font=dict(size=16)),
                     type="date", autorange=False, range=[df.index[0], df.index[-1]],
                     ticks="inside")
    fig.update_yaxes(visible=True, title=dict(text="Number of Cases", font=dict(size=16)),
                     type="log", range=[0.0, rangeUpper], showgrid=True, gridcolor="#eee",
                     ticks="inside", tickson="labels")
    fig.update_layout(
        showlegend=True, legend=dict(font=dict(size=14)),
        margin=dict(l=20, r=20, t=50, b=50),
        plot_bgcolor="white",
        paper_bgcolor="white", )
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
                          plot_bgcolor="white",
                          paper_bgcolor="white", )
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
                      paper_bgcolor="LightSteelBlue", )
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
                      paper_bgcolor="LightSteelBlue", )
    return fig
