from flask import Flask, jsonify
import random
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow frontend requests

@app.route('/toss')
def toss():
    result = random.choice(["Heads", "Tails"])
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(debug=True)
