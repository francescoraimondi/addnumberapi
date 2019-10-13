from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def hello():
    return "<h1>Hi! I think you're after /addone API :)</h1>"

@app.route('/addone/<number>', methods=['GET'])
def add_number(number):
    result = int(number) + 1
    return jsonify({'result': result})

if __name__ == "__main__":
    app.run(host='0.0.0.0')
