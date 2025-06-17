from flask import jsonify
from . import api_bp

@api_bp.route('/hello', methods=['GET'])
def hello():
    return jsonify({"message": "¡Hola desde el backend Python!"})

@api_bp.route('/world', methods=['GET'])
def world():
    return jsonify({"message": "world"})

@api_bp.route('/amigo', methods=['GET'])
def amigo():
    return jsonify({"message": "amigo"})
