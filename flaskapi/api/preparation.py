from pathlib import Path

import PIL

basedir = Path(__file__).parent.parent

# ==================================================
# データの前処理を実施するファイル
# ==================================================


def load_image(request, reshaped_size=(256, 256)):
    """画像の読み込み"""
    filename = request.json["filename"]
    dir_image = str(basedir / "data" / "original" / filename)
    # 画像ファイルのオブジェクトを作成する。
    image_obj = PIL.Image.open(dir_image).convert("RGB")
    # 画像のサイズを変更
    image = image_obj.resize(reshaped_size)
    return image, filename
