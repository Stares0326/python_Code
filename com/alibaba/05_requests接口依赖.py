import requests

# 获取验证码接口
result = requests.get("http://47.94.86.16/shop/mcheckImg")
if result.status_code == 200:
    print(result.json())
    # code=result["data"]["code"]
    code = result.json().get("data").get("code")
    # print(result.headers,type(result.headers))
    # 获取验证码接口的Set-Cookie响应头
    cookie = result.headers["Set-Cookie"]
    print(code)
    # 放置到注册的接口中
    registResult = requests.post(url="http://47.94.86.16/shop/mregist", data={"username": "刘亦菲",
                                                                              "password": "123",
                                                                              "email": "11@qq.com", "verifyCode": code},
                                 headers={"Cookie": cookie})
    print(registResult.json())
