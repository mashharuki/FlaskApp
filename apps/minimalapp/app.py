# Flask起動のためのインデックスファイル
from flask import Flask

# Flaskクラスをインスタンス化
app = Flask(__name__)

# ルーティングの設定
@app.route("/")
def index():
    return "Hello Flaskbook!!"
