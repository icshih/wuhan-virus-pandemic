import plotly.graph_objects as go


def plot_country_state(country, date, cases, province=""):
    data_state = cases[province + "/" + country]
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=date, y=data_state, marker=dict(symbol="circle-open"), name=province + "/" + country))
    fig.update_traces(mode='lines+markers', showlegend=True)
    fig.update_xaxes(title=dict(text="Date"), type="date", autorange=False, range=[date[0], date[-1]])
    fig.update_yaxes(title=dict(text="Number of Confirmed Cases"), type="log", range=[0, 5])
    fig.update_layout(title=dict(text="Wuhan Virus 武漢肺炎 2020 "))
    fig.show()


def plots(date, cases):
    fig = go.Figure()
    for n, v in cases.items():
        fig.add_trace(go.Scatter(x=date, y=v, marker=dict(symbol="circle-open"), name=n))
    fig.update_traces(mode='lines+markers', showlegend=True)
    fig.update_xaxes(title=dict(text="Date"), type="date", autorange=False, range=[date[0], date[-1]])
    fig.update_yaxes(title=dict(text="Number of Confirmed Cases"), type="log", range=[0, 5])
    fig.update_layout(title=dict(text="Wuhan Virus 武漢肺炎 2020 "))
    fig.show()
