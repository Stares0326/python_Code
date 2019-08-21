import os
import requests

from com.tencent.utils import log


class RequestUtils:
    def doRequest(self, url=None, method=None, params=None, headers={}, json=None):
        # 往头中添加cookie信息

        cookie = self.getCookies()
        if cookie != None:
            headers["Cookie"] = cookie
        if method == "POST":
            return self.doPOST(url, params, headers, json)
        else:
            return self.doGET(url, params, headers)

    # post请求
    def doPOST(self, url, params, headers, json):
        result = requests.post(url=url, data=params, headers=headers, json=json, timeout=10)
        # 判断当前状态码是否是200
        if result.status_code == 200:
            self.setCookies(result.headers)
            try:
                return result.json()
            except:
                return result.text
        else:
            # 状态码如果是404，记录错误信息....log
            return {}

    # get请求
    def doGET(self, url, params, headers):
        result = requests.get(url=url, params=params, headers=headers, timeout=10)
        # 判断当前状态码是否是200
        if result.status_code == 200:
            self.setCookies(result.headers)
            try:
                return result.json()
            except:
                return result.text
        else:
            # 状态码如果是404，记录错误信息....log
            log.logger().info("当前出错了,错误码%d" % result.status_code)
            try:
                result.raise_for_status()
            except Exception as e:
                log.logger().info("当前出错了,错误信息%s" % e)
            return {}

    def setCookies(self, headers):
        cookie = headers.get("Set-Cookie")
        if cookie != None:
            stream = open("../cookie/cookie.txt", mode="w")
            stream.write(str(cookie))
            stream.close()

    def getCookies(self):
        # 先判断文件是否存在，如果存在
        if os.path.exists("../cookie/cookie.txt"):
            stream = open("../cookie/cookie.txt", mode="r")
            cookie = stream.readline().strip()
            stream.close()
            return cookie
        else:
            return None


if __name__ == '__main__':
    requestUtils = RequestUtils()
    result = requestUtils.doRequest("http://47.94.86.16/shop/indexxxx", method="GET")
    print(result)
