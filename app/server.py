#!flask/bin/python
from flask import render_template
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    # TODO: Your code goes here!
    return jsonify({'detail': 'hello world'})

if __name__ == '__main__':
    app.run(host='0.0.0.0')
