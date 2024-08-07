from flask import Flask, request, render_template
import os

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
        # File manager will come here
        pass
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
