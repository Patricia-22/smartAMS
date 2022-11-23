import json
import time
import uvicorn
from pathlib import Path
from flask import Flask
from flask import request
from flask import jsonify
import face_detection
import requests
import os

app = Flask(__name__)

url='http://127.0.0.1:8000/faculty/attendancefile'

@app.route('/run', methods=['GET', 'POST'])
def root():
    if request.method == 'POST':
        face_detection.run()
        attendance={'file':open("attendance.csv",'r')}
        resp={"face_detection":"Done"}
        send_attendance = requests.post(url, files=attendance)
        return jsonify(resp)

UPLOAD_FOLDER = 'student_images\\'


@app.route('/image', methods=['GET', 'POST'])
def imaging():
    if request.method == 'POST':
        file = request.files['file']
        app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
    resp = {"resp": "Done"}

    return jsonify(resp)