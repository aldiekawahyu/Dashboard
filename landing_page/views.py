
from django.shortcuts import render
import plotly
import plotly.graph_objs as go
import json


# Create your views here.
# def index(request):
#     return render(request, "landing_page/login.html")


def index(request):
    # Membuat data untuk plot
    trace = go.Scatter(
        x=[1, 2, 3, 4],
        y=[10, 11, 12, 13],
        mode='lines+markers',
        name='Test Plot'
    )
    layout = go.Layout(
        title='My Plot',
        xaxis=dict(title='x-axis'),
        yaxis=dict(title='y-axis')
    )

    # Mengkonversi plot menjadi JSON
    plot_json = json.dumps({'data': [trace], 'layout': layout},
                           cls=plotly.utils.PlotlyJSONEncoder)

    # Melewatkan JSON ke template
    context = {'plot_json': plot_json}
    return render(request, 'landing_page/index.html', context)
