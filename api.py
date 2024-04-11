# ------------------------- KEY NOTES -------------------------------

# APIs son interfaces (Intermediarios A -> B Clente -> Servidor )

# APIs pueden hacer cualquier cosa que se pueda programar

# Endpoint -> URL dentro de una API con diversas operaciones

# URLBASE -> Raiz de la API, a traves de esta contruimos todos los endpoints

# swapi.tech/
# endpoints
# swapi.tech/people/1 -> Endpoints que hacian cosas
# swapi.tech/plamets/5

# @nombre_del_decorador # Decorador -> Darle poderes extras a una funcion
# def hello_world():
#     return "Hello World!"
# se llama igual que la variable definida

# Levantar el servidor de nuestra web App
    
# localhost -> 127.0.0.1 | 0.0.0.0
# port = 3306, 80, etc

# ------------------------ BODY ----------------------------------- 

from flask import Flask, jsonify, request
from pymongo import MongoClient
import re

app = Flask(__name__)

# MongoDB conection
client = MongoClient('mongodb+srv://marconvrdgz:1234@cluster0.kfxhibr.mongodb.net/')
db = client['master-data']
coll = db['spotify']

# Test MongoDB conection
if client is not None:
    print("Conection sucesfully ready!")
    
@app.route('/') # -> URLBASE Ej. swapi.tech   coingecko.com/api/v3/.....endpoint
def root():
    print('Hola')
    return 'Hello World!'

@app.route('/resta') # Metodo por default es GET
def resta():
  x = 100
  y = 20
  print(x-y)
  return jsonify({
    "status_code": 200,
    "data": x-y,
    "message": "TODO OK"
  })

@app.route('/resta', methods=['POST'])
def resta2():
  x = 78
  y = 20
  print(x-y)
  return jsonify({
    "status_code": 200,
    "data": x-y,
    "message": "TODO OK"
  })

@app.route('/suma', methods=['GET'])
def suma():
  x = 78
  y = 20
  print(x+y)
  return jsonify({
    "status_code": 200,
    "data": x-y,
    "message": "TODO OK"
  })

@app.route('/minus', methods=['POST'])
def minus():
  x = request.args.get('first_value', type=float)
  y = request.args.get('second_value', type=float)
  print(x)
  print(y)
  if(x and y):
   return jsonify({
    "status_code": 200,
    "data": x-y,
    "message": "TODO OK"
   })
  else:
   response = jsonify({
    "status_code": 400,
    "data": "No se han introducido valores numericos",
    "message": "ERROR"
   })
   response.status_code = 400
   return response

# ---------------------------------- END POINTS SPOTIFY ------------------------------------------

# End point for Artists
@app.route('/spotify-data/ky.artists', methods=['POST'])
def get_spotify_data_artists():
    # Obtener el valor de 'artists'
    artists = request.args.get('artists')  
    # Construir una expresión regular para buscar 'lady' en cualquier parte del texto
    regex = re.compile('.*{}.*'.format(re.escape(artists)), re.IGNORECASE)
    # Buscar documentos en la colección 'spotify' donde 'artists' coincida con la expresión regular
    documents = coll.find({'artists': {'$regex': regex}})
    # Convertir los documentos a una lista para que puedan ser serializados como JSON
    result = list(documents)

    if result:
        # Convertir ObjectId a cadena en cada documento
        for doc in result:
            doc['_id'] = str(doc['_id'])
        return jsonify({
           "0. Status code": 200,
           "1. Message": "Sucessfully executed!",
           "2. Number of Records": len(result),
           "3. Data": result})
    else:
        response = jsonify({
            "0. Status code": 400,
            "1. Message": "None artists found",
            "2. Number of Records": 0,
            "3. Data": "Not found",
        })
        response.status_code = 400
        return response

# End point for Name
@app.route('/spotify-data/ky.name', methods=['POST'])
def get_spotify_data_name():
    # Obtener el valor de 'name'
    name = request.args.get('name')  
    # Construir una expresión regular para buscar 'lady' en cualquier parte del texto
    regex = re.compile('.*{}.*'.format(re.escape(name)), re.IGNORECASE)
    # Buscar documentos en la colección 'spotify' donde 'name' coincida con la expresión regular
    documents = coll.find({'name': {'$regex': regex}})
    # Convertir los documentos a una lista para que puedan ser serializados como JSON
    result = list(documents)

    if result:
        # Convertir ObjectId a cadena en cada documento
        for doc in result:
            doc['_id'] = str(doc['_id'])
        return jsonify({
           "0. Status code": 200,
           "1. Message": "Sucessfully executed!",
           "2. Number of Records": len(result),
           "3. Data": result})
    else:
        response = jsonify({
            "0. Status code": 400,
            "1. Message": "None name found",
            "2. Number of Records": 0,
            "3. Data": "Not found",
        })
        response.status_code = 400
        return response

