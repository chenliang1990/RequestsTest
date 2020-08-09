from dbtools import query,commit
"""
请使用代码完成一个登陆和注册功能，并且数据要存入数据库中
"""
def checkname(username,password):
    #自动判断账号长度是5-8位，并且账号必须小写开头
    if len(username) >=  5 and len(username) <= 8:
        if username[0] in ("qwertyuiopasdfghjklzxcvbnm"):
            if len(password) >= 8 and len(password) <= 16:
                return True
            else:
                return "密码不符合规范"
        else:
            return "账号的首字母必须小写字母开头!"
    else:
        return "您输入的账号长度不符合规范，请输入5-8位的账号"
def regist():
    username = input("请输入您的账号: ")
    password = input("请输入您的密码: ")
    res = checkname(username,password)
    if res == True:
        res = query("select * from t_user where username = '{}'".format(username))
        if len(res) == 0:
            res = commit("insert into t_user (username,password) values('{}','{}')".format(username,password))
            print("注册成功!",res)
        else:
            print("账号已存在!")
    else:
        print(res)
def login():
    username = input("请输入您的账号: ")
    password = input("请输入您的密码: ")
    res = query("select * from t_user where username = '{}'".format(username))
    if len(res) != 0:
        if res[0][2] == password:
            print("登陆成功! ")
        else:
            print("登陆失败! ")
    else:
        print("对不起,账号不存在")

print("--------------------------------")
print("欢迎使用XXX系统")
print("--------------------------------")
res = input("请选择您要使用的功能:1.注册 2.登陆")
if res == '1':
    regist()
elif res == '2':
    login()
else:
    print("请选择正确的功能:1.注册 2.登陆")