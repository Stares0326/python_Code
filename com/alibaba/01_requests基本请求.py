#请求百度，获取信息
import json

import requests
result=requests.get("https://www.baidu.com")
#获取文本信息
# print(result.text)
params={
    "username":"王五",
    "password":"123",
    "phone":"15330276178",
    "email":"111111@qq.com"
}
result=requests.get(url="http://47.94.86.16/stest/user/regist.action",params=params)
print(result.text)
print(type(result.text))
# print(result.text[2:8])
# xxx=json.loads(result.text)
# print(type(xxx),xxx)
# print(xxx["status"],xxx.get("status"))
print(result.json(),type(result.json()))