from flask import *
import requests

# noinspection SpellCheckingInspection
cookie = "buvid3=109277F6-9E1D-2BE6-659C-9357A01175B136828infoc; b_nut=1732445936; _uuid=5C84E4C4-BF7E-7F47-7791-13CCE108DDA3836304infoc; buvid_fp=b50ec886c196c981acefb185ab0928ca; enable_web_push=DISABLE; buvid4=9B7F743C-DE64-F748-DB64-9841D473CA5137556-024112410-AZ5watrOjBO%2F3kusUssSCQ%3D%3D; DedeUserID=3461572043212849; DedeUserID__ckMd5=9c859e98e1b4ab2c; bp_t_offset_3461572043212849=1003336830298357760; b_lsid=F4610D56D_1937BF55BD4; bmg_af_switch=1; bmg_src_def_domain=i0.hdslb.com; header_theme_version=CLOSE; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MzMyMTA2ODksImlhdCI6MTczMjk1MTQyOSwicGx0IjotMX0._7YESb_KeYbXedX9CpZc7FaLlxqqHdTJEzJ8CPRsrd0; bili_ticket_expires=1733210629; SESSDATA=202a954d%2C1748503489%2Ccd936%2Ab1CjDW69SwyzNL1DniJkUVgrfJTJf4jU3YyN8HlkbCm8tK1gn3gkmza-gQAmayq7m9nMESVk1YMmhsNWI1ejRmVkZLeXdLb1daYTBaVi1ZcTRYM2ROUVhXWUNPUVlSRk1mT1J0d0pJZEU5MzJ6Y0p1M2R2M1Z2cGxvTDhfa05BN0tzQjI3Rmp5cDNnIIEC; bili_jct=e2df52cc194c68dd66e9c11105b4f14b; home_feed_column=4; browser_resolution=853-700; CURRENT_FNVAL=4048; sid=g3u0lg57"
header = {
    'Cookie': cookie,
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    'Referer': "https://www.bilibili.com/",
}
app = Flask(__name__)


@app.route('/bilibili/search')
def bilibili_search():
    page = request.args.get('page')
    keyword = request.args.get('keyword')
    print("https://api.bilibili.com/x/web-interface/search/all/v2?page={}&keyword={}".format(page, keyword))
    res = requests.get("https://api.bilibili.com/x/web-interface/search/all/v2?page={}&keyword={}"
                       .format(page, keyword), headers=header)
    try:
        return jsonify(res)
    except Exception as e:
        print(e)
        return res.content


@app.route('/bilibili/view')
def bilibili_view():
    bvid = request.args.get('bvid')
    res = requests.get("https://api.bilibili.com/x/web-interface/view?bvid={}"
                       .format(bvid), headers=header)
    try:
        return jsonify(res)
    except Exception as e:
        print(e)
        return res.content


@app.route('/bilibili/playurl')
def bilibili_playurl():
    avid = request.args.get('avid')
    cid = request.args.get('cid')
    res = requests.get("https://cc1287-redirect.vercel.app/bilibili/x/player/playurl?fnval=80&cid={}&avid={}"
                       .format(cid, avid), headers=header)
    try:
        return jsonify(res)
    except Exception as e:
        print(e)
        return res.content
