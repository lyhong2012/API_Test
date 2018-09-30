import requests
#response = requests.request("get","https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=wx3e136f856b79baf4&secret=0436041340b58dde7edf530c96c5ed42")
#print(response.cookies)
#print(response.json())

#response2 = requests.get("https://blog.csdn.net/fxbin123/article/details/80428216")
#print(response2.text)
parameters = {"url_forward":"", "username":  "liyinghong", "password":"123456"}
response3 = requests.post("http://localhost/index.php?m=user&c=public&a=login",data=parameters)
response3.encoding = response3.apparent_encoding
print(response3.headers["Expires"])
