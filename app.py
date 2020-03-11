import frida
from flask import Flask, jsonify, request
from hook import start_hook


app = Flask(__name__)
api = start_hook()


@app.route('/sign')
def sign():
    global api
    url = request.args.get('url', '')
    headers = dict(request.headers)
    try:
        data = api.exports.sign(url, headers)
    except frida.InvalidOperationError as e:
        print(f'app crash: {e}')
        api = start_hook()
        data = api.exports.sign(url, headers)
    return jsonify({
        'url': url,
        'headers': headers,
        'sign': data,
    })


if __name__ == '__main__':
    app.run()
