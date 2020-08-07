import requests
from dbtools import query
from filetools import write_file,read_file
#接口1 用户登录
u = "http://192.144.148.91:2333/login"
d = {"username":"liuyun1", "password":"a12345678"}
res = requests.post(url = u,json = d)

assert res.status_code == 200
assert res.json()["status"] == 200

sql = "select * from t_user where username='{}'".format(d["username"])
r = query(sql)
assert len(r) != 0

print("登录接口测试通过!")

#token取出来
# print(res.text) 

#取出token并且保存
token = res.json()["data"]["token"]
write_file("user_token.txt",token)
user_token = read_file("user_token.txt")

#接口2：用户修改头像
u1 = "http://192.144.148.91:2333/updateuserheadpic"
h1 = {"Content-Type":"application/json","token":user_token} #请求头:字典
d1 = {"ximg":"chen.jpg"} #参数
r1 = requests.post(url = u1,json = d1,headers = h1) #hearders：指定请求头

assert res.status_code == 200
assert res.json()["status"] == 200
#修改类型的数据如何查
sql = "select * from t_user where username = 'liuyun1' and headpic = 'chen.jpg'"
assert len(query(sql)) != 0
print("用户修改头像成功!")