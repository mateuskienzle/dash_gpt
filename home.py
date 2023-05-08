from app import *
from dash import html


def generate_card_gpt(pesquisa):
    cardNovo =  dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        dbc.Row([
                            dbc.Col([
                                dbc.Row([
                                    dbc.Col([
                                        html.H5([html.I(className='fa fa-desktop', style={"fontSize": '85%'}), " ChatGPTov: "], className='textoQuartenario'),
                                        html.H5(str(pesquisa), className='textoQuartenarioBranco')
                                    ], md=12, style={'text-align' : 'left'}),                              
                                ]),
                            ], md=11, xs=6, style={'text-align' : 'left'}),
                        ])
                    ])
                ], className='card_compra')
            ])
        ], className='g-2 my-auto')

    return cardNovo
def generate_card_user(pesquisa):
    cardNovo =  dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        dbc.Row([
                            dbc.Col([
                                dbc.Row([
                                    dbc.Col([
                                        html.H5([html.I(className='fa fa-user-circle', style={"fontSize": '85%'}), " User: "], className='textoQuartenario'),
                                        html.H5(str(pesquisa), className='textoQuartenarioBranco')
                                    ], md=12, style={'text-align' : 'left'}),                              
                                ]),
                            ], md=11, xs=6, style={'text-align' : 'left'}),
                        ])
                    ])
                ], className='card_compra')
            ])
        ], className='g-2 my-auto')

    return cardNovo

def generateCardsList(card_pergunta, card_resposta):

    cardAgrupado = dbc.Row([
        dbc.Col([
            dbc.Row([
                dbc.Col([
                    card_pergunta
                ])
            ]),
            dbc.Row([
                dbc.Col([
                    card_resposta
                ])
            ]),
        ])
    ]),

    return cardAgrupado



layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            dbc.Row([
                dbc.Col([
                    dbc.Input(id="msg_user", type="text", placeholder="Insira uma mensagem")
                ], md=10),
                dbc.Col([
                    dbc.Col([dbc.Button("Pesquisa", id="botao_search")])
                ], md=2)
            ])
        ]),
        dbc.Col([

        ],md=12, id='cards_respostas', style={"height": "100%", "maxHeight": "55rem", "overflow-y": "auto"}),
    ], className='g-2 my-auto')
],fluid=True),