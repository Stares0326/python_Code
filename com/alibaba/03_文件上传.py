import requests
#先获取图片流文件
pic={"pic":open("C:\\Users\\zhiyuan\\Desktop\\xiaofeifei.jpg",mode="rb")}
#上传图片
result=requests.post(url="http://47.94.86.16/stest/user/upload.action",data={"username":"刘亦菲"},files=pic)
print(result.json())