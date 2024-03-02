from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/", methods=['GET', 'POST'])
def addItems():
    if request.method == 'POST':
        items = request.json.get('items', [])
        print("Items received from local storage:")
        for item in items:
            print(item)
        return 'Items received successfully'
    else:
        return render_template('addItems/items.html')

if __name__ == '__main__':
    app.run(debug=True)
