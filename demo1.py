import requests
from dbtools import query

# url = "http://192.144.148.91:2333/get_title_img"
# res = requests.get(url) #使用get方法请求地址 res=返回值
# print(res.text)     #res.text就是返回值

#构造请求
u = "http://192.144.148.91:2333/login"
d = {"username":"liuyun1", "password":"a12345678"}
res = requests.post(url = u,json = d)
# print(res.text) #text以字符串/文本的格式显示

#判断http状态码和结果码
assert res.status_code == 200
assert res.json()["status"] == 200

#数据自动查询功能
sql = "select * from t_user where username='{}'".format(d["username"])
res = query(sql)
assert len(res) != 0

print("测试通过!")


