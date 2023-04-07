import os
import cv2
import numpy as np
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from PIL import Image

app = Flask(__name__)


@app.route('/')
def upload_form():
    return render_template('upload.html')


@app.route('/', methods=['POST'])
def upload_image():
    #write the code from here    
    image_file=request.files['file']
    filename=secure_filename(image_file.filename)
    image_file.save(os.path.join('static/',filename))
    image=Image.open(image_file)
    image_flip=image.transpose(Image.FLIP_LEFT_RIGHT)
    image_flip.save(os.path.join('static/','flip.jpg'))
    flipped_image='flip.jpg'
    return render_template('upload.html',filename=flipped_image)

@app.route('/display/<filename>')
def display_image(filename):
    return redirect(url_for('static', filename=filename))


if __name__ == "__main__":
    app.run()
