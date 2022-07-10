from flaskapi.api.config.base import Config


# ==================================================
# 物体検知APIをローカルで起動させるための設定ファイル
# ==================================================
class LocalConfig(Config):
    TESTING = True
    DEBUG = True
