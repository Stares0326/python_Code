import requests


data = {
    "username": "xxxx",
    "password": "123",
    "email": "xx@qq.com",
    "phone": "123"
}
# 报文请求
result = requests.post(url="http://47.94.86.16/stest/user/dataRegist", json=data)
print(result.json())


