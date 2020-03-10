from flask import Flask, jsonify, request
from hook import start_hook


app = Flask(__name__)
api = start_hook()


@app.route('/sign')
def sign():
    url = request.args.get('url', '')
    headers = dict(request.headers)
    data = api.exports.sign(url, headers)
    return jsonify({
        'url': url,
        'headers': headers,
        'sign': data,
    })


if __name__ == '__main__':
    app.run()
