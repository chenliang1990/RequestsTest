with open("日记.txt","r",encoding="utf8") as f:
    txt = f.readlines()
    # print(txt)

for i in txt:
    print(i)