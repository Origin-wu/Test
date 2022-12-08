# -*- coding: utf8 -*-
'''
[task_local]
57 0,19 * * * https://raw.githubusercontent.com/Origin-wu/Test/main/yunyoudao.js, tag=yunyoudao, enabled=true

new Env('yunyoudao');
'''
import requests
import time

def sign():
    pass
    # url = 'https://note.youdao.com/yws/mapi/user?method=checkin'
    # url = 'https://note.youdao.com/yws/api/self?ClientVer=61000010000&GUID=PC84de924deb417c0b0&client_ver=61000010000&device_id=PC84de924deb417c0b0&device_name=LPC-20220531B07&device_type=PC&keyfrom=pc&method=get&os=Windows&os_ver=Windows%2010&subvendor=&vendor=website&vendornew=website'
    # login_url = 'https://note.youdao.com/yws/api/self?ClientVer=61000010000&GUID=PC84de924deb417c0b0&client_ver=61000010000&device_id=PC84de924deb417c0b0&device_name=LPC-20220531B07&device_type=PC&keyfrom=pc&method=get&os=Windows&os_ver=Windows%2010&subvendor=&vendor=website&vendornew=website'
    login_url = 'https://note.youdao.com/yws/mapi/user?method=checkin'
    # response = requests.get(url)
    # # print(type(response))
    # # print(response.request.headers)
    # print("")
    # print("")
    # print(response.status_code)
    # print(response.headers)
    para = {
        "ClientVer":"61000010000"
    }

    heads = {
        "User-Agent": "YNote",
        "Host": "note.youdao.com",
        "Connection": "Keep-Alive",
        "Cache-Control": "no-cache",
        "Accept": "*/*",
        #"Cookie": "JSESSIONID=9DD897A01FCD24CF32EA75AE10542AF1.ynote-webserver-docker-cwonline-3-c0u1c-5p83d-84f5cd5d7b-m8t9z-8081; YNOTE_FORCE=true; YNOTE_SESS=v2|-oOIeZMLU0kMhHgukfTLRQuk4zWnMzWRz5kLYWOLzm0kERLguhMYY0zWPMezhMPu0eKOLpuhLl50JF6MQ4RMYl0PS0HYY6Lkm0; YNOTE_LOGIN=5||1669978287158"
    }
 
    timestamp = int(time.time() * 1000)
    str_timestamp = '1 |' + str(timestamp)
#  Cookie: YNOTE_FORCE=true; YNOTE_SESS=v2|oAmsQxwbWYEOfg4P4T4064nLgy0M6S0pLnfw40Lgz06FhMkY0HYW0OYOLgzhMQz0pZ64TLRfzfRpuhMTLnHPF0e40MUm0LlWR; YNOTE_LOGIN=1||1670503428222
    cookie = {
        "YNOTE_FORCE" : "true",
        "YNOTE_SESS"  : "v2|oAmsQxwbWYEOfg4P4T4064nLgy0M6S0pLnfw40Lgz06FhMkY0HYW0OYOLgzhMQz0pZ64TLRfzfRpuhMTLnHPF0e40MUm0LlWR",
        "YNOTE_LOGIN" : str_timestamp
    }
    session = requests.session()
    r = session.post(url = login_url, headers=heads, cookies=cookie, verify=False)
    print("-----------------------")
    print(r.headers)
    # print(r.)
    print(r.status_code)
    print(r.content)

    

def main():
    print("【start yundaoyou sign】")
    result = sign()
    timestamp = int(time.time() * 1000)
    str_timestamp = '1 |' + str(timestamp)
    print(str_timestamp)

if __name__ == '__main__':
    main()