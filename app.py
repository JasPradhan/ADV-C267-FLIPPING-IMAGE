import os

from flask import Flask, request, jsonify, render_template, redirect, url_for,send_file
from faker import Faker
from twilio.jwt.access_token import AccessToken
from twilio.jwt.access_token.grants import SyncGrant
from werkzeug.utils import secure_filename

app = Flask(__name__)
fake = Faker()


@app.route('/')
def index():
    return render_template('index.html')

# Add your Twilio credentials
@app.route('/token')
def generate_token():
    TWILIO_ACCOUNT_SID = 'AC7a0a20f5856f98da085f1e7661c186b4'
    TWILIO_SYNC_SERVICE_SID = 'ISc3d71b1272b78ff9dc56343542fc5cff'
    TWILIO_API_KEY = 'SKd8b1cc41f10e2b57dc1d26cad7c97ac1'
    TWILIO_API_SECRET = 'GwaSR2pJ5B50En0eWulUP7WowBHFvhoD'

    username = request.args.get('username', fake.user_name())

    # create access token with credentials
    token = AccessToken(TWILIO_ACCOUNT_SID, TWILIO_API_KEY, TWILIO_API_SECRET, identity=username)
    # create a Sync grant and add to token
    sync_grant_access = SyncGrant(TWILIO_SYNC_SERVICE_SID)
    token.add_grant(sync_grant_access)
    return jsonify(identity=username, token=token.to_jwt().decode())

# Write the code here
@app.route('/', methods=['POST'])
def download_text():
    text_from_text_area=request.form['text']
    with open('work_file.txt','w') as f:
    	f.write(text_from_text_area)


    path_to_store_text='work_file.txt'

    return send_file(path_to_store_text,as_attachment=True)

if __name__ == "__main__":
    app.run(host='localhost', port='5001', debug=True)
