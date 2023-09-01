import os
import boto3

from flask import Flask, session, redirect, escape, request

# Create the pre-signed URL
def presigned_s3_url(bucket, key, expiration):
    """ Ggenerate presigned URL on S3 (Default 1 hour expiration)
    """
    params = {
        'Bucket': bucket,
        'Key': key
    }
    s3 = boto3.client('s3')
    url = s3.generate_presigned_url('get_object', Params=params, ExpiresIn=expiration)
    return(url)

# Configure the application name with the FLASK_APP environment variable.
app = Flask(__name__)


# Configure the secret_key with the SECRET_KEY environment variable.
app.secret_key = os.environ.get('SECRET_KEY', default=None)

@app.route('/')
def index():
    pre_signed_url = presigned_s3_url('pre-signed-url-lab', 'ScatterChart.png', 3660)
    html_out = '''<!DOCTYPE html> 
                    <html> 
                      <head> 
                        <title>
                           HTML img src Attribute 
                        </title>
                      </head>
                      <body>
                        <h1>Image from pre-signed URL</h1>
                        <img src= {0} alt="Pre-Signed URL generated image link"> 
                      </body>
                      </html>'''.format(pre_signed_url)

    return html_out
