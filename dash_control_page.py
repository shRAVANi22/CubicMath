import numpy as np
# from app import app
import dash
from dash import Input, Output, ctx
from app_layout import layout1
from basic_structure import RubiksCube3x3
from dash import html, dcc

Rubie = RubiksCube3x3()
app = dash.Dash(__name__)
app.layout = layout1

@app.callback(
    Output('container', 'children'),
    [Input('cube_dropdown', 'value'),
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
    Input('Lg_inv', 'n_clicks')])
def rubie_transitions(cube_dropdown, reset, Uw, Uw_inv, Fr, Fr_inv, Rb, Rb_inv, Dy, Dy_inv, Bo, Bo_inv, Lg, Lg_inv):
    # Rubie = RubiksCube3x3()
    # ctx = dash.callback_context
    button_id = ctx.triggered_id if not None else 'No clicks yet'
    print(button_id)

    if button_id == 'cube_dropdown':
        if cube_dropdown == 'Ideal Cube':
            Rubie.initial_state = 0
            Rubie.cube = Rubie.construct_ideal_cube()
        else:
            Rubie.initial_state = -1
            Rubie.scramble_ideal_cube()
        fig = Rubie.display_cube()
        fig.layout['uirevision'] = True
        update_out = html.Div([
            html.Div([dcc.Graph(id='graph_3d', figure=fig)], style={'width': '49%', 'display': 'inline-block'})],
            style={'display': 'flex'})
        return update_out
    elif button_id == 'reset':
        # Rubie1 = RubiksCube3x3()
        if Rubie.initial_state == 0:
            Rubie.cube = Rubie.construct_ideal_cube()
        else:
            Rubie.scramble_ideal_cube()
        fig = Rubie.display_cube()
        fig.layout['uirevision'] = True
        update_out = html.Div([
            html.Div([dcc.Graph(id='graph_3d', figure=fig)], style={'width': '49%', 'display': 'inline-block'})],
            style={'display': 'flex'})
        return update_out
    elif button_id == 'Uw':
        print(button_id)
        Rubie.rotate_layer('u', -90)
        fig = Rubie.display_cube()
        fig.layout['uirevision'] = True
        update_out = html.Div([
            html.Div([dcc.Graph(id='graph_3d', figure=fig)], style={'width': '49%', 'display': 'inline-block'})],
            style={'display': 'flex'})
        return update_out
    elif button_id == 'Uw_inv':
        Rubie.rotate_layer('u', 90)
        fig = Rubie.display_cube()
        fig.layout['uirevision'] = True
        update_out = html.Div([
            html.Div([dcc.Graph(id='graph_3d', figure=fig)], style={'width': '49%', 'display': 'inline-block'})],
            style={'display': 'flex'})
        return update_out
    elif button_id == 'Fr':
        print(button_id)
        Rubie.rotate_layer('f', -90)
        fig = Rubie.display_cube()
        fig.layout['uirevision'] = True
        update_out = html.Div([
            html.Div([dcc.Graph(id='graph_3d', figure=fig)], style={'width': '49%', 'display': 'inline-block'})],
            style={'display': 'flex'})
        return update_out
    elif button_id == 'Fr_inv':
        Rubie.rotate_layer('f', 90)
        fig = Rubie.display_cube()
        fig.layout['uirevision'] = True
        update_out = html.Div([
            html.Div([dcc.Graph(id='graph_3d', figure=fig)], style={'width': '49%', 'display': 'inline-block'})],
            style={'display': 'flex'})
        return update_out
    elif button_id == 'Rb':
        print(button_id)
        Rubie.rotate_layer('r', -90)
        fig = Rubie.display_cube()
        fig.layout['uirevision'] = True
        update_out = html.Div([
            html.Div([dcc.Graph(id='graph_3d', figure=fig)], style={'width': '49%', 'display': 'inline-block'})],
            style={'display': 'flex'})
        return update_out
    elif button_id == 'Rb_inv':
        Rubie.rotate_layer('r', 90)
        fig = Rubie.display_cube()
        fig.layout['uirevision'] = True
        update_out = html.Div([
            html.Div([dcc.Graph(id='graph_3d', figure=fig)], style={'width': '49%', 'display': 'inline-block'})],
            style={'display': 'flex'})
        return update_out
    elif button_id == 'Dy':
        print(button_id)
        Rubie.rotate_layer('d', -90)
        fig = Rubie.display_cube()
        fig.layout['uirevision'] = True
        update_out = html.Div([
            html.Div([dcc.Graph(id='graph_3d', figure=fig)], style={'width': '49%', 'display': 'inline-block'})],
            style={'display': 'flex'})
        return update_out
    elif button_id == 'Dy_inv':
        Rubie.rotate_layer('d', 90)
        fig = Rubie.display_cube()
        fig.layout['uirevision'] = True
        update_out = html.Div([
            html.Div([dcc.Graph(id='graph_3d', figure=fig)], style={'width': '49%', 'display': 'inline-block'})],
            style={'display': 'flex'})
        return update_out
    elif button_id == 'Bo':
        print(button_id)
        Rubie.rotate_layer('b', -90)
        fig = Rubie.display_cube()
        fig.layout['uirevision'] = True
        update_out = html.Div([
            html.Div([dcc.Graph(id='graph_3d', figure=fig)], style={'width': '49%', 'display': 'inline-block'})],
            style={'display': 'flex'})
        return update_out
    elif button_id == 'Bo_inv':
        Rubie.rotate_layer('b', 90)
        fig = Rubie.display_cube()
        fig.layout['uirevision'] = True
        update_out = html.Div([
            html.Div([dcc.Graph(id='graph_3d', figure=fig)], style={'width': '49%', 'display': 'inline-block'})],
            style={'display': 'flex'})
        return update_out
    elif button_id == 'Lg':
        print(button_id)
        Rubie.rotate_layer('l', -90)
        fig = Rubie.display_cube()
        fig.layout['uirevision'] = True
        update_out = html.Div([
            html.Div([dcc.Graph(id='graph_3d', figure=fig)], style={'width': '49%', 'display': 'inline-block'})],
            style={'display': 'flex'})
        return update_out
    elif button_id == 'Lg_inv':
        Rubie.rotate_layer('l', 90)
        fig = Rubie.display_cube()
        fig.layout['uirevision'] = True
        update_out = html.Div([
            html.Div([dcc.Graph(id='graph_3d', figure=fig)], style={'width': '49%', 'display': 'inline-block'})],
            style={'display': 'flex'})
        return update_out
    else:
        return 0


if __name__ == '__main__':
    app.run_server(host='127.0.0.1', debug=True, port='8088', use_reloader=True)