meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            'RATA': 'Alguien pillo para algo',
            'BROTHER': 'un gran amigo',
            'RANDOM': 'Algo aleatorio o inesperado'
            'CRACK': 'Alguien abilidoso para algo'
            }
            
word = input("Escribe alguna palabra que no entiendas (¡con mayúsculas!): ")

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print('disculpeme pero esta palabra no se encuentra en este vocabulario, proximamente lo actualizaremos')
