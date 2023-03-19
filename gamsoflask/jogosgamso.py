from itchio import Session, GameCollection, UserCollection
from dotenv import load_dotenv
from os import getenv

load_dotenv()
api_key = getenv('ITCHIOKEY')


session = Session(api_key)

game_collection = GameCollection(session).all()

itchuser = UserCollection(session).me()

# tratamento rapido das strings...
for jogo in game_collection:
    
    jogo.published_at = jogo.published_at[:10]
    if jogo.short_text is None:
        jogo.short_text = ''
    elif len(jogo.short_text) > 36:
        jogo.short_text = jogo.short_text[:30] + '...'
    
    #print(jogo.published_at)
    #print(jogo.short_text)


#todo: filtrar a lista pra mandar apenas jogos de fato publicados e ordenados com os mais recentes primeiro