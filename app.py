import time
import random
import requests
from flask import Flask, jsonify, request
from hook import start_hook


app = Flask(__name__)
script = start_hook()


@app.route("/")
def index():
    current_timestamp = str(int(time.time() * 1000))
    url = "https://aweme.snssdk.com/aweme/v1/user/?user_id=57833035660&retry_type=no_retry&ac=wifi&channel=wandoujia_aweme1&aid=1128&app_name=aweme&version_code=580&version_name=5.8.0&device_platform=android&ssmix=a&device_type=OPPO+R11+Plus&device_brand=OPPO&language=zh&os_api=22&os_version=5.1.1&resolution=720*1280&dpi=192&update_version_code=5800&mcc_mnc=46002&ts=1578724824&_rticket=" +  current_timestamp +"&device_id=70433914677&iid=99003389687&as=a1552681083dee3da94255&cp=63d8e65f8f9313d2e1McUg&mas=01656f90dce2caa5a0d24a9cfcb52bdb78acac4c2c9c8626cca6a6"
    # url = "https://api.amemv.com/aweme/v1/comment/list/?aweme_id=6746897222073470215&cursor=0&count=20&user_id=57833035660&retry_type=no_retry&ac=wifi&channel=wandoujia_aweme1&aid=1128&app_name=aweme&version_code=580&version_name=5.8.0&device_platform=android&ssmix=a&device_type=OPPO+R11+Plus&device_brand=OPPO&language=zh&os_api=22&os_version=5.1.1&resolution=720*1280&dpi=192&update_version_code=5800&mcc_mnc=46002&ts=1578724824&_rticket=" +  current_timestamp +"&device_id=70433914677&iid=99003389687&as=a1552681083dee3da94255&cp=63d8e65f8f9313d2e1McUg&mas=01656f90dce2caa5a0d24a9cfcb52bdb78acac4c2c9c8626cca6a6"
    # url = "http://aweme.snssdk.com/aweme/v1/aweme/post/?aid=1128&min_cursor=0&user_id=104255897823&count=21&max_cursor=0&source=0&aweme_id=6746897222073470215&cursor=0&count=20&user_id=57833035660&retry_type=no_retry&ac=wifi&channel=wandoujia_aweme1&aid=1128&app_name=aweme&version_code=580&version_name=5.8.0&device_platform=android&ssmix=a&device_type=OPPO+R11+Plus&device_brand=OPPO&language=zh&os_api=22&os_version=5.1.1&resolution=720*1280&dpi=192&update_version_code=5800&mcc_mnc=46002&ts=1578724824&_rticket=" +  current_timestamp +"&device_id=70433914677&iid=99003389687&as=a1552681083dee3da94255&cp=63d8e65f8f9313d2e1McUg&mas=01656f90dce2caa5a0d24a9cfcb52bdb78acac4c2c9c8626cca6a6"
    # url = "https://api.amemv.com/aweme/v1/aweme/detail/?aweme_id=6746897222073470215&aid=1128&min_cursor=0&user_id=104255897823&count=21&max_cursor=0&source=0&aweme_id=6746897222073470215&cursor=0&count=20&user_id=57833035660&retry_type=no_retry&ac=wifi&channel=wandoujia_aweme1&aid=1128&app_name=aweme&version_code=580&version_name=5.8.0&device_platform=android&ssmix=a&device_type=OPPO+R11+Plus&device_brand=OPPO&language=zh&os_api=22&os_version=5.1.1&resolution=720*1280&dpi=192&update_version_code=5800&mcc_mnc=46002&ts=1578724824&_rticket=" +  current_timestamp +"&device_id=70433914677&iid=99003389687&as=a1552681083dee3da94255&cp=63d8e65f8f9313d2e1McUg&mas=01656f90dce2caa5a0d24a9cfcb52bdb78acac4c2c9c8626cca6a6"

    args = script.exports.a(url)
    # print(args)
    x_gorgon = args.get("X-Gorgon")
    x_khronos = args.get("X-Khronos")

    headers = {
            "Host": "aweme-hl.snssdk.com",
            "Connection": "keep-alive",
            "Cookie": "odin_tt=a900e5fd7ce1f4c2d49de90e1fb9af468bb3ae1fad94d142d34f42e0087338cfd7fe03b0080a5242e17d62769239142d",
            "Accept-Encoding": "gzip",
            "X-SS-REQ-TICKET": x_khronos + str(random.randint(125, 896)),
            "X-SS-TC": "0",
            "X-SS-RS": "0",
            "User-Agent": "com.ss.android.ugc.aweme/530 (Linux; U; Android 7.1.2; zh_CN; Redmi 5A; Build/N2G47H; Cronet/58.0.2991.0)",
            "X-Khronos": x_khronos,
            "X-Gorgon": x_gorgon,
        }

    res = requests.get(url=url, headers=headers)

    return jsonify({
        "x_gorgon": x_gorgon,
        "x_khronos": x_khronos,
        "headers": headers,
        "url": url,
        "data": res.json()
    })


if __name__ == '__main__':
    app.run()
