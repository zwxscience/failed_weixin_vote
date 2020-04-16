#-*- coding：utf-8 -*-
import requests
import json
import time
import re
import base64
import threading
import  string
import  random
from random import randint
# 生成指定位数的随机字符串，字符为字母或数字
def get_random_string(id_length):
    charSeq = string.ascii_letters + string.digits
    randString = 'oJBHc'
    for i in range(id_length):
        randString += random.choice(charSeq)
    return randString


# randon number 10-99
def random_sleep_time(digits_length):
    digits_char = string.digits
    need_sleep_time = ''
    for i in range(digits_length):
        need_sleep_time += random.choice(digits_char)
    return int(need_sleep_time)

userAgentList = [
    'Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15F79 MicroMessenger/6.6.7 NetType/WIFI Language/en',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 11_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E302 MicroMessenger/6.7.0 NetType/WIFI Language/zh_CN',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 10_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/13B53 MicroMessenger/6.6.4 NetType/WIFI Language/zh_CN',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 11_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15G108 MicroMessenger/6.6.7 NetType/WIFI Language/zh_CN',
    'Mozilla/5.0 (Linux; Android 6.0.1; SM-G930V Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36 MicroMessenger/6.6.31.921 NetType/WIFI Language/zh_CN',
    'Mozilla/5.0 (Linux; Android 5.0.2; HTC 8088; Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) MicroMessenger/4.5.255Chrome/37.0.2049.0 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 4.4.4; HM NOTE 1LTEW Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/33.0.0.0 Mobile Safari/537.36 MicroMessenger/6.6.0.54_r849063.501 NetType/WIFI',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Mobile/14E304 MicroMessenger/6.6.5 NetType/4G Language/zh_CN',
    'mozilla/5.0 (linux; u; android 4.1.2; zh-cn; mi-one plus build/jzo54k) applewebkit/534.30 (khtml, like gecko) version/4.0 mobile safari/534.30 MicroMessenger/6.6.7',
    'mozilla/5.0 (iphone; cpu iphone os 5_1_1 like mac os x) applewebkit/534.46 (khtml, like gecko) mobile/9b206 MicroMessenger/6.0',
    'Mozilla/5.0 (Linux; Android 4.4.2; GT-N7100 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Mobile Safari/537.36 MicroMessenger/6.6.3 NetType/cmnet',
    'Mozilla/5.0 (Linux; U; Android 4.4.4; zh-cn; HTC D820mu Build/KTU84P) AppleWebKit/533.1 (KHTML, like Gecko)Version/4.0 MQQBrowser/5.4 TBS/025410 Mobile Safari/533.1 MicroMessenger/6.6.7 NetType/WIFI',
    'Mozilla/5.0 (Linux; U; Android 4.4.2; zh-cn; SM-N9008V Build/KOT49H) AppleWebKit/533.1 (KHTML, like Gecko)Version/4.0 MQQBrowser/5.4 TBS/025410 Mobile Safari/533.1 MicroMessenger/6.6.6 NetType/cmnet',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 7_0_2 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Mobile/11A501 MicroMessenger/6.1.1 NetType/3G',
    'Mozilla/5.0 (Linux; U; Android 4.4.2; zh-cn; HM NOTE 1LTETD Build/KVT49L) AppleWebKit/533.1 (KHTML, like Gecko)Version/4.0 MQQBrowser/5.4 TBS/025410 Mobile Safari/533.1 MicroMessenger/6.6.5 NetType/cmnet',
    'Mozilla/5.0 (Linux; U; Android 4.4.4; zh-cn; N918St Build/KTU84P) AppleWebKit/533.1 (KHTML, like Gecko)Version/4.0 MQQBrowser/5.4 TBS/025410 Mobile Safari/533.1 MicroMessenger/6.7.0 NetType/3gnet',
    'Mozilla/5.0 (Linux; U; Android 4.3; zh-cn; HM 1SC Build/JLS36C) AppleWebKit/533.1 (KHTML, like Gecko)Version/4.0 MQQBrowser/5.4 TBS/025410 Mobile Safari/533.1 MicroMessenger/6.6.7 NetType/#777',
    'Mozilla/5.0 (Linux; U; Android 4.2.2; zh-cn; vivo Y22 Build/JDQ39) AppleWebKit/533.1 (KHTML, like Gecko)Version/4.0 MQQBrowser/5.4 TBS/025410 Mobile Safari/533.1 MicroMessenger/6.7.0.62_r1062275.542 NetType/WIFI',
    'Mozilla/5.0 (Linux; U; Android 4.1.2; zh-cn; GT-I9128V Build/JZO54K) AppleWebKit/533.1 (KHTML, like Gecko)Version/4.0 MQQBrowser/5.4 TBS/025410 Mobile Safari/533.1 MicroMessenger/6.6.0.65_r1022275.542 NetType/WIFI',
    'Mozilla/5.0 (Linux; U; Android 4.4.2; zh-cn; HUAWEI MT2-L01 Build/HuaweiMT2-L01) AppleWebKit/533.1 (KHTML, like Gecko)Version/4.0 MQQBrowser/5.7 Mobile Safari/533.1 MicroMessenger/6.5.2.56_r958800.520 NetType/cmnet',
    '537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36 Chrome/53.0.2875.116 Safari/537.36 NetType/WIFI MicroMessenger/7.0.5 WindowsWechat',
]


