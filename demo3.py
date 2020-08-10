import requests
from filetools import write_file,read_file
from dbtools import query,commit
#接口1 用户登录

#构造请求
u = "http://192.144.148.91:2333/login"
d = {"username":"liuyun1", "password":"a12345678"}
res = requests.post(url = u,json = d)
print(res.text)

#判断结果
assert res.status_code == 200
assert res.json()["status"] == 200

#查询数据库
sql = "select * from t_user where username = '{}'".format(d["username"])
print(sql)
assert len(query(sql)) != 0
print("用户登录接口成功")
#取出用户token
token = res.json()["data"]["token"]
write_file("token.txt",token)
user_token = read_file("token.txt")


# #接口2 用户写篇文章
# #构造请求
# u1 = "http://192.144.148.91:2333/article/new"
# d1 = {"title":"如何学习测试",
#       "content":"每天通宵学习",
#       "tags":"测试1234",
#       "brief":"好好学习测试",
#       "ximg":"chen.jpg"}
# h1 = {"Content-Type":"application/json","token":user_token} #请求头:字典
# res1 = requests.post(url = u1,json = d1,headers = h1)
# # print(res1.text)
# #判断结果
# assert res1.status_code == 200
# assert res1.json()["status"] == 200

# #查询数据库 第一种写法
# # sql = "select * from t_article where title = '如何学习测试' and content = '每天通宵学习'"
# # assert len(query(sql)) != 0
# # print("发表文章成功")
# #查询数据库 第二种写法
# articleId = res1.json()["data"]["articleid"]
# sql = "select * from t_article where id = {}".format(articleId)
# assert len(query(sql)) != 0
# print("发表文章成功!")