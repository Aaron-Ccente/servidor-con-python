from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Habilita CORS para todas las rutas

@app.route('/')
def home():
    return "Welcome to the Python Backend Server!"

# Importa y registra el blueprint de rutas
from routes import api_bp
app.register_blueprint(api_bp, url_prefix='/api')

if __name__ == '__main__':
    #por defecto el puerto es 5000, pero lo cambiamos a 5001 para evitar conflictos con el frontend
    app.run(debug=True, port=5001)