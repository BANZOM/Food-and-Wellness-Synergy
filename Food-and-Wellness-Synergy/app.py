from flask import Flask, render_template, jsonify, request
import json  # Import the json module

app = Flask(__name__, static_folder='static')

@app.route("/")
def index():
    return render_template('index.html')

# @app.route('/save_items', methods=['GET','POST'])

# @app.route('/get_items', methods=['GET'])
# def get_items():
#     items = json.loads(request.args.get('items'))  # Retrieve items from query parameters
#     print('Received items:', items)
#     return jsonify({'items': items})


@app.route("/page1")
def page1():
    return render_template('page1.html')

@app.route("/page2")
def page2():
    return render_template('page2.html')

@app.route("/page3")
def page3():
    return render_template('page3.html')


if __name__ == '__main__':
    app.run(debug=True)
