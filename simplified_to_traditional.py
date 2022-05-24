import chinese_converter

def write_txt(file,data):
    f=open(file,'a',encoding='utf-8')
    f.write(data)
    print(data,'写入',file,'成功')
    f.close()

f = open("locals.txt", "r")

for name in f:
    print(name)
    if "下属行政单位" in name:
        continue
    name = name.replace("村委会","")
    name = name.replace("村民委员会", "")
    name = name.replace("居委会","")
    name = name.replace("居民委员会", "")
    trad_name = chinese_converter.to_traditional(name)
    trad_name = trad_name.replace("裡","里")
    write_txt("trad_villages.txt",trad_name)
