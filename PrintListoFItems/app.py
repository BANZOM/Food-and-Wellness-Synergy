from flask import Flask, render_template

app = Flask(__name__)

# Define a list of image paths
# image_paths = ['static/images/1.jpeg', 'static/images/2.jpeg', 'static/images/3.jpeg','static/images/4.jpeg']
image_paths = ['https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQos9X5vD8OOluVuxJUKbaoY9-X6pbZb5AGmhoLKFwjl2ojOUtyNq8OUy6rprs&s', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRs1_yAbqgVSPzTDFP2U13sriWM3jBmBrkte7c3meT01Yxf3LkYC2vDlkMeyeM&s', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTFRWN4KYS3OtRe128bxnsXRXSo8aDHcuhvHdHn1HiWsejxUqllG-hAsJKRRg&s', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRgAOBLqsYWRYkWnjbbfKFrJqcySN_3xhoMiwvf-GTBYRUMN_KsY0mr2tktmw&s', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSRHkwKmA_7etg5I4zPrEFMc0e9Y-CYWIRMtu1E_UqkLaKC6OLrSENz_W6v8Q&s']

@app.route('/')
def index():
    return render_template('printImages.html', image_paths=image_paths)

if __name__ == '__main__':
    app.run(debug=True)
