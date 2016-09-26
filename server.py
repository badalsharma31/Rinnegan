from flask import Flask
import os

app = Flask(__name__)

PORT = int(os.getenv('PORT', 8000))

@app.route("/")
def index():
    return "Hello World"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=PORT)
