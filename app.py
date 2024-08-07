from flask import Flask, request, render_template
import os
import uuid

app = Flask(__name__)

# Temporary folder for storing uploaded files
UPLOAD_FOLDER = 'static/videos'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Create the upload folder if it doesn't exist
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = str(uuid.uuid4()) + os.path.splitext(file.filename)[1]
            input_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(input_path)
            return 'Upload successful'
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
