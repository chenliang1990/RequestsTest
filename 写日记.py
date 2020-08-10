import time
now = time.strftime("%y-%m-%d %H:%M:%S")

#python制表符
# \t 的意思是在字符串中增加一个tab键的空格，\n是换行的意思
#将文件内容写进去
#"日记.txt"是相对位置，也可以把写入的文件存入F盘，可以写"F:\日记.txt"
text = input("请输入内容: ")
with open("日记.txt","a",encoding = "utf8") as f: #a是追加在后面，r是只读，w是只写，在继续写会覆盖
    f.writelines(now+"\n")
    f.write(text+"\n")
    f.write("--------------------------------\n")

