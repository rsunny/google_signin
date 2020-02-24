from flask import Flask, render_template, request
from flask_cors import CORS, cross_origin
import requests, json

app = Flask(__name__)
CORS(app, support_credentials=True)

@app.route('/authenticate', methods = ['POST'])
def authenticate():
    req_data = request.get_json()

    url = 'http://127.0.0.1:5001/google/login_google/'
    body = {
        'google_token': req_data['id_token'],
        'source': 'twe'
    }
    print(body)
    res = requests.post(url=url, data=json.dumps(body), headers={'Content-Type': 'application/json'})
    print(res)
    res = json.loads(res.content)
    print('twas', res)

    url = 'http://127.0.0.1:55569/auth/twa/verify'
    body = {
        "headers": {
            "appid": 0,
            "client_build_id": 0,
            "key": "string",
            "key_type": "client",
            "request_version": 0,
            "timestamp": 0
        },
        "request": {
            "backend_access_token": res['access_token'],
            "backend_user_id": res['user_id'],
            "kick_existing_user": True,
            "machine_fingerprint": "string",
            "region": "string",
            "session_guid": "0033e9ec-2e42-4738-8743-8cc645b7e175"
        }
    }
    print(body)
    res = json.loads(requests.post(url=url, data=json.dumps(body), headers={'Content-Type': 'application/json'}).content)
    print(res)

    return res


@app.route('/')
def status():
    return "Healthy"


if __name__ == '__main__':
    app.run(port=5002, debug=True)