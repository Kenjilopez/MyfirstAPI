from flask import Flask

app = Flask(__name__)

@app.route("/usuario", methods=["POST"])
def crear_usuario():
    return "Usuario creado"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")