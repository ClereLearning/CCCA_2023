import uuid

from flask import Flask, jsonify, request, render_template, redirect
app = Flask(__name__)

movies = [
    {
        "id": "1",
        "title": "xxx",
        "plotsumary": "aaaaaaaaaaaaa",
        "releaseddate":"2022-03-29",
        "mainactors": "rrrrrrrrrrrr",
        "directors": "dddddddddddd1"
    },
    {
        "id": "2",
        "title": "ggg",
        "plotsumary": "bbbbbbbbbbbbbbb",
        "releaseddate":"2022-03-29",
        "mainactors": "ttttttttttt",
        "directors": "dddddddddddd2"
    }    
]

#website
@app.get('/')
def index():
  return render_template('homepage.html', data = movies)

#Add a single data point (for example /add_movie)
@app.post("/add_movie")
def add_movie():
    data = request.get_json()  
    idunique = str(uuid.uuid4())
    new_movie = {"id": idunique, "title": data["title"], "plotsumary" : data["plotsumary"], "releasedate" : data["releaseddate"], "mainactors": data["mainactors"], "directors": data["directors"]} 
    movies.append(new_movie)
    #return jsonify(new_movie), 201
    return redirect('/')
    
#Get all data (for example /movies)
@app.get('/movies')
def hello():
  return jsonify(movies)

#Get a single data point (for example /movies/1)
@app.get('/movie/<string:id>')
def get_movie(id):
  for movie in movies:
    if movie["id"] == (str(id)):
        return jsonify(movie)
  return f'Movie with id {id} not found', 404

#Delete a single data point (for example /delete_movie)
#@app.delete('/delete_movie/<string:id>')
@app.route('/delete_movie/<string:id>', methods=['GET','POST'])
def delete_movie(id):
  for movie in movies:
    if movie["id"] == (str(id)):
      if request.method=="POST":
        movies.remove(movie)
        #return jsonify(movie), 200 changing to template
        return redirect('/')
      else:
        return render_template('delete.html', movie = movie)
  return f'Movie with id {id} not found', 404 
#movies.remove(movie)
#return f'Movie with id {id} has been removed', 200    
#return f'Movie with id {id} not found', 404


@app.route('/delete_moviebyget/<string:id>', methods=['GET','POST'])
def delete_moviebyget(id):
  for movie in movies:
    if movie["id"] == (str(id)):
      if request.method=="GET":
        movies.remove(movie)        
        return redirect('/')
      else:
        return render_template('delete.html', movie = movie)
  return f'Movie with id {id} not found', 404 

#Update a single data point (for example /update_movie)
@app.route('/update_movie/<string:id>', methods=['GET','POST'])
def update_movie(id):  
  for movie in movies:
    if movie["id"] == (str(id)):
        if request.method=="POST":
          movie["id"] = str(request.form['id'])
          movie["title"] = request.form['title']
          movie["plotsumary"] = request.form['plotsumary']
          movie["mainactors"] = request.form['mainactors']
          movie["directors"] = request.form['directors']
          return redirect('/')
        else:
          return render_template('update.html', movie = movie)
  return f'movie with id {id} not found', 404

