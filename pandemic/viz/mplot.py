import matplotlib.pyplot as plt


def plot_country_state(country, date, cases, province="", xsize=15, ysize=10):
    data_state = cases[province + "/" + country]
    fig, ax = plt.subplots(figsize=(xsize, ysize))
    ax.plot_date(x=date, y=data_state, label=province + "/" + country, marker="o", ls="-")
    ax.set_yscale("log")
    ax.set_ylim(1e0, 1e5)
    ax.set_ylabel("Cases Confirmed")
    ax.set_xlabel("Date")
    ax.xaxis.set_tick_params(rotation=30, labelsize=10)
    ax.legend()
    plt.show()


def plot_countries(country_list, date, cases, xsize=15, ysize=10):
    fig, ax = plt.subplots(figsize=(xsize, ysize))
    for c in country_list:
        ax.plot_date(x=date, y=cases["/" + c], label=c, marker="o", ls="-")
    ax.set_yscale("log")
    ax.set_ylim(1e0, 1e5)
    ax.set_ylabel("Cases Confirmed")
    ax.set_xlabel("Date")
    ax.set_title("Confirmed")
    ax.xaxis.set_tick_params(rotation=30, labelsize=10)
    ax.legend()


def plots(date, cases, xsize=15, ysize=10):
    fig, ax = plt.subplots(figsize=(xsize, ysize))
    for n, v in cases.items():
        ax.plot_date(x=date, y=v, label=n, marker="o", ls="-")
    ax.set_yscale("log")
    ax.set_ylim(1e0, 1e5)
    ax.set_ylabel("Cases Confirmed")
    ax.set_xlabel("Date")
    ax.set_title("Confirmed")
    ax.xaxis.set_tick_params(rotation=30, labelsize=10)
    ax.legend()
    plt.show()
