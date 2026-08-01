from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

@app.route("/buscar", methods=["GET"])
def buscar():
    termino = request.args.get("q", "")
    with sqlite3.connect("database.db") as conexion:
        cursor = conexion.cursor()
        consulta = "SELECT * FROM productos WHERE nombre = ?"
        cursor.execute(consulta, (termino,))
        resultado = cursor.fetchall()
    return jsonify(resultado)

@app.route("/evaluar", methods=["GET"])
def evaluar():
    return jsonify({"error": "Operación no permitida"}), 400

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=False)
