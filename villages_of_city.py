"""寻找地级市内所有的社区和行政村"""
import requests
import pandas as pd

url = 'https://xingzhengquhua.bmcx.com/331100000000__xingzhengquhua/'
html = requests.get(url).content
df_list = pd.read_html(html)
df = df_list[-1]
counties_name = []
counties_number = []
villages_name = []
for i in range(4,len(df[0])-1):
    print(df[0][i])
    counties_name.append(df[0][i])
    print(df[1][i])
    counties_number.append(df[1][i])
for j in range(len(counties_name)):
    print("查找"+counties_name[j]+"下属行政单位中")
    new_url = 'https://xingzhengquhua.bmcx.com/'+ counties_number[j] +'__xingzhengquhua/'

