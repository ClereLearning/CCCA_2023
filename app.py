from flask import Flask, jsonify, request, render_template, redirect
app = Flask(__name__)

#curl http://localhost:5000
@app.get('/')
def index():
  return 'Welcome to our BlockBuster API v2'