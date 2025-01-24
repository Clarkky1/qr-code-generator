import qrcode
from flask import Flask, request, render_template, jsonify
from io import BytesIO
import base64

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/generate', methods=['POST'])
def generate_qr():
    # Get the data from the form
    data = request.form['data']
    
    # Generate QR Code
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image for the QR Code
    img = qr.make_image(fill='black', back_color='white')
    
    # Save the image to a BytesIO object
    buffer = BytesIO()
    img.save(buffer)
    buffer.seek(0)
    
    # Encode the image to base64 to embed it in HTML
    img_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
    
    # Return the image in base64 format so it can be displayed in HTML
    return jsonify({'img_data': img_base64})

if __name__ == '__main__':
    app.run(debug=True)
