from dash import html, no_update
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from dash import dcc
import pandas as pd

from app import *
from home import *
import home
import header

import openai
from dotenv import load_dotenv
import os

load_dotenv()

#definicao da chave da API
openai.api_key = os.getenv("OPENAI_API_KEY")

# if os.path.isfile('historical_msgs.csv'):
#     df_historico = pd.read_csv('historical_msgs.csv', index_col=0)
#     print('oi')

# else:
#     df_historico = pd.DataFrame(columns=['user', 'chatGPT'])
#     print('oiwefewfwe')


try:
    df_historico = pd.read_csv('historical_msgs.csv', index_col=0)
    # print('\nTONGUILOPERR')

except:
    df_historico = pd.DataFrame(columns=['user', 'chatGPT'])
    # print('\nXADSSSS')
    
df_historico.to_csv('historical_msgs.csv')


app.layout = dbc.Container([
    # dcc.Store(id='historical_msgs_store', data=df_historico_csv, storage_type='memory'),
    dcc.Location(id="url"),
    dbc.Row([
        dbc.Col([
            dbc.Row([
                dbc.Col([
                    header.layout
                ], className= 'header_layout'),
            ]),
            dbc.Row([
                dbc.Col([
    
                ]),
            ],id="page_content"),
        ])
    ])
], fluid=True)

def gerar_resposta(messages):
    try:
        response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        #model="gpt-3.5-turbo-0301", ## ate 1 junho 2023
        messages=messages,
        max_tokens=1024,
        temperature=1,
        # stream=True
        )
        retorno = response.choices[0].message.content
    except:
        retorno = 'Não foi possível pesquisar. ChatGPT fora do ar'
    return retorno

def clusterCards(df_msgs_store):

    df_historical_msgs = pd.DataFrame(df_msgs_store)
    cardsList = []
    
    for line in df_historical_msgs.iterrows():
        card_pergunta = generate_card_user(line[1]['user'])
        card_resposta = generate_card_gpt(line[1]['chatGPT'])


        cardsList.append(card_pergunta)
        cardsList.append(card_resposta)


    return cardsList


@app.callback(
    # Output('historical_msgs_store', 'data'),
    Output('cards_respostas', 'children'),
    Input('botao_search', 'n_clicks'),
    # Input('historical_msgs_store', 'data'),
    State('msg_user', 'value'),
    # prevent_initial_call=True
)

def add_msg(n, msg_user):

    df_historical_msgs = pd.read_csv('historical_msgs.csv', index_col=0)

    mensagens = []
    mensagens.append({"role": "user", "content": str(msg_user)})

    pergunta_user = mensagens[0]['content']
    resposta_chatgpt = gerar_resposta(mensagens)

    # print(type(pergunta_user))

    if pergunta_user == 'None' or  pergunta_user == '':
        lista_cards = clusterCards(df_historical_msgs)
        return lista_cards

    new_line = pd.DataFrame([[pergunta_user, resposta_chatgpt]], columns=['user', 'chatGPT'])
    df_historical_msgs = pd.concat([new_line, df_historical_msgs], ignore_index = True)

    # import pdb; pdb.set_trace()   

    df_historical_msgs.to_csv('historical_msgs.csv')
    
    lista_cards = clusterCards(df_historical_msgs)



    return lista_cards


# @app.callback(
#     Output('cards_respostas', 'children'),
#     Input('historical_msgs_store', 'data'),
#     prevent_initial_call=True
# )


    




@app.callback(
    Output('page_content', 'children'),
    Input('url', 'pathname'),
)

def render_page(pathname):
    if pathname == '/pesquisa-chatgpt' or pathname == '/':
        return home.layout



if __name__ == "__main__":
    app.run_server(port=8050, debug=True)