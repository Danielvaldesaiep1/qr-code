from flask import Flask, redirect, url_for, request, send_file
from io import BytesIO
import qrcode
# Importa las funciones necesarias de 1.py
from generar_qr import generate_qr_code  # Asume que tienes una función llamada generate_qr_code en 1.py

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <!doctype html>
    <html lang="es">
      <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
        <title>Página Principal</title>
      </head>
      <body>
        <div class="container mt-5">
          <h1>Bienvenido a la página principal</h1>
          <a href="/generar_qr" class="btn btn-primary">Ir a Generador QR</a>
        </div>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js"></script>
      </body>
    </html>
    '''

@app.route('/generar_qr')
def generar_qr():
    # Esta ruta debería mostrar el formulario para generar QR
    return '''
    <!doctype html>
    <html lang="es">
      <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
        <title>Generador de Códigos QR</title>
      </head>
      <body>
        <div class="container mt-5">
          <h1>Generador de Códigos QR</h1>
          <form action="/generate_qr" method="POST">
            <input type="text" name="data" placeholder="Introduce texto o URL" required>
            <button type="submit" class="btn btn-primary">Generar QR</button>
          </form>
        </div>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js"></script>
      </body>
    </html>
    '''

@app.route('/generate_qr', methods=['POST'])
def generate_qr():
    data = request.form['data']
    img = generate_qr_code(data)  # Usa la función de 1.py
    img_io = BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)
    return send_file(img_io, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)