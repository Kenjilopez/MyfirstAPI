from flask import Flask

app = Flask(__name__)

@app.route("/ESPAÑOL/<nombre>")
def saludo_espanol(nombre):
    return f"Hola Mundo {nombre}"

@app.route("/ENGLISH/<nombre>")
def saludo_ingles(nombre="diego"):
    return f"Hello World {nombre}"

@app.route("/FRANCAIS/<nombre>")
def saludo_frances(nombre="diego"):
    return f"BONJOUR LE MONDE {nombre}"

@app.route("/DEUTSCH/<nombre>")
def saludo_aleman(nombre="diego"):
    return f"HALLO WELT {nombre}"

@app.route("/CHINO/<nombre>")
def saludo_chino(nombre="diego"):
    return f"你好世界 {nombre}"

@app.route("/PYCCKNÑ/<nombre>")
def saludo_ruso(nombre="diego"):
    return f"ПРИВЕТ, МИР {nombre}"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=53)

