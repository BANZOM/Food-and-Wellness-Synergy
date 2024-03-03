from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('uploadImages.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'image' in request.files:
        image_file = request.files['image']
        # Save the image file or process it as needed
        image_file.save('uploaded_image.jpg')
        return "Image uploaded successfully!"
    else:
        return "No image uploaded!"

if __name__ == "__main__":
    app.run(debug=True)
