from flask import Flask
import psycopg2

app = Flask(__name__)
VERSION = "2.0.0"

@app.route("/")
def inicio():
    try:
        conexion = psycopg2.connect(
            host="db",
            database="empresa",
            user="admin",
            password="admin123"
        )
        cursor = conexion.cursor()
        cursor.execute("SELECT id, nombre FROM clientes;")
        filas = cursor.fetchall()
        cursor.close()
        conexion.close()

        lista_clientes = "".join([f"<li>ID: {f[0]} - Nombre: {f[1]}</li>" for f in filas])

        return f"""
        <h1>Aplicación Flask</h1>
        <h2>Versión {VERSION}</h2>
        <p style='color: green; font-weight: bold;'>✔ Conexión exitosa a PostgreSQL</p>
        <h3>Lista de Clientes Registrados:</h3>
        <ul>
            {lista_clientes}
        </ul>
        """
    except Exception as e:
        return f"<h1>Error</h1><p>{str(e)}</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)