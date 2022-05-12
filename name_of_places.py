import json
import time
import requests

def sleep(n):
    time.sleep(n)
    print("~~~sleeping~~~~")
def requested(url):
    sleep(5)
    html=requests.get(url)
    data=html.json()
    return data
def write_txt(file,data):
    f=open(file,'a',encoding='utf-8')
    f.write(data)
    print(data,'写入',file,'成功')
    f.close()
def time_now():
    time_now=time.strftime('%Y-%m-%d-%H%M%S',time.localtime(time.time()))
    print(time_now)
    return str(time_now)

def remove_prefix(name):
    if name[0:3] == "莲都区":
        print("yes!"+name[3:])
        return name[3:]
    else:
        print("no"+name)
        return name

ak ="C75tUrXIZKbn3QOMB3e9cIx7g9fsMrUo"
# url='http://api.map.baidu.com/place/v2/search?query=楚雄& bounds=24.390894,102.174112,26.548645,103.678942&page_size=20&page_num=0&output=json&ak='+ak

url_1='http://api.map.baidu.com/place/v2/search?query='
url_2='小学'#搜索关键词
url_3='&region='
url_4='莲都区'#所在城市
url_5='&page_size=20&page_num='
url_6='1'
url_7='&output=json&ak='+ak
file=time_now()+url_4+'-'+url_2+"results.txt"
for url_6 in range(20):
    url=url_1+url_2+url_3+url_4+url_5+str(url_6)+url_7
    data=requested(url)
    for item in data['results']:
        jname = item['name']
        jlat = item['location']['lat']
        jlon = item['location']['lng']
        jadd = item['address']
        j_data=remove_prefix(jname)+'\n'
        write_txt(file, j_data)
