import requests
import json
from tkinter import *
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(
    InsecureRequestWarning)  # 去掉ssl烦人的警告


def log():
    phone =             #你的手机号
    password = ""       #你的密码
    headers = {
        "Accept-Language": "zh-CN,zh;q=0.8",
        "User-Agent": "Mozilla/5.0 (Linux; U; Android 8.0.0; zh-cn; MI 6 Build/OPR1.170623.027) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
        "Authorization": "",
        "roleKey": "",
        "Content-Type": "application/json; charset=UTF-8",
        "Content-Length": "85",
        "Host": "api.moguding.net:9000",
        "Connection": "close",
        "Accept-Encoding": "gzip, deflate",
        "Cache-Control": "no-cache",
    }
    url = "https://api.moguding.net:9000/session/user/v1/login"
    pyload = {"password": password, "phone": phone,
              "loginType": "android", "uuid": ""}
    response = requests.post(url, data=json.dumps(
        pyload), headers=headers, verify=False).text
    response = json.loads(response)
    Authorization = response["data"]["token"]
    print(Authorization)
    return Authorization  


# 获取planId
def planId(Authorization):
    headers = {
        "Accept-Language": "zh-CN,zh;q=0.8",
        "User-Agent": "Mozilla/5.0 (Linux; U; Android 8.0.0; zh-cn; MI 6 Build/OPR1.170623.027) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
        "Authorization": Authorization,  
        "roleKey": "student",
        "Content-Type": "application/json; charset=UTF-8",
        "Content-Length": "500",
        "Host": "api.moguding.net:9000",
        "Connection": "close",
        "Accept-Encoding": "gzip, deflate",
        "Cache-Control": "no-cache",
    }
    url = "https://api.moguding.net:9000/practice/plan/v1/getPlanByStu"
    data = {"state": ""}
    response = requests.post(url, data=json.dumps(
        data), headers=headers, verify=False).text
    response = json.loads(response)
    return response['data'][0]['planId']


# 登录
def sin(Authorization, planId):
    country = ""        #国家
    address = ""        #上班地址
    province = ""       #省份
    city = ""           #城市
    type = "START"      #上班START/下班END
    description = ""    #打卡备注
    latitude= ""        #纬度
    longitude= ""       #经度


    url2 = "https://api.moguding.net:9000/attendence/clock/v1/save"
    headers2 = {
        "Accept-Language": "zh-CN,zh;q=0.8",
        "User-Agent": "Mozilla/5.0 (Linux; U; Android 8.0.0; zh-cn; MI 6 Build/OPR1.170623.027) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
        "Authorization": Authorization,  
        "roleKey": "student",
        "Content-Type": "application/json; charset=UTF-8",
        "Content-Length": "500",
        "Host": "api.moguding.net:9000",
        "Connection": "close",
        "Accept-Encoding": "gzip, deflate",
        "Cache-Control": "no-cache",
    }
   
    data = {"country": country,  
            "address": address,  
            "province": province,  
            "city": city,  
            "latitude": latitude,  
            "description": description,  
            "planId": planId,
            "type": type,  
            "device": "Android",
            "longitude": longitude  
            }
    response2 = requests.post(url2, data=json.dumps(
        data), headers=headers2, verify=False).text
    response2 = json.loads(response2)
    print(response2)


if __name__ == '__main__':
    Authorization = log()
    planId = planId(Authorization)
    sin(Authorization, planId)
