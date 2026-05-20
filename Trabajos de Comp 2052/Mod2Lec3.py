from flask import Flask, request, jsonify

app = Flask(__name__)

# Lista en memoria para almacenar usuarios
usuarios = []

# GET /info
@app.route("/info", methods=["GET"])
def info():
    return jsonify({
        "sistema": "API de Gestión de Usuarios",
        "version": "1.0.0",
        "descripcion": "Servidor Flask para gestionar usuarios y productos",
        "autor": "Leonel Santa Alvarado"
    }), 200

# POST /crear_usuario
@app.route("/crear_usuario", methods=["POST"])
def crear_usuario():
    data = request.get_json()

    # Validar que ambos campos estén presentes
    if not data or "nombre" not in data or "correo" not in data:
        return jsonify({
            "error": "Faltan datos. Se requieren 'nombre' y 'correo'."
        }), 400

    nombre = data["nombre"].strip()
    correo = data["correo"].strip()

    if not nombre or not correo:
        return jsonify({
            "error": "Los campos 'nombre' y 'correo' no pueden estar vacíos."
        }), 400

    nuevo_usuario = {"nombre": nombre, "correo": correo}
    usuarios.append(nuevo_usuario)

    return jsonify({
        "mensaje": "Usuario creado exitosamente",
        "usuario": nuevo_usuario
    }), 201

# GET /usuarios
@app.route("/usuarios", methods=["GET"])
def get_usuarios():
    return jsonify({
        "usuarios": usuarios,
        "total": len(usuarios)
    }), 200

if __name__ == "__main__":
    app.run(debug=True)