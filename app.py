from flask import Flask, render_template, request, jsonify
import model
from flask_cors import CORS

app = Flask(__name__, static_folder='static')
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_recipe_from_text', methods=['POST', 'GET'])
def get_recipe():
    if request.method == 'POST':
        text = request.json.get('input_text','')
        processed_text = model.get_recipe(text)
        return jsonify({'processed_text': processed_text})
    else:
        return jsonify({'error': 'Invalid request'})
    
@app.route("/page1")
def page1():
    return render_template('page1.html')

@app.route('/submit/page1', methods=['POST'])
def submit1():
    input_values = request.form.getlist('inputField[]')
    if not input_values or all(not value.strip() for value in input_values):
        # If the list is empty or contains only empty strings
        return "No non-empty input values provided!"
    
    # something with the input values, such as printing them
    processed_inputs = ', '.join(input_values)

    recipe = model.get_recipe(processed_inputs)
    # print("Input values:", processed_inputs)
    return render_template('Result1.html', processed_inputs=recipe)

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
    app.run("0.0.0.0",5002,debug=True)
