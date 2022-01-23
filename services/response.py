from flask import jsonify, Response

def ReS(data):
    return jsonify(success = True, data= data), 200

def ReF(data):
    return jsonify(success=False, data=data), 400
