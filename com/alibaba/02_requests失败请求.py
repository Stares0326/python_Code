import requests

result=requests.post(url="http://47.94.86.16/stest/user/login.action",data={"username":"张三","password":"123"},timeout=10)
print(result.status_code)
#获取状态码，判断是否是200
if result.status_code==200:
    #获取响应头信息
    print(result.headers)
    print(result.json())
else:
    #抛出异常信息
    print("执行else---")
    result.raise_for_status()