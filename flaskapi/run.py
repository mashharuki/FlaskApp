import os

from flask import Flask

from flaskapi.api import api
from flaskapi.api.config import config

# ==================================================
# APIサーバーを起動させるためのファイル
# ==================================================
config_name = os.environ.get("CONFIG", "local")

app = Flask(__name__)
app.config.from_object(config[config_name])
# blueprintをアプリケーションに登録
app.register_blueprint(api)
