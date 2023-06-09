from dash import Dash, html, dcc, no_update
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import plotly.express as px
from PIL import Image
import json

app = Dash(__name__)

img1 = Image.open('westconcordaerial.png').convert('RGB')
img2 = Image.open('westconcordorthophoto.png').convert('RGB')

fig1 = px.imshow(img1, title='Image 1')
fig2 = px.imshow(img2, title='Image 2')

fig1.add_trace(go.Scatter(x=[], y=[]))

for fig in [fig1, fig2]:
    fig.update_traces(
        hoverinfo="none",
        hovertemplate=None
    )
    fig.update_layout(
        clickmode='event+select',
        xaxis = dict(
            visible=False,
        ),
        yaxis = dict(
            visible=False,
        ),
    )

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    html.Div(children=[
        dcc.Graph(
            id='img1',
            figure=fig1,
            style={'width': '100%'}
        ),
        html.Pre(id='hover-data-1'),
        html.Pre(id='click-data-1')
    ], style={'width': '50%', 'display': 'inline-block', 'textAlign': 'center'}),
    html.Div(children=[
        dcc.Graph(
            id='img2',
            figure=fig2
        ),
        html.Pre(id='hover-data-2'),
        html.Pre(id='click-data-2')
    ], style={'width': '50%', 'display': 'inline-block', 'textAlign': 'center'}),
])

@app.callback(
    [Output('hover-data-1', 'children'), Output('hover-data-2', 'children')],
    [Input('img1', 'hoverData'), Input('img2', 'hoverData')])
def display_hover_data(hover_data_1, hover_data_2):
    xy1 = [hover_data_1['points'][0][key] for key in ['x', 'y']] if hover_data_1 is not None else [0, 0]
    xy2 = [hover_data_2['points'][0][key] for key in ['x', 'y']] if hover_data_2 is not None else [0, 0]
    return f'x: {xy1[0]: 3d}, y: {xy1[1]: 3d}\n', f'x: {xy2[0]: 3d}, y: {xy2[1]: 3d}\n'

@app.callback(
    # [Output('click-data-1', 'children'), Output('click-data-2', 'children')],
    Output('img1', 'extendData'),
    [Input('img1', 'clickData'), Input('img2', 'clickData')])
def display_click_data(click_data_1, click_data_2):
    if click_data_1 is None:
        return no_update
    xy1 = [click_data_1['points'][0][key] for key in ['x', 'y']] if click_data_1 is not None else [0, 0]
    # xy2 = [click_data_2['points'][0][key] for key in ['x', 'y']] if click_data_2 is not None else [0, 0]
    # return str(xy1), str(xy2)
    return dict(x=[[xy1[0]]], y=[[xy1[1]]]), [1]


if __name__ == '__main__':
    app.run_server(debug=True)