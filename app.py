from flask import Flask, request, render_template
import os
import uuid
from moviepy.editor import VideoFileClip

app = Flask(__name__)

# Temporary folder for storing uploaded files
UPLOAD_FOLDER = 'static/videos'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Create the upload folder if it doesn't exist
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


def convert_video(input_path, output_path):
    clip = VideoFileClip(input_path)
    clip.write_videofile(output_path, codec='libx264', audio_codec='aac')


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = str(uuid.uuid4()) + os.path.splitext(file.filename)[1]
            input_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(input_path)

            output_filename = str(uuid.uuid4()) + '.mp4'
            output_path = os.path.join(app.config['UPLOAD_FOLDER'], output_filename)

            # Convert the uploaded video to MP4 using the moviepy library
            convert_video(input_path, output_path)

            return 'Upload and conversion successful'
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
