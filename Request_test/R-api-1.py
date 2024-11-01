# 华测商城进行登录。。。。。
import requests
headers={
    "application":"app",
    "application_client_type":"weixin"
}
params = {
    "application": "app",
    "application_client_type": "weixin"
}
data = {
    "accounts":"wyc111111",
    "pwd":"111111",
    "type":"username"
}
r_login=requests.post(url="http://shop-xo.hctestedu.com/index.php?s=api/user/login",
               headers=headers,params=params,data=data)
print(r_login.text)
# 设置变量提取登录接口返回的token，为登录后需要用到token的接口使用
token=r_login.json()["data"]["token"]
print(token)

goos_data = {"goods_id": 11,
"stock": 1,
"spec": [{"type":"尺码","value":"L"}]}
r_addcart = requests.post(url= "http://shop-xo.hctestedu.com/index.php?s=api/cart/save&token=token",params = params,data = goos_data)
print(r_addcart)