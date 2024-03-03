from flask import Flask, render_template, request, jsonify
from pyzbar.pyzbar import decode
import cv2
import numpy as np  # Import NumPy

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('qr_code_scanner.html')

@app.route('/scan_qr_code', methods=['POST'])
def scan_qr_code():
    try:
        # Access the image data sent from the client
        image_data = request.files['image'].read()
        
        # Convert the image data to a numpy array
        nparr = np.frombuffer(image_data, np.uint8)
        
        # Decode the QR code
        image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        decoded_objects = decode(image)
        
        if decoded_objects:
            qr_data = decoded_objects[0].data.decode('utf-8')
            # Here you can store or process the scanned QR code data as per your requirement
            return jsonify({"qr_data": qr_data})
        else:
            return jsonify({"error": "No QR code detected"})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
