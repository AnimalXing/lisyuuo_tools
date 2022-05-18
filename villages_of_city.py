"""寻找地级市内所有的社区和行政村"""
"""find all communities & villages in a Chinese prefecture"""
import requests
import pandas as pd
def write_txt(file,data):
    f=open(file,'a',encoding='utf-8')
    f.write(data)
    print(data,'写入',file,'成功')
    f.close()

url = 'https://xingzhengquhua.bmcx.com/331100000000__xingzhengquhua/'
html = requests.get(url).content
df_list = pd.read_html(html)
df = df_list[-1]
counties_name = []
counties_number = []
towns_name = []
towns_number = []
villages_name = []
villages_number = []
for i in range(4,len(df[0])):#find all counties
    print(df[0][i])
    counties_name.append(df[0][i])
    print(df[1][i])
    counties_number.append(df[1][i])
for j in range(len(counties_name)):#find all towns
    print("查找"+counties_name[j]+"下属行政单位中")
    url = 'https://xingzhengquhua.bmcx.com/'+ counties_number[j] +'__xingzhengquhua/'
    html = requests.get(url).content
    df_list = pd.read_html(html)
    df = df_list[-1]
    for k in range(4, len(df[0])):
        if "撤销" in df[0][k] or "*" in df[0][k]:
            continue
        print(df[0][k])
        towns_name.append(df[0][k])
        print(df[1][k])
        towns_number.append(df[1][k])
for l in range(len(towns_name)):#find all villages
    print("查找"+towns_name[l]+"下属行政单位中")
    write_txt('locals.txt', towns_name[l]+'下属行政单位'+'\n')
    url = 'https://xingzhengquhua.bmcx.com/'+ towns_number[l] +'__xingzhengquhua/'
    html = requests.get(url).content
    df_list = pd.read_html(html)
    df = df_list[-1]
    for m in range(4, len(df[0])):
        if "撤销" in df[0][m] or "*" in df[0][m]:
            continue
        village_name = df[0][m]+'\n'
        print(village_name)
        write_txt('locals.txt',village_name)#write names of villages


