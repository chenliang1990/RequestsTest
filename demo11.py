import requests
from dbtools import query

#get请求:接口地址是字符串类型
# u = "http://192.144.148.91:2333/getarticle?pagenum=1"  
# r = requests.get(u)  #所有的相应信息，requests.get(u)发送请求
# print(r.text)  #r.text：打印接口的返回值

# 1.构造请求
u = "http://192.144.148.91:2333/login"
d = {"username":"liuyun1", "password":"a12345678"} #http json格式/python字典
r = requests.post(url = u,json = d)
print(r.text)

# 2.判断结果
assert r.status_code == 200 # 状态码
assert r.json()["status"] == 200 # 判断结果码

# 3.数据自动查询功能：一定要考虑正确的情况
sql = "select * from t_user where username='{}'".format(d["username"]) 
res = query(sql)
assert len(res) != 0

print("测试通过!")

#新增文章:文章有没有添加成功  判断文章存在
#修改文章：修改的数据有没有生效  判断字段
#删除文章：有没有删除成功 判断存在


