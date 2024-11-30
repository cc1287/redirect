from flask import *
import requests

app = Flask(__name__)


@app.route('/bilibili/search')
def bilibili_search():
    page = request.args.get('page')
    keyword = request.args.get('keyword')
    res = requests.get("https://api.bilibili.com/x/web-interface/search/all/v2?page={}&keyword={}"
                       .format(page, keyword))
    return jsonify(res)
