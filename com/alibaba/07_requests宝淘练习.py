# 登录
import requests

base_url = "http://47.94.86.16"


def login():
    result = requests.post(url=base_url + "/shop/mlogin", data={"username": "wangwu", "password": "123"})
    print(result.json())
    # 其他接口使用到响应头中的Set-Cookie
    cookie = result.headers["Set-Cookie"]
    headers = {"Cookie": cookie}
    return headers


# 添加购物车
def addCart(headers=None):
    result = requests.post(url=base_url + "/shop/maddCart", data={"product.pid": 10, "count": 10}, headers=headers)
    print(result.json())


# 生成订单
def saveOrders(headers=None):
    result = requests.get(url=base_url + "/shop/msaveOrder", headers=headers)
    print(result.json())
    return result.json()["data"]["oid"]


# 订单支付
def payOrders(headers=None, oid=None):
    json = {
        "addr": "北京",
        "name": "zhangsan",
        "oid": oid,
        "pd_FrpId": "BOCO-NET-B2C",
        "phone": "111111111"
    }
    # Content - Type
    # application / json;
    # charset = utf - 8
    # headers["Content-Type"]="application/json;charset=utf-8"
    result=requests.post(url=base_url+"/shop/mpayOrder",json=json,headers=headers)
    print(result.json())


if __name__ == '__main__':
    #登录接口，获取返回值-响应头中的cookie
    headers = login()
    #添加购物车
    addCart(headers)
    #获取订单oid
    oid=saveOrders(headers)
    #支付订单
    payOrders(headers,oid)
