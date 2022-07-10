from flask import Blueprint, jsonify, request
from flaskapi.api import calculation

api = Blueprint("api", __name__)

# /のルーティング


@api.get("/")
def index():
    return jsonify({"column": "value"}), 201


# /detectのルーティング
@api.post("/detect")
def detection():
    return calculation.detection(request)
