import os

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("池田葵のホームページ.html")

if __name__ == "__main__":
    port = int(os.environ.get("port",10000))
    app.run(host="0.0.0.0", port=port)
    