import asyncio
import time

import pyppeteer
import os
import requests
import json
import numpy as np
import cv2
import base64

AK = '1vEHOKqaLqYHOQGo2rl0n6zH'
SK = '8iAtmXUlnErGuoArNI1df73bqeIb37d2'


def get_token(ak, sk):
    # http://ai.baidu.com/docs#/Auth/top
    url = 'https://aip.baidubce.com/oauth/2.0/token'
    params = {
        'grant_type': 'client_credentials',
        'client_id': ak,
        'client_secret': sk,
    }
    r = requests.post(url, params=params)
    return r.json()['access_token']


TOKEN = get_token(AK, SK)


def ocr(img):
    # 文件名
    if isinstance(img, str):
        img = open(img, 'rb').read()
    # 或cv2图像
    elif isinstance(img, np.ndarray):
        _, img = cv2.imencode('.jpg', img)
    # https://ai.baidu.com/docs#/OCR-API/e1bd77f3
    url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic'
    params = {'access_token': TOKEN}
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    img = base64.b64encode(img)
    data = {'image': img}
    r = requests.post(url, data=data, params=params, headers=headers).json()
    print(r)
    # 该项目只需要一个词
    return r['words_result'][0]['words']


def GetImage(words_count_abstract, words_count_starry_night):
    # 66442f2f720bfc86799932d8ad2eb6c7
    gt = 'bd111e81eda1cbb9f54425aafc0908ac'
    # 取challenge
    gt_judgement_data = 'zLf69dCm19Px89)S0VF9xNJclZqmqDRJ4WWMjkfhPdSCKkDYcMSXz)BRKViMXqV2FzbfgwMvONpvaxtdKhJ0Ir47)yIBomCpyJxHOXz)xhobweR(TtPNOH8j8eGLWdKnLGJkx5aRtucLNjKw6MiRULTzarEnsoutPJifN(LVurZ89WjgP8CnD0C0zrVupW4zYhfZOSysxbWAQR9a(Dh31ZdQIU(ZE72GhEfaNzpEZkAZIJ6lPXUVcQ9XjaaNiD5YgxtxP8qw2vXT1XWjSzONVoF7Epa7hgAiW6PjaMAt)YeFFv45gQO5wU3h)pZlZJeCL5LYx4d2OHfxhgJSAZuupkcsMptURPPOVoZriT)qE6CiSrDdCtxQPOqXMgBJYeqGJaK58kx17p4CRmI2FS2M24)OuneWpKeBvjOdIbd4s1RGqTUs1jWSWkP56ud(ekGm3wXDz)2vp8BKI4YNQhuoQ8N0FUrGKx9mBXHvNo8T4n7tOKwehrwM6ofCEcrQ4tWJfrJfk0xjd3y9jSNTqKXExAriNyjchTS0kcG4iJIy1YxBVgtlcv)4C9OzPIiRiKDKwGDS1vUoSr)U(9(4JmVFdE9MRu22RAb1fTxKKazRWRa1G(Oh1ph)wUVcTSKNLArTtm4eAp(AJYlz5Bhj01Vf3pfs)2)oCp4vGDIIyCNd(GteQxMM(PMKicoUcVYpA8Uf7Je0Jev0V6JY)N2VmG2sqyED01KVqThq8L)KuZmI9Xi0EWOTnb)sTK2rBg6josZ2ooK(aoDGHgvt1CcAClrwMHLQMEyElzGQDWshXI05eZYgPJgKOZJQPbE(DmPODRXTlhDCQlGa6w(fs9rs7H(OQIcy)q8QxmVLv4IOH2yYBEJY9iX1MKQvSfg5Iw4WZvjYDpiXFloRavYq2jbSQQdZS7HXsJH25KzFjnxePELFysPyvbeSBt6QsFctIg1cbU4yzELTdF66M4016m5P8t5PNKkCF66rSbsbePYtHz4rmrzUCjD05FGZutWBgQoCPTMCwKvMlr(u0gKQeW(jTrWjbZKsl7yCi3rk((1I0MMGUPVwzAgAA3BRSOtl0Jfx00Hoqk038r9K3V99j2)BGbINPCZkwVFlfqA963enyJpofZxOj2vAMGZoKoUfHd1jl31Gnmy42Jf3YBRj3954qaVYwHbs5a72dfpX9ASEfD1m82zAKA728PRxDZpZIy8)1se2xVMlqJpZzvVKj9XDyonvRG1urr)z0yFfq0NotfvA7YnUZnj8NnflgCo42lp3zSA2C1Oh7xgzG)iDIqniaPniWXosNoOtKM6MqTBN8iZ1V3Jk9dRe)HbFRsWcX2K(EFQcOlCmEmaNHsf)AKwxurxbk1yCnFNUZB5mzt0qkW2ofmJmZpES5LynhCfHXpihbSv8l6hLusApxSCawTV)lJfFSKmf0lzYdLRXxNQDqSAoICeY07(wTP1vKSF9fBR)6b3g3XMYhu37LDdePU0bBEuoLdX6D8a3mc6rUk1hMAA68iIqfLiyLqipkZH(TEj(RwfO5Te2gvJsJEhDT3Ibh3emn56TdI4aSFZ8hRGtcTfgynMJjelWa)ZdlCuCM50O2iCUM82)SQvv3xctwOnrODFkBGrURN8yPwdRpN9sA8yi6wloolOtpPj7Snj09cz(7sQKaXhjiH2(mF3ASdRPebfqoW72vn5VN7BpM1BRBpTLcfe1dyGqZypoGUYRnqQVVR8AXhcx1nxv0)i8DpnLA(gile2)U)agEApavgbJUt1CtQp68K7QeommLmAFRmDXDLHVVIGf1z7qGLQ4Evvux1rkpJmZTgjFcmc0658X2TrpKwXNeGh3CrO8mhZF1kxO1A0Qhu0Z4WWe)SXchmvAxveigF1NFPO71WC9H8nzmAbwN0cL6YSpl6WbV71Q)imMFaP67TEO(uAOxnBbc6BGjBWLo(IPuHN8qnAUrjJcOOGAPgSMEu1n)F71DTEy8MzgAMazkNYCOCi5VWX66hDDB2M3o7XO0RAkq9AMy6Y6Hr4jlEjaBJH2msmgf5wqaaRbwnOC1S(ZgCbUSbNFpC1tliXzvJr0bcIKUqEaE0YRXaqisOgBIcNB)7RamESbpFJFL8VyzeAnuccrTvMKVDcOki2)4OWws6iM3Pls7(mzWZOBKMlYn88xYF4Tzvdp6WMerFdhMhMfFlgirf0ACC7YAzXVhe1dJMjN1y32e6M9IX43FE46F1uVkGLsI3ztMl2)tefbgRoVCHFuviSl6iOHvAIIT)f4q(K8CZRh4vKymXPCgT7qx1MctIubpdtGHjmlXQ8CWSMCAJqZGmkcG2euy1VlIzpCgyVzN)bSi1nDR562q3uzodRvC4AFMJU)mw)4FC48KXqT3uPYUTusjzfsnK2dxuaeR4YAp)vkHREC1SmGGGivcTECTqdbkWq7168ep6X8upxT97KeLv9hViodBLNiufZgcp85MZTl85OwUmLNnHV9dI(O99aSoDznyz3KA38z5rsVXAE9FOcRFxtZ8i5sHaG3emToqQS9ntzSuoLD5bt(sa0w)x7LDDxAPQEY9XREUuv6nP6kwoIcptuLaD2)nXn5gpAVZxujGVuLnW9ywJoN7oY2fuZIbFa3jM593vZ694da0b917adc96d31059ea33e781b2a8e0c089f9d359c9888b53e0d8c74b768e3c9a6d1ee2f77a740e8d008f7ae884a630425b51818f47d30c107212b9b501933585bad98a5c75ee0e9c7fe712373873b7bb74183a9e10a9e60db8317ea4ae929515603a1658cff1d9f46d5dab855ff8c8cff0eb2158813163c682a769512fdc'
    response = requests.post(f"https://api.geetest.com/gt_judgement?pt=0&gt={gt}", gt_judgement_data)
    challenge = ""
    if response.status_code == 200:
        print(response.json())
        challenge = response.json().get("challenge")
    data = {"is_next": "true", "type": "click", "gt": gt, "challenge": challenge, "lang": "zh-cn", "https": "true", "protocol": "https://", "product": "embed", "width": "100%", "api_server": "api.geetest.com",
            "static_servers": ["static.geetest.com", "dn-staticdown.qbox.me"], "post": "true"}
    image_url_http = "https://static.geetest.com"
    image_url = ""
    response = requests.post("https://api.geetest.com/get.php", json=data)
    if response.status_code == 200:
        print(response.json())
        image_url = response.json().get("data").get("pic")
    print(image_url_http + image_url)
    try:
        image_name = os.path.basename(image_url)
        category = image_url.split("/")[-2]
        print(category)

        image_dir1 = f'./images/{category}'
        if not os.path.exists(image_dir1):
            os.mkdir(image_dir1)
        image_dir2 = f'./repeats/{category}'
        if not os.path.exists(image_dir2):
            os.mkdir(image_dir2)

        path1 = f'{image_dir1}/{image_name}'
        path2 = f'{image_dir2}/{image_name}'

        words_count_temp = {}
        if category == "abstract":
            words_count_temp = words_count_abstract
        else:
            words_count_temp = words_count_starry_night

        path = path1
        repeat = False
        if os.path.exists(path1):
            path = path2
            repeat = True
        if os.path.exists(path2):
            print(f"################{i}########################")
            return

        response = requests.get(image_url_http + image_url)
        with open(path, 'wb') as f:
            f.write(response.content)
        if repeat:
            return
        image = cv2.imdecode(np.asarray(bytearray(response.content), dtype='uint8'), cv2.IMREAD_GRAYSCALE)
        image = image[345:, :115]
        words = ocr(image)
        if words is None:
            cv2.imwrite(f"./words_temp/{image_name}", image)
        cv2.imwrite(f"./words_temp/{words}.jpg", image)
        if words in words_count_temp:
            words_item = words_count_temp[words]
            words_item["count"] += 1
            words_item["images"].append(image_name)
        else:
            words_count_temp[words] = {"count": 1, "images": [image_name]}
        # cv2.imshow(words, image)
        # cv2.waitKey(0)

    except Exception as ex:
        print(ex)
        pass


print("开始..." + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

image_dirs = ["./images/", "./repeats/"]

for item in image_dirs:
    if not os.path.exists(item):
        os.mkdir(item)


words_count_abstract = {}
words_count_starry_night = {}
words_count = {"abstract": words_count_abstract, "starry_night": words_count_starry_night}

for i in range(10):
    print(f"........................{i}........................")
    time.sleep(1)
    GetImage(words_count_abstract, words_count_starry_night)
print(words_count)
with open("./words_count_2.json", "w", encoding='utf-8') as f:
    json.dump(words_count, f, ensure_ascii=False)
print("完成...")
