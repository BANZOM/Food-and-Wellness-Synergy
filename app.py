from flask import Flask, render_template, request, jsonify
import model
from flask_cors import CORS

app = Flask(__name__)
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
    
if __name__ == '__main__':
    app.run("0.0.0.0",5002,debug=True)
