from flask import Flask
from os.path import dirname, abspath, join
from json import loads, dumps
import random

app = Flask(__name__)


@app.route('/api/one')
def home():
    dir1 = dirname(abspath(__file__))
    with open(join(dir1, "data", "quotes.json"), mode='r', encoding="utf-8") as file:
        print(111)
        crf = file.read()
        print(222)
    content = loads(crf)
    print(333)
    ran_quote = random.choice(content["quotes"])
    print(444)
    response = dumps(ran_quote, ensure_ascii=False)
    print(555)
    return response, 200, {"Content-Type": "application/json"}


@app.route('/api/all')
def about():
    dir1 = dirname(abspath(__file__))
    with open(join(dir1, "data", "quotes.json"), mode='r', encoding="utf-8") as file:
        crf = file.read()
    content = loads(crf, ensure_ascii=False)
    return content, 200, {"Content-Type": "application/json"}


if __name__ == '__main__':
    app.config['JSON_AS_ASCII'] = False
    app.run(host='127.0.0.1', port=2333)
