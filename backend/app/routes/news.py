from flask import Blueprint, jsonify

bp = Blueprint('news', __name__, url_prefix='/api/news')

@bp.route('/', methods=['GET'])
def get_news():
    return jsonify({"message": "News endpoint working"})
