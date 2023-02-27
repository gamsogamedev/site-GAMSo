from flask import Flask, render_template
from dotenv import load_dotenv
from os import getenv

from jogosgamso import game_collection as nossos_jogos
from membrosgamso import df as planilha_membros

load_dotenv()

app = Flask(__name__)
app.secret_key = getenv('CHAVE_COOKIES')


@app.route('/')
def pg_principal():
    return render_template('home.html.j2', destaques = nossos_jogos[:12])

@app.route('/jogos')
def pg_jogos():
    return render_template('jogos.html.j2', jogos = nossos_jogos)

@app.route('/membros')
def pg_membros():
    return render_template('membros.html.j2', membros = planilha_membros.iterrows())

@app.route('/eventos')
def pg_eventos():
    return render_template('eventos.html.j2')

@app.route('/sobre')
def pg_sobre():
    return render_template('sobre.html.j2')

@app.route('/contato')
def pg_contato():
    return render_template('contatos.html.j2')
