import numpy as np
from app import app
from dash import Input, Output, ctx
from app_layout import layout
from basic_structure import RubiksCube3x3
from dash import html, dcc

Rubie = RubiksCube3x3()

app.layout = layout

@app.callback(
    Output('values', 'children'),
    Input('cube_dropdown', 'value'),
    Input('reset', 'n_clicks'),
    Input('Uw', 'n_clicks'),
    Input('Uw_inv', 'n_clicks'),
    Input('Fr', 'n_clicks'),
    Input('Fr_inv', 'n_clicks'),
    Input('Rb', 'n_clicks'),
    Input('Rb_inv', 'n_clicks'),
    Input('Dy', 'n_clicks'),
    Input('Dy_inv', 'n_clicks'),
    Input('Bo', 'n_clicks'),
    Input('Bo_inv', 'n_clicks'),
    Input('Lg', 'n_clicks'),
    Input('Lg_inv', 'n_clicks')
)
def rubie_transitions(cube_dropdown, reset, Uw, Uw_inv, Fr, Fr_inv, Rb, Rb_inv, Dy, Dy_inv, Bo, Bo_inv, Lg, Lg_inv):
    # Rubie = RubiksCube3x3()
    button_id = ctx.triggered_id if not None else 'No clicks yet'
    print(button_id)
    # translation along X axis
    if button_id == 'reset':
        fig = Rubie.display_cube()
        update_out = html.Div([
            html.Div([dcc.Graph(id='graph_3d', figure=fig)], style={'width': '49%', 'display': 'inline-block'})],
            style={'display': 'flex'})
        return update_out
    elif button_id == 'Uw':
        print(button_id)
        Rubie.rotate_layer('u', -90)
        fig = Rubie.display_cube()
        update_out = html.Div([
            html.Div([dcc.Graph(id='graph_3d', figure=fig)], style={'width': '49%', 'display': 'inline-block'})],
            style={'display': 'flex'})
        return update_out
    elif button_id == 'Uw_inv':
        Rubie.rotate_layer('u', 90)
        fig = Rubie.display_cube()
        update_out = html.Div([
            html.Div([dcc.Graph(id='graph_3d', figure=fig)], style={'width': '49%', 'display': 'inline-block'})],
            style={'display': 'flex'})
        return update_out


if __name__ == '__main__':
    app.run_server(host='127.0.0.1', debug=True, port='8088')