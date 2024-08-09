from flask import Flask, request, render_template
import os
import uuid
from moviepy.editor import VideoFileClip
import boto3
from dotenv import load_dotenv

app = Flask(__name__)

# Temporary folder for storing uploaded files
UPLOAD_FOLDER = 'static/videos'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Create the upload folder if it doesn't exist
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Load environment variables from.env file
load_dotenv()

# AWS S3 client setup
s3 = boto3.client('s3')
S3_BUCKET_NAME = os.getenv('S3_BUCKET_NAME')
S3_REGION_NAME = os.getenv('S3_REGION_NAME')


def convert_video(input_path, output_path):
    clip = VideoFileClip(input_path)
    clip.write_videofile(output_path, codec='libx264', audio_codec='aac')


def upload_to_s3(file_path, bucket_name, object_name):
    s3.upload_file(file_path, bucket_name, object_name)


@app.route('/', methods=['GET', 'POST'])
def index():
    video_url = None
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

            # Upload the converted video to AWS S3
            upload_to_s3(output_path, S3_BUCKET_NAME, output_filename)

            video_url = f"https://{S3_BUCKET_NAME}.s3.{S3_REGION_NAME}.amazonaws.com/{output_filename}"

            return render_template('index.html', video_url=video_url)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
