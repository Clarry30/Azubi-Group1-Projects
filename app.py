from flask import Flask, render_template, request
import boto3
from botocore.exceptions import NoCredentialsError
from werkzeug.utils import secure_filename


app = Flask(__name__)

# AWS S3 configuration
S3_ACCESS_KEY = 'AKIA6IZCB4YRXBOEQKP2'
S3_SECRET_KEY = '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'
S3_BUCKET_NAME = 'rafique-aws-bucket'
S3_REGION = 'eu-west-2'

s3 = boto3.client('s3', aws_access_key_id=S3_ACCESS_KEY, aws_secret_access_key=S3_SECRET_KEY, region_name=S3_REGION)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        try:
            # Get the uploaded file
            uploaded_file = request.files['photo']

            # Check if the file is present and allowed
            if uploaded_file and allowed_file(uploaded_file.filename):
                # Generate a unique filename for the image
                filename = secure_filename(uploaded_file.filename)

                # Upload the file to S3
                s3.upload_fileobj(uploaded_file, S3_BUCKET_NAME, filename)

                # Provide the S3 URL for further processing or display
                s3_url = f"https://{S3_BUCKET_NAME}.s3.{S3_REGION}.amazonaws.com/{filename}"

                return render_template('success.html', s3_url=s3_url)

            else:
                return render_template('error.html', message='Invalid file format. Please upload an image.')

        except NoCredentialsError:
            return render_template('error.html', message='AWS credentials not available.')

    return render_template('error.html', message='Error in file upload.')


def allowed_file(filename):
    # Check if the file extension is allowed
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


if __name__ == '__main__':
    app.run(debug=True)

