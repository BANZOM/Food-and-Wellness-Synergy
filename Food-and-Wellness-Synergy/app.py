from flask import Flask, render_template, jsonify, request
import json  # Import the json module

app = Flask(__name__, static_folder='static')

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/page1")
def page1():
    return render_template('page1.html')

@app.route('/submit/page1', methods=['POST'])
def submit1():
    input_values = request.form.getlist('inputField[]')
    # Do something with the input values, such as printing them
    print("Input values:", input_values)
    return "Form submitted successfully!"

@app.route("/page2")
def page2():
    return render_template('page2.html')

@app.route('/submit/page2', methods=['POST'])
def submit2():
  # Get the uploaded file
    file = request.files['image']

    # Read the file and decode the QR code
    # qr_text = decode(Image.open(file))

    # Print the decoded text
    print("Decoded QR code:", file)

    # Return a response (you can customize this as needed)
    return {'qr_data': "file"}
    

@app.route("/page3")
def page3():
    return render_template('page3.html')

@app.route('/submit/page3', methods=['POST'])
def submit3():
    if 'image' in request.files:
        image_file = request.files['image']
        # Save the image file or process it as needed
        image_file.save('dump/uploaded_image.jpg')
        return "Image uploaded successfully!"
    else:
        return "No image uploaded!"

    

if __name__ == '__main__':
    app.run(debug=True)
