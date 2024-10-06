from flask import Flask, render_template, request, jsonify
import qrcode
import io
import base64

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_qr', methods=['POST'])
def generate_qr():
    data = request.json['data']  # Obtener el texto desde la solicitud
    
    # Generar código QR
    qr_img = qrcode.make(data)
    
    # Guardar el QR en memoria
    img_io = io.BytesIO()
    qr_img.save(img_io, 'PNG')
    img_io.seek(0)
    
    # Convertir la imagen a base64 para enviarla al frontend
    img_base64 = base64.b64encode(img_io.getvalue()).decode('ascii')
    
    return jsonify({'img': img_base64})

if __name__ == "__main__":  
    app.run(debug=True)
