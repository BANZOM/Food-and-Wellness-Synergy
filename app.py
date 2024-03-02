from flask import Flask, render_template, request, jsonify
import model
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/get_recipe_from_text', methods=['POST'])
def get_recipe():
    if request.method == 'POST':
        text = request.form['input_text']
        processed_text = model.get_recipe(text)
        return jsonify({'processed_text': processed_text})

if __name__ == '__main__':
    app.run("0.0.0.0",5002,debug=True)