# Flask起動のためのインデックスファイル
from crypt import methods

from flask import Flask

# Flaskクラスをインスタンス化
app = Flask(__name__)

# ルーティングの設定
@app.route("/")
def index():
    return "Hello Flaskbook!!"


# ルーティングの設定
@app.route("/hello", methods=["GET"], endpoint="hello-endpoint")
def hello():
    return "Hello World!!"
