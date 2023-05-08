from dash import html
import dash_bootstrap_components as dbc


layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            dbc.Button("Pesquisa ChatGPTov", href='/pesquisa-chatgpt', className='header_icon')
        ], md=3,xs=4), 
        dbc.Col([
            dbc.Button("Dall-e", href='/dall-e', className='header_icon')
        ], md=3,xs=4),
        html.Hr(style={'color' : 'rgba(255, 255, 255, 0.6)'})
    ], className='g-2 my-auto'),

], fluid=True)