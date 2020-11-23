import urllib.request as ur
import ssl
import json
import time


def signIn(token, tpye, context):
    data_dict = {
        # "device":"Android",
        # "address":"实习的详细地址",
        # "description":"",
        # "longitude":"上面地址的经度",
        # "latitude":"上面地址的纬度",
        # "planId":"抓签到包上显示的planID",
        # "type":tpye
    }
    url = 'https://api.moguding.net:9000/attendence/clock/v1/save'
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json; charset=UTF-8',
        'roleKey': 'student'
    }
    data = json.dumps(data_dict)
    requests = ur.Request(url=url, data=data.encode("utf-8"), headers=headers)
    try:
        if json.loads(ur.urlopen(requests, context=context).read().decode())['code'] == 200:
            pass
        else:
            with open('C:/Users/Administrator/Desktop/signlog.txt', 'a+') as f:
                f.write(time.strftime('%Y-%m-%d %H:%M:%S',
                                      time.localtime())+'签到失败\n')
    except Exception as e:
        pass


def login(type, context):
    login_data = {
        "phone": "",
        "password": "",
        "uuid": "",
        "loginType": "android"
    }
    request_login = ur.Request(
        url='https://api.moguding.net:9000/session/user/v1/login',
        data=json.dumps(login_data).encode(),
        headers={
            'Content-Type': 'application/json; charset=UTF-8'
        }
    )
    print(request_login)
    try:
        token = json.loads(ur.urlopen(request_login, context=context).read().decode())[
            'data']['token']
        print(token)
        if token:
            signIn(token, type, context)
    except Exception as e:
        datad = '<urlopen error Remote end closed connection without response>'
        if datad == str(e):
            print(e)
            print('网络连接超时')
        else:
            print('账号或密码输入错误')
        pass


if __name__ == '__main__':
    context = ssl._create_unverified_context()
    login("START", context)
    # time.sleep( 15 )
    # login("END",context)
