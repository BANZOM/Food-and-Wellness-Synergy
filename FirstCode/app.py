from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    input_values = request.form.getlist('inputField[]')
    # Process input values here
    print("Received input values:", input_values)
    return "Form submitted successfully!"

if __name__ == "__main__":
    app.run(debug=True)
