def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg'}

def dummy_process(input):
    return input[::-1]

def dummy_process_image(filename):
    return f"Image {filename} processed"