from flask import Flask, render_template, request, redirect, url_for
import model

app = Flask(__name__)
UPLOAD_FOLDER = 'dump/images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_text', methods=['POST', 'GET'])
def process():
    if request.method == 'POST':
        user_input = request.form['user_input']
        result = model.dummy_process(user_input)
        return render_template('result.html', user_input=user_input, result=result)
    else:
        return render_template('process.html')

@app.route('/process_image', methods=['POST', 'GET'])
def process_image():
    if request.method == 'POST':
        file = request.files['file']
        if file and model.allowed_file(file.filename):
            filename = file.filename
            file.save(UPLOAD_FOLDER + '/' + filename)
            result = model.dummy_process(filename)
            return render_template('result.html', user_input=filename, result=result)
    else:
        return render_template('image_upload.html')

if __name__ == '__main__':
    app.run("0.0.0.0",5000,debug=True)