# End point for Danceability
@app.route('/spotify-data/ky.danceability', methods=['POST'])
def get_spotify_data_danceability():
    # Obtener el valor de 'danceability'
    danceability = request.args.get('danceability', type=float)  
    # Buscar documentos en la colección 'spotify' donde 'danceability' coincida con el valor ingresado
    documents = coll.find({'danceability': danceability})
    # Convertir los documentos a una lista para que puedan ser serializados como JSON
    result = list(documents)

    if result:
        # Convertir ObjectId a cadena en cada documento
        for doc in result:
            doc['_id'] = str(doc['_id'])
        return jsonify({
           "0. Status code": 200,
           "1. Message": "Sucessfully executed!",
           "2. Number of Records": len(result),
           "3. Data": result})
    else:
        response = jsonify({
            "0. Status code": 400,
            "1. Message": "None value found",
            "2. Number of Records": 0,
            "3. Data": "Not found",
        })
        response.status_code = 400
        return response

# End point for Energy
@app.route('/spotify-data/ky.energy', methods=['POST'])
def get_spotify_data_energy():
    # Obtener el valor de 'energy'
    energy = request.args.get('energy', type=float)  
    # Buscar documentos en la colección 'spotify' donde 'energy' coincida con el valor ingresado
    documents = coll.find({'energy': energy})
    # Convertir los documentos a una lista para que puedan ser serializados como JSON
    result = list(documents)

    if result:
        # Convertir ObjectId a cadena en cada documento
        for doc in result:
            doc['_id'] = str(doc['_id'])
        return jsonify({
           "0. Status code": 200,
           "1. Message": "Sucessfully executed!",
           "2. Number of Records": len(result),
           "3. Data": result})
    else:
        response = jsonify({
            "0. Status code": 400,
            "1. Message": "None value found",
            "2. Number of Records": 0,
            "3. Data": "Not found",
        })
        response.status_code = 400
        return response

# End point for Explicit
@app.route('/spotify-data/ky.explicit', methods=['POST'])
def get_spotify_data_explicit():
    # Obtener el valor de 'explicit'
    explicit = request.args.get('explicit', type=float)  
    # Buscar documentos en la colección 'spotify' donde 'explicit' coincida con el valor ingresado
    documents = coll.find({'explicit': explicit})
    # Convertir los documentos a una lista para que puedan ser serializados como JSON
    result = list(documents)

    if result:
        # Convertir ObjectId a cadena en cada documento
        for doc in result:
            doc['_id'] = str(doc['_id'])
        return jsonify({
           "0. Status code": 200,
           "1. Message": "Sucessfully executed!",
           "2. Number of Records": len(result),
           "3. Data": result})
    else:
        response = jsonify({
            "0. Status code": 400,
            "1. Message": "None value found",
            "2. Number of Records": 0,
            "3. Data": "Not found",
        })
        response.status_code = 400
        return response

# End point for Popularity
@app.route('/spotify-data/ky.popularity', methods=['POST'])
def get_spotify_data_popularity():
    # Obtener el valor de 'popularity'
    popularity = request.args.get('popularity', type=float)  
    # Buscar documentos en la colección 'spotify' donde 'popularity' coincida con el valor ingresado
    documents = coll.find({'popularity': popularity})
    # Convertir los documentos a una lista para que puedan ser serializados como JSON
    result = list(documents)

    if result:
        # Convertir ObjectId a cadena en cada documento
        for doc in result:
            doc['_id'] = str(doc['_id'])
        return jsonify({
           "0. Status code": 200,
           "1. Message": "Sucessfully executed!",
           "2. Number of Records": len(result),
           "3. Data": result})
    else:
        response = jsonify({
            "0. Status code": 400,
            "1. Message": "None value found",
            "2. Number of Records": 0,
            "3. Data": "Not found",
        })
        response.status_code = 400
        return response

# End point for Tempo
@app.route('/spotify-data/ky.tempo', methods=['POST'])
def get_spotify_data_tempo():
    # Obtener el valor de 'tempo'
    tempo = request.args.get('tempo', type=float)  
    # Buscar documentos en la colección 'spotify' donde 'tempo' coincida con el valor ingresado
    documents = coll.find({'tempo': tempo})
    # Convertir los documentos a una lista para que puedan ser serializados como JSON
    result = list(documents)

    if result:
        # Convertir ObjectId a cadena en cada documento
        for doc in result:
            doc['_id'] = str(doc['_id'])
        return jsonify({
           "0. Status code": 200,
           "1. Message": "Sucessfully executed!",
           "2. Number of Records": len(result),
           "3. Data": result})
    else:
        response = jsonify({
            "0. Status code": 400,
            "1. Message": "None value found",
            "2. Number of Records": 0,
            "3. Data": "Not found",
        })
        response.status_code = 400
        return response
    

# ultima linea del file de la API, solo cuando se ejecuta en modo local
# app.run(debug=True, host='localhost', port=5000)
if __name__ == "__main__":
	app.run()
