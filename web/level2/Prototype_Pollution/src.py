from flask import Flask
import pydash
import html 
from flask import request
from flask import jsonify
# pydash==5.1.2


class Pollute:
    def __init__(self):
        pass

app=Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return "hello world"

@app.route('/one', methods={'GET', 'POST'})
def one():
    if request.content_type == 'application/json':
        data = request.get_json(force=True)
        key = data.get('key')
        value = data.get('value')
        if key and value:
            pollute = Pollute()
            pydash.set_(pollute, key, value)
            return jsonify({"status": "success"})
        else:
            return jsonify({"status": "false"})
    else:
        return jsonify({"status": "false", "message": "Invalid content type"})
@app.route("/src")
def src():
    return '<div style="word-wrap: break-word; white-space: pre-wrap;">'+html.escape(open(__file__).read())+'</div>'
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=10001)