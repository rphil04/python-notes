# Import necessary modules
import os
import boto3
from flask import Flask, session, redirect, escape, request

# Create Flask application instance
app = Flask(__name__)

# Configure the secret key with the SECRET_KEY environment variable
app.secret_key = os.environ.get('SECRET_KEY', default=None)

# Generate presigned URL for an S3 object
def presigned_s3_url(bucket, key, expiration):
    params = {'Bucket': bucket, 'Key': key}
    s3 = boto3.client('s3')
    url = s3.generate_presigned_url('get_object', Params=params, ExpiresIn=expiration)
    return url

# Define a route for the root URL
@app.route('/')
def index():
    # Generate presigned URL for an image in S3 bucket
    pre_signed_url = presigned_s3_url('pre-signed-url-lab', 'ScatterChart.png', 3660)
    
    # Create an HTML template to display the image
    html_out = '''
        <!DOCTYPE html> 
        <html> 
          <head> 
            <title>HTML img src Attribute</title>
          </head>
          <body>
            <h1>Image from presigned URL</h1>
            <img src="{0}" alt="Pre-Signed URL generated image link"> 
          </body>
        </html>
    '''.format(pre_signed_url)

    return html_out

# Run the Flask application if script is executed directly
if __name__ == '__main__':
    app.run()
