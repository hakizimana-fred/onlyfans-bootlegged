from flask  import Flask, jsonify

app = Flask(__name__)

@app.route('/hello/', methods=['GET', 'POST'])
def welcome():
    return jsonify({"message":"welcome"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)