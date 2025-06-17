from flask import jsonify
from . import api_bp

@api_bp.route('/hello', methods=['GET'])
def hello():
    return jsonify({"message": "¡Hola desde el backend Python!"})