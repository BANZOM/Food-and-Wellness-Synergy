from flask import Flask, render_template, jsonify, request

app = Flask(__name__, static_folder='static')


@app.route("/")
def index():
    return render_template('addItems/items.html')

# @app.route('/save_items', methods=['GET','POST'])

@app.route('/get_items', methods=['GET'])
def get_items():
    data = request.json
    items = data.get('items', [])
    return jsonify({'items': items})


if __name__ == '__main__':
    app.run(debug=True)
