import requests
h={
    "Cookie":"JSESSIONID=677031264BF3B502C43DD430A9995BDC"
}
result=requests.get("http://47.94.86.16/shop/myCart",headers=h)
#cookie
print(result.text)