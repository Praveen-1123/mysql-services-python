from flask import Flask, request, jsonify
from main import app
from db.db_init import *
from db.controller import *
from controller import user_controller

@app.route('/', methods=['GET'])
def hello_world():
    return 'Welcome to MySQL Test API'

@app.route('/user/get/<id>', methods=['GET'])
def getUser(id):
    return user_controller.getUser(id)

@app.route('/user/create', methods=['POST'])
def createUser():
    data = request.json
    return user_controller.createUser(data)

@app.route('/db/droptable/<table>', methods=['DELETE'])
def drop(table):
    return dropTable(table)
