# FlaskApp

Flask を使った物体検知用のアプリのリポジトリです。

### 仮想環境を構築するコマンド

`python3 -m venv venv`
`source venv/bin/activate`

### gitignore 生成コマンド

`curl -L http://www.gitignore.io/api/python,flask,vscode > .gitignore`

### 学習済みモデルを保存するコマンド

1.  `python`

その後は、インタラクティブシェルモードで次のようにコマンドを打ち込んでいく。

```cmd
ype "help", "copyright", "credits" or "license" for more information.
>>> import torch
>>> import torchvision
>>> model = torchvision.models.detection.maskrcnn_resnet50_fpn(pretrained=True)
/Users/harukikondo/git/FlaskApp/venv/lib/python3.9/site-packages/torchvision/models/_utils.py:208: UserWarning: The parameter 'pretrained' is deprecated since 0.13 and will be removed in 0.15, please use 'weights' instead.
  warnings.warn(
/Users/harukikondo/git/FlaskApp/venv/lib/python3.9/site-packages/torchvision/models/_utils.py:223: UserWarning: Arguments other than a weight enum or `None` for 'weights' are deprecated since 0.13 and will be removed in 0.15. The current behavior is equivalent to passing `weights=MaskRCNN_ResNet50_FPN_Weights.COCO_V1`. You can also use `weights=MaskRCNN_ResNet50_FPN_Weights.DEFAULT` to get the most up-to-date weights.
  warnings.warn(msg)
Downloading: "https://download.pytorch.org/models/maskrcnn_resnet50_fpn_coco-bf2d0c1e.pth" to /Users/harukikondo/.cache/torch/hub/checkpoints/maskrcnn_resnet50_fpn_coco-bf2d0c1e.pth
100.0%
>>> torch.save(model, "model.pt")
```