#wxOpenId = "oJBHc1cqOPebHZ4eJVnbe7WOoq-o" # 微信号oJBHc1cqOPebHZ4eJVnbe7WOoq-o

wxOpenId = get_random_string(24)
exp = str(1586952151)  # 时间戳1586930199
timeArray = time.localtime(int(exp))
print(timeArray)
obj = '{"jwt-id":"' + wxOpenId + '","wxOpenId":"'+ wxOpenId +'","nickname":"此章微详","exp":'+ exp +'}'
encode_obj = str(base64.encodebytes(obj.encode('utf-8')), encoding ="utf-8")
# print(obj)
# print(encodeStrTest.replace('\n', ''))
token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.' + encode_obj.replace('\n', '') + '.7XuTQ-ZsdRJmhXlQkXgdqDdaVb3ZS9REaZLP-fJZeAA'



check_headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip',
    'Accept-Language': 'zh-CN',
    'Connection': 'keep-alive',
    'Content-Length': '0',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Host': 'www.8912421.cn',
    'Origin': 'http://www.8912421.cn/',
    'Referer': 'http://www.8912421.cn/welcome/detail.html?activityId=caa2e7e7-fd82-4ba4-948e-4f7eb6fd2a30&playerId=809499&skin=golden',
    'User-Agent': userAgentList[randint(0, 20)],
    'X-Requested-With': 'XMLHttpRequest',
    'token': token
}
# post表单网址
check_url = "http://www.8912421.cn/vote/api/wx/checkToken" #"http://www.8912421.cn/vote/api/wx/checkToken"
check_params = {'playerId': '809499'}


# 下面是开始刷票了
# 请求头信息
headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip',
    'Accept-Language': 'zh-CN',
    'Connection': 'keep-alive',
    'Content-Length': '0',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Host': 'www.8912421.cn',
    'Origin': 'http://www.8912421.cn/',
    'Referer': 'http://www.8912421.cn/welcome/detail.html?activityId=caa2e7e7-fd82-4ba4-948e-4f7eb6fd2a30&playerId=809499&skin=golden',  #活动名称，参与选手
    'User-Agent':  userAgentList[randint(0, 20)],
    'X-Requested-With': 'XMLHttpRequest',
    'token': token
}

# post表单网址
url = "http://www.8912421.cn/vote/api/wx/voteFree/add"
params = {'playerId': '809499'}  #参与选手


def post_req(tag):
    print(tag)
    # # 计数器
    count = 0
    while count < 5000:  # 定个小目标，先投他个5000票
        try:
            r = requests.post(url=check_url, data=check_params,
                              headers=check_headers)
            if(r.json()['code'] == 200):
                print("check成功%d次！" % (count))
        except Exception as reason:
            print("check错误原因是：",reason)

        try:
            r = requests.post(url=url, data=params,
                              headers=headers)
            if (r.json()['code'] == 200):
                count += 1
                print("成功投票%d次！" % (count))
            print(r.json())
        except Exception as reason:
            print("错误原因是：", reason)



if __name__ == '__main__':
    t1 = threading.Thread(target=post_req, args=("t1 start",))
    t2 = threading.Thread(target=post_req, args=("t2 start",))
    t3 = threading.Thread(target=post_req, args=("t3 start",))

    t1.start()
    t2.start()
    t3.start()
