from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html',
                           titulo="Bienvenido",
                           mensaje="Esta es la página principal.")

@app.route('/pagina1')
def pagina1():
    datos = ["Python", "Flask", "Jinja2", "HTML"]
    return render_template('pagina1.html', lista=datos)

@app.route('/pagina2')
def pagina2():
    personas = [
        {"nombre": "Ana", "edad": 22},
        {"nombre": "Luis", "edad": 30},
        {"nombre": "María", "edad": 27}
    ]
    return render_template('pagina2.html', personas=personas)

if __name__ == '__main__':
    app.run(debug=True)
