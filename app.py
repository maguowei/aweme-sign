import os
import frida
from flask import Flask, jsonify, request
from hook import start_hook


REMOTE_DEVICE = os.getenv('REMOTE_DEVICE', '192.168.56.103:5555')


app = Flask(__name__)
api = start_hook(REMOTE_DEVICE)


@app.route('/sign')
def sign():
    global api
    url = request.args.get('url', '')
    headers = dict(request.headers)
    try:
        data = api.exports.sign(url, headers)
    except frida.InvalidOperationError as e:
        print(f'app crash: {e}')
        api = start_hook(REMOTE_DEVICE)
        data = api.exports.sign(url, headers)
    return jsonify({
        'url': url,
        'headers': headers,
        'sign': data,
    })


if __name__ == '__main__':
    app.run()
