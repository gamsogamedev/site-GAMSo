from itchio import Session, GameCollection, UserCollection
from dotenv import load_dotenv
from os import getenv

load_dotenv()
api_key = getenv('ITCHIOKEY')


session = Session(api_key)

game_collection = GameCollection(session).all()
itchuser = UserCollection(session).me()

#print(jogo.url)

#todo: filtrar a lista pra mandar apenas jogos de fato publicados e ordenados com os mais recentes primeiro