import dash
import dash_core_components as dcc
import dash_html_components as html
import data
import sys

def configure(star_data, app):
    x, y = star_data[0], star_data[1]
    app.layout = html.Div(children=[
        dcc.Graph(
            id='Light-Plot',
            figure={
                'data': [
                    {'x': x, 'y': y, 'type': 'scatter', 'name': 'Light Curve'},
                ],
                'layout': {
                    'title': 'Light Plot For Our Star'
                }
            }
        )
    ])   

if __name__ == '__main__':
    app = dash.Dash(__name__)
    star_data = data.process(sys.argv[1])
    configure(star_data, app)
    app.run_server(debug=True)