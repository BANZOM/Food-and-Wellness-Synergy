from flask import Flask, render_template

app = Flask(__name__)

# Define a list of image paths
image_paths = ['static/images/1.jpeg', 'static/images/2.jpeg', 'static/images/3.jpeg','static/images/4.jpeg']

@app.route('/')
def index():
    return render_template('printImages.html', image_paths=image_paths)

if __name__ == '__main__':
    app.run(debug=True)
