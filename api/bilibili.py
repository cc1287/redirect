from flask import *
import requests

# noinspection SpellCheckingInspection
bilibili_cookie = "buvid4=C9BFC9E2-E7E5-091A-22C9-409B4F48107E40794-022020811-Pk1O31qDhl6Jj4V431PIhjyISUxRfkXz7w3Qh7RdhDt15UIdb1Simw%3D%3D; buvid_fp_plain=undefined; header_theme_version=CLOSE; FEED_LIVE_VERSION=V8; enable_web_push=DISABLE; CURRENT_BLACKGAP=0; LIVE_BUVID=AUTO9017015168446128; hit-dyn-v2=1; CURRENT_FNVAL=4048; rpdid=|(J~lRJ|lm|J0J'u~|l)J~l)Y; buvid3=469C1854-27B5-431D-991F-EE7C964542DC27591infoc; DedeUserID=3461572043212849; DedeUserID__ckMd5=9c859e98e1b4ab2c; CURRENT_QUALITY=32; b_nut=100; home_feed_column=4; fingerprint=2806405a2d4d995fc4087c7da401395c; buvid_fp=f01f9fe6915db32363e25dc5bc08d1ef; bp_t_offset_3461572043212849=997411948683329536; PVID=4; _uuid=A1BD10486-4109F-4771-10167-53B10EDA5EE3217697infoc; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MzI0NTcyNjgsImlhdCI6MTczMjE5ODAwOCwicGx0IjotMX0.1qJ94AqULdH75Ozcdku2bzsAeLlSZ2oR4upuu_DabC0; bili_ticket_expires=1732457208; SESSDATA=acd7784b%2C1747750076%2Cd9a5e%2Ab1CjATrntTcQqWYEG0rXU2FImzTRFX0BOeSxMBwfImutyTxs1OHUUIJdNDgKPYZB95BEMSVnEtR3N2RHoyRzRGeTlGeE1jdnJ3WHFEaXhQUVI0S0FqWThibDEwQTB5RGVBeC1lMS1EY1pBckRnS3U2M2hFZlg5UkFWLWFVa21XeG5CczdQZzZfQk5nIIEC; bili_jct=a4d28dbbb5c2253ffcdb5cffe8a4d915; sid=4yl2wvlx; match_float_version=ENABLE; browser_resolution=1231-706; b_lsid=10E5B3411_1935C926704"
header = {
    'User-Agent': "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0",
    'Referer': "Referer: https://www.bilibili.com/",
}
app = Flask(__name__)


@app.route('/bilibili/search')
def bilibili_search():
    page = request.args.get('page')
    keyword = request.args.get('keyword')
    res = requests.get("https://api.bilibili.com/x/web-interface/search/all/v2?page={}&keyword={}"
                       .format(page, keyword), headers=header)
    try:
        return jsonify(res)
    except Exception as e:
        print(e)
        return res
