from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Bienvenido a mi API"


# GET /info - Devuelve información básica de la app
@app.route("/info", methods=["GET"])
def info():
    return jsonify({
        "nombre": "Mi API Flask",
        "descripcion": "API REST de ejemplo"
    })

# POST /mensaje - Recibe un mensaje y devuelve respuesta personalizada
@app.route("/mensaje", methods=["POST"])
def mensaje():
    data = request.json
    msg = data.get("mensaje", "")
    return jsonify({
        "respuesta": f"Mensaje recibido: {msg}"
    })

# Ruta /saludo existente
@app.route("/saludo", methods=["POST"])
def saludo():
    data = request.json
    nombre = data.get("nombre", "Usuario")
    return f"Hola, {nombre}!"

if __name__ == "__main__":
    app.run(debug=True)