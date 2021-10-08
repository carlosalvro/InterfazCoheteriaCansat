import dash
from dash import dcc
from dash import html
import numpy as np


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets= external_stylesheets)


app.layout = html.Section([
  dcc.Interval(
          id="interval",
          interval=1000,
          n_intervals=0
        ),
  html.Div([
        html.Div([
            html.H3(children='Column 1', id="h1"),
            dcc.Graph(id='g1', figure={'data': [{'y': [1, 2, 3]}]})
        ], className="six columns"),

        dcc.Tabs(className="six columns",
          value="tab1", children=[
            dcc.Tab(id = "tab-1",
            value="tab1",label="tab1", children=[
              html.H3('tab1'),
              dcc.Graph(id='g2', figure={'data': [{'y': [1, 2, 3]}]})
            ]),
            dcc.Tab(id = "tab-2",
            value="tab2", label="tab2",children=[
              html.H2("Tab2")
            ])
        ]),
    ], className="row")
])

@app.callback(
  dash.dependencies.Output("h1", "children"),
  [dash.dependencies.Input("interval", "n_intervals")]
)
def prueba(n):
  x = np.random.randint(0,101)
  print(x)
  return x

app.css.append_css({
    "external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"
})

if __name__ == '__main__':
  app.run_server(debug=True)