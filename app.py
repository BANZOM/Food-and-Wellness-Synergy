from flask import Flask, render_template, request
import model

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST', 'GET'])
def process():
    if request.method == 'POST':
        user_input = request.form['user_input']
        result = model.dummy_process(user_input)
        return render_template('result.html', user_input=user_input, result=result)
    else:
        return render_template('process.html')

if __name__ == '__main__':
    app.run("0.0.0.0",5000,debug=True)