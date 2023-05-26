import uuid

from flask import Flask, jsonify, request
app = Flask(__name__)

movies = [
    {
        "id": "1",
        "title": "xxx",
        "plotsumary": "aaaaaaaaaaaaa",
        "released":"2022-03-29",
        "mainactors": "rrrrrrrrrrrr",
        "directors": "dddddddddddd1"
    },
    {
        "id": "2",
        "title": "ggg",
        "plotsumary": "bbbbbbbbbbbbbbb",
        "released":"2022-03-29",
        "mainactors": "ttttttttttt",
        "directors": "dddddddddddd2"
    }    
]

#website
@app.get('/')
def index():
  idunique = str(uuid.uuid4())
  return 'Welcome to our BlockBuster API V3' + idunique

#Add a single data point (for example /add_movie)
@app.post("/add_movie")
def add_movie():
    data = request.get_json()  
    idunique = str(uuid.uuid4())
    
    #"id": "1",
    #"title": "xxx",
    #"plotsumary": "",
    #"releasedate":2022-03-29,
    #"mainactors": "",
    #"directors": ""

    #mainactors = []  
    #for item in data["mainactors"]:
    #    mainactors.append({"actor": item.actor})
    
    #directors = []
    #for item in data["directors"]:
    #    directors.append({"firstname": item.firstname ,"lastname": item.lastname})

    #writers = []   
    #for item in data["writers"]:
    #    writers.append({"firstname": item.firstname ,"lastname": item.lastname})

    
    new_movie = {"id": idunique, "title": data["title"], "plotsumary" : data["plotsumary"], "releasedate" : data["releasedate"], "mainactors": data["mainactors"], "directors": data["directors"]} 
    movies.append(new_movie)
    return jsonify(new_movie), 201
    
#Get all data (for example /movies)
@app.get('/movies')
def hello():
  return jsonify(movies)

#Get a single data point (for example /movies/1)
@app.get('/movie/<int:id>')
def get_movie(id):
  for movie in movies:
    if movie["id"] == id:
        return jsonify(movie)
  return f'Movie with id {id} not found', 404

#Delete a single data point (for example /delete_movie)
@app.delete('/delete_movie/<int:id>')
def delete_movie(id):
    for movie in movies:        
      if movie["id"] == id:
        movies.remove(movie)
        return f'Movie with id {id} has been removed', 200
    
  return f'Movie with id {id} not found', 